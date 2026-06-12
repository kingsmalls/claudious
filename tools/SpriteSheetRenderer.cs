// SpriteSheetRenderer.cs
//
// Unity Editor tool that renders a rigged humanoid character's animations
// to a sprite sheet PNG + atlas JSON that The Block engine can load directly.
//
// HOW TO USE:
//   1. Drop this file into Assets/Editor/ in your Unity project
//   2. Set up a scene with:
//        a. The KayKit character placed at world origin, FACING +X (camera-right)
//        b. An Orthographic Camera looking along -Z, framing the character
//           (default settings: position (0, 1, -5), orthographic size 1.2)
//        c. A bright Directional Light from above-front
//   3. Open Window -> The Block -> Render Sprite Sheet
//   4. Drag the character GameObject into "Character"
//   5. Drag the camera into "Render Camera"
//   6. Set output name (rio / duke / atlas / baron / etc.)
//   7. Click "Render All Animations"
//
// Output: Assets/RenderedSprites/<name>.png + <name>_atlas.json
// Copy BOTH files into characters/ in the The Block repo. The engine
// picks them up automatically.
//
// Works with any rigged character + AnimatorController that has the clips
// you want to render as states (KayKit Adventurers, Kevin Iglesias Melee
// Animations, etc.)

using System.Collections.Generic;
using System.IO;
using System.Text;
using UnityEditor;
using UnityEngine;

public class SpriteSheetRenderer : EditorWindow {
    GameObject character;
    Camera renderCamera;
    string outputName = "rio";
    string outputFolder = "Assets/RenderedSprites";
    int frameSize = 256;
    int framesPerAnim = 8;
    int targetH = 96;
    int fps = 10;
    bool useNameMap = true;

    // KayKit / Kevin Iglesias clip names -> The Block engine anim slots.
    // The slicer is permissive about extra anims, but mapping the common
    // ones gets you idle/walk/run/attacks wired to the right input bindings.
    static readonly Dictionary<string, string> DEFAULT_NAME_MAP = new Dictionary<string, string> {
        // KayKit Adventurers
        {"Idle",                        "idle"},
        {"Idle_Combat",                 "idle"},
        {"Walking_A",                   "walk"},
        {"Walking_B",                   "walk"},
        {"Running_A",                   "run"},
        {"Running_B",                   "run"},
        {"Jump_Start",                  "jump"},
        {"Jump_Idle",                   "jump"},
        {"Jump_Land",                   "jump"},
        {"1H_Melee_Attack_Slice_Diagonal", "atk1"},
        {"1H_Melee_Attack_Slice_Horizontal", "atk2"},
        {"1H_Melee_Attack_Chop",        "atk3"},
        {"1H_Melee_Attack_Stab",        "heavy"},
        {"2H_Melee_Attack_Slice",       "atk1"},
        {"2H_Melee_Attack_Spin",        "special"},
        {"2H_Melee_Attack_Chop",        "atk3"},
        {"Unarmed_Melee_Attack_Punch_A", "atk1"},
        {"Unarmed_Melee_Attack_Punch_B", "atk2"},
        {"Unarmed_Melee_Attack_Kick",   "atk3"},
        {"Hit_A",                       "hurt"},
        {"Hit_B",                       "hurt"},
        {"Death_A",                     "dead"},
        {"Death_B",                     "dead"},
        {"Dodge_Backward",              "dodge"},
        {"Dodge_Forward",               "dodge"},
        {"Block",                       "counter"},
        {"Throw",                       "throw"},
        // Kevin Iglesias Melee
        {"Punch1",                      "atk1"},
        {"Punch2",                      "atk2"},
        {"Kick1",                       "atk3"},
        {"Kick2",                       "atk4"},
        {"AttackUppercut",              "heavy"},
        {"AttackJump",                  "jump_atk"},
    };

    [MenuItem("The Block/Render Sprite Sheet")]
    public static void ShowWindow() {
        var w = GetWindow<SpriteSheetRenderer>();
        w.titleContent = new GUIContent("Render Sprite Sheet");
        w.minSize = new Vector2(380, 360);
        w.Show();
    }

    void OnGUI() {
        GUILayout.Label("The Block — Sprite Sheet Renderer", EditorStyles.boldLabel);
        EditorGUILayout.LabelField(
            "Renders one rigged character's animations to a sprite sheet + atlas JSON " +
            "consumable by the_block.html engine.",
            EditorStyles.wordWrappedMiniLabel
        );
        EditorGUILayout.Space();

        character = (GameObject)EditorGUILayout.ObjectField("Character", character, typeof(GameObject), true);
        renderCamera = (Camera)EditorGUILayout.ObjectField("Render Camera", renderCamera, typeof(Camera), true);
        EditorGUILayout.Space();

        outputName = EditorGUILayout.TextField("Output name", outputName);
        outputFolder = EditorGUILayout.TextField("Output folder", outputFolder);
        frameSize = EditorGUILayout.IntField("Frame size (px square)", frameSize);
        framesPerAnim = EditorGUILayout.IntField("Frames per anim", framesPerAnim);
        targetH = EditorGUILayout.IntField("Engine display height", targetH);
        fps = EditorGUILayout.IntField("Anim fps", fps);
        useNameMap = EditorGUILayout.Toggle("Map KayKit names → engine names", useNameMap);

        EditorGUILayout.Space();
        EditorGUILayout.HelpBox(
            "Camera: orthographic, Clear Flags = Solid Color, Background = (0,0,0,0). " +
            "Character should face +X (screen-right) at idle — the game engine mirrors for left-facing.",
            MessageType.Info
        );

        GUI.enabled = character != null && renderCamera != null;
        if (GUILayout.Button("Render All Animations", GUILayout.Height(36))) {
            try { Render(); }
            catch (System.Exception e) {
                EditorUtility.ClearProgressBar();
                EditorUtility.DisplayDialog("Render failed", e.Message, "OK");
                Debug.LogException(e);
            }
        }
        GUI.enabled = true;
    }

    void Render() {
        var animator = character.GetComponent<Animator>();
        if (animator == null || animator.runtimeAnimatorController == null) {
            EditorUtility.DisplayDialog("Missing Animator",
                "Character GameObject needs an Animator with an AnimatorController assigned.", "OK");
            return;
        }

        var clips = animator.runtimeAnimatorController.animationClips;
        if (clips.Length == 0) {
            EditorUtility.DisplayDialog("No clips",
                "AnimatorController has no clips. Assign one with the animations you want to render.", "OK");
            return;
        }

        Directory.CreateDirectory(outputFolder);

        int sheetW = frameSize * framesPerAnim;
        int sheetH = frameSize * clips.Length;
        var sheet = new Texture2D(sheetW, sheetH, TextureFormat.RGBA32, false);
        var blank = new Color[sheetW * sheetH];
        sheet.SetPixels(blank);

        var rt = RenderTexture.GetTemporary(frameSize, frameSize, 24, RenderTextureFormat.ARGB32);
        var prevTarget = renderCamera.targetTexture;
        var prevClear = renderCamera.clearFlags;
        var prevBg = renderCamera.backgroundColor;
        renderCamera.targetTexture = rt;
        renderCamera.clearFlags = CameraClearFlags.SolidColor;
        renderCamera.backgroundColor = new Color(0, 0, 0, 0);

        var frames = new List<FrameRecord>();
        var anims = new List<AnimRecord>();

        try {
            for (int row = 0; row < clips.Length; row++) {
                var clip = clips[row];
                string animName = CleanName(clip.name);
                var frameNames = new List<string>();

                EditorUtility.DisplayProgressBar(
                    "Rendering sprite sheet",
                    $"{animName} ({row + 1}/{clips.Length})",
                    (float)row / clips.Length
                );

                for (int f = 0; f < framesPerAnim; f++) {
                    float t = ((float)f / framesPerAnim) * clip.length;
                    // SampleAnimation pose the rig directly without going through
                    // the controller state machine. Works for Generic + Humanoid.
                    clip.SampleAnimation(character, t);

                    RenderTexture.active = rt;
                    GL.Clear(true, true, new Color(0, 0, 0, 0));
                    renderCamera.Render();

                    var frame = new Texture2D(frameSize, frameSize, TextureFormat.RGBA32, false);
                    frame.ReadPixels(new Rect(0, 0, frameSize, frameSize), 0, 0);
                    frame.Apply();

                    int dstX = f * frameSize;
                    int dstY_unity = (clips.Length - 1 - row) * frameSize;
                    sheet.SetPixels(dstX, dstY_unity, frameSize, frameSize, frame.GetPixels());
                    DestroyImmediate(frame);

                    string frameName = $"{animName}_{f}";
                    frameNames.Add(frameName);
                    // Atlas JSON uses top-left origin; convert.
                    int dstY_topleft = sheetH - dstY_unity - frameSize;
                    frames.Add(new FrameRecord {
                        name = frameName,
                        x = dstX, y = dstY_topleft,
                        w = frameSize, h = frameSize
                    });
                }

                anims.Add(new AnimRecord { name = animName, frames = frameNames });
            }
        } finally {
            EditorUtility.ClearProgressBar();
            RenderTexture.active = null;
            renderCamera.targetTexture = prevTarget;
            renderCamera.clearFlags = prevClear;
            renderCamera.backgroundColor = prevBg;
            RenderTexture.ReleaseTemporary(rt);
        }

        sheet.Apply();

        string pngPath = $"{outputFolder}/{outputName}.png";
        File.WriteAllBytes(pngPath, sheet.EncodeToPNG());
        Debug.Log($"<color=lime>Saved sprite sheet:</color> {pngPath}");

        string jsonPath = $"{outputFolder}/{outputName}_atlas.json";
        File.WriteAllText(jsonPath, BuildAtlasJson(frames, anims));
        Debug.Log($"<color=lime>Saved atlas:</color> {jsonPath}");

        AssetDatabase.Refresh();

        EditorUtility.DisplayDialog("Done",
            $"Rendered {clips.Length} animations × {framesPerAnim} frames\n\n" +
            $"PNG : {pngPath}\nJSON: {jsonPath}\n\n" +
            "Copy both files into the_block repo's characters/ folder.",
            "OK"
        );
    }

    string CleanName(string raw) {
        if (useNameMap && DEFAULT_NAME_MAP.TryGetValue(raw, out var mapped)) return mapped;
        return raw.ToLower().Replace(' ', '_').Replace("|", "_").Replace("-", "_");
    }

    string BuildAtlasJson(List<FrameRecord> frames, List<AnimRecord> anims) {
        var sb = new StringBuilder();
        sb.Append("{\n");
        sb.AppendFormat("  \"fps\": {0},\n", fps);

        // Frames
        sb.Append("  \"frames\": {\n");
        for (int i = 0; i < frames.Count; i++) {
            var fr = frames[i];
            sb.AppendFormat("    \"{0}\": {{\"x\": {1}, \"y\": {2}, \"w\": {3}, \"h\": {4}, \"th\": {5}}}",
                fr.name, fr.x, fr.y, fr.w, fr.h, targetH);
            sb.Append(i < frames.Count - 1 ? ",\n" : "\n");
        }
        sb.Append("  },\n");

        // Anims — collapse duplicates (e.g. multiple Idle clips both mapping to "idle")
        var unique = new Dictionary<string, List<string>>();
        var order = new List<string>();
        foreach (var a in anims) {
            if (!unique.ContainsKey(a.name)) {
                unique[a.name] = new List<string>();
                order.Add(a.name);
            }
            unique[a.name].AddRange(a.frames);
        }

        sb.Append("  \"anims\": {\n");
        for (int i = 0; i < order.Count; i++) {
            var name = order[i];
            sb.AppendFormat("    \"{0}\": [", name);
            for (int j = 0; j < unique[name].Count; j++) {
                sb.AppendFormat("\"{0}\"", unique[name][j]);
                if (j < unique[name].Count - 1) sb.Append(", ");
            }
            sb.Append("]");
            sb.Append(i < order.Count - 1 ? ",\n" : "\n");
        }
        sb.Append("  },\n");

        sb.Append("  \"anchor\": {\"x\": 0.5, \"y\": 1.0},\n");
        sb.AppendFormat("  \"target_h\": {0}\n", targetH);
        sb.Append("}\n");
        return sb.ToString();
    }

    class FrameRecord { public string name; public int x, y, w, h; }
    class AnimRecord { public string name; public List<string> frames; }
}
