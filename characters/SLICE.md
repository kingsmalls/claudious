# SLICE

Kane's knife specialists. Hit-and-run fighters who never hold ground — lunge, cut, dash out, reposition. Recruited from street fights and underground knife clubs. They're the ones who *enjoy* this work.

## Physical

- **Age range:** 22–32
- **Height/build:** 5'6" – 5'10", lean and fast. Whip-thin.
- **Body language:** Always shifting weight. Never stands flat — bobs and weaves on the balls of the feet. Knife held in a reverse grip, blade along the forearm.
- **Face:** Visible. A cocky half-smile in idle. Some have small scars across cheek or eyebrow.

## Hair

- Varied. Side-shaved with a long top, slicked back; or a tied back ponytail; or a mullet. Pick a memorable silhouette per spawn.

## Costume (head to feet)

1. **Sleeveless mesh shirt** — black (`#0a0a10`), tight, exposing arms. Some have a fishnet undershirt visible at the collar.
2. **Studded vest** (optional) over the mesh — dark grey (`#36363f`) leather with metallic stud rivets (`#a8a8b0`).
3. **Skinny pants** — black (`#1a1a22`), tight, ankle-length.
4. **Combat boots** — black, laced loose at the top, scuffed.
5. **Fingerless gloves** — black leather (`#16100a`).

## Identity item — REQUIRED IN EVERY FRAME

**A bowie knife held in a reverse grip in the dominant hand.** Blade against the forearm in idle (concealed line); flips out forward during the lunge. Steel-grey blade (`#cfd0d6`) with a black handle (`#0a0a10`) and a small wrist-strap. ~14 px long when extended. The knife is always visible — it's what makes Slice *Slice*.

## Palette (hex)

```
mesh shirt         #0a0a10
vest leather       #36363f
vest stud          #a8a8b0
pants              #1a1a22
glove              #16100a
boot               #0a0a10
skin (light)       #d4a888    (vary)
skin (shadow)      #9a785a
hair               #1a1410     (vary)
knife blade        #cfd0d6
knife edge hi      #ffffff
knife handle       #0a0a10
```

## Personality / fighting style

- **Always in motion.** Hit-and-run — lunges in, knife flicks, dashes back 35 px. Never sits in melee range.
- **Signature move — `lunge`:** A fencer's forward thrust executed with a knife instead of a foil. **Visual signature: at peak extension the body is fully horizontal** — front leg fully extended forward, rear leg straight back, torso flat parallel to the ground, knife-arm leading like a spear. The pose is unmistakably an **arrow shape** pointing at the target. 14 dmg + 120 knockback + self-pushes 220 px forward (the lunge itself is movement).
- **Crossup-prone.** If protagonist faces away, Slice routes around to attack from the back.
- **Knife grip:** reverse / icepick grip (blade along the forearm) in idle and walk. **Flips to forward grip (blade leading)** on the lunge wind-up — the visible flip is part of the visual identity.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | **Bouncing weight shift** — never still. Knife reverse-grip against the right forearm. Body angled 30° toward the camera (boxer's blade-stance). |
| `walk`   | 6 | Light, prowling steps. **Knife arm forward, free hand low** as counter-weight. Feet barely lift. |
| `run`    | 4 | Sprint with **2-px motion lines behind both heels**. Knife extended forward like a spear-tip. |
| `atk1`   | 6 | **Lunge.** F1 = coil (knees deep bent, knife at hip, **blade flips to forward grip**). F2 = launch (front leg explodes forward, rear leg extends back). F3 = **arrow pose — body fully horizontal, knife leading 24 px past the front foot, rear leg straight, 4-px motion-line streak behind the knife**. F4 = active stab held one frame. F5 = miss-pose (body extended, blade swung past). F6 = recoil pull-back. |
| `dash`   | 4 | Backward dash after lunge. Body low (knees deep), **knife held across the chest** as a guard. Motion lines trail FORWARD from the heels because he's reversing direction. |
| `hurt`   | 3 | Body folds. Knife arm drops to hip. |
| `dead`   | 3 | Crumples sideways. **Knife slides 6 px from the open hand** on F3. |

## DO NOT include

- Multiple knives / dual wield — single bowie only.
- Bulky armor — Slice is FAST.
- Gun on the hip — Slices don't carry guns.
- The bandana from Runner's bicep.

## Sheet specs

- 8 columns × 4 rows = 32 cells
- Cell size: **48 × 72**
- Magenta `#ff00ff` background
- Bottom-center anchor — Slice's knife should be visible at the silhouette edge in idle frames
