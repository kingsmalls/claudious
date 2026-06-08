# SLICE

Kane's knife specialists. Hit-and-run fighters who never hold ground — lunge, cut, dash out, reposition. Recruited from street fights and underground knife clubs. They're the ones who *enjoy* this work.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **9 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (4 frames)
> 4. `atk1` — FENCER'S LUNGE (6 frames) — **body fully HORIZONTAL arrow**, knife in forward grip leading like a spear
> 5. `atk2` — LOW SWEEP KICK (5 frames) — **body LOW with supporting hand braced on the floor**, free leg sweeps at ankle height
> 6. `jump_atk` — FLYING STAB (5 frames) — **AIRBORNE 45° diagonal dive**, knife in REVERSE/icepick grip pointing DOWN
> 7. `dash` (4 frames)
> 8. `hurt` (3 frames)
> 9. `dead` (3 frames)
>
> **Total: 40 frames in 9 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Slice's three attacks must each occupy a DIFFERENT silhouette quadrant — the generator's failure mode is "guy with a knife held forward, slightly different limb." If any two attacks share a silhouette, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` lunge | Body fully HORIZONTAL, parallel to ground | Front arm + knife (forward grip) | Horizontal forward at chest height | Arrow-shape — front leg fully extended forward, rear leg straight back, torso flat parallel to ground, knife leading like a spear |
> | `atk2` sweep kick | Body LOW to ground, supporting hand braced on floor | Free LEG | Horizontal ankle-height arc | Body crouched with one hand on the FLOOR — only attack that touches the ground with the hand; knife stays in the floor-hand in reverse grip |
> | `jump_atk` flying stab | AIRBORNE, body tilted 45° downward (dart) | Knife (REVERSE/icepick grip) | Vertical downward from overhead | Only aerial attack + knife held OVERHEAD in icepick grip pointing DOWN (forward grip on the lunge, reverse on this one) |
>
> Cross-checks before approving the sheet:
> - **atk1 vs jump_atk:** atk1 is GROUNDED with the knife in FORWARD grip leading horizontally; jump_atk is AIRBORNE with the knife in REVERSE/icepick grip pointing DOWN from overhead. Grip flip + grounding + direction are all opposite. If both look like "knife stabbing forward," the icepick grip on jump_atk isn't reading — redraw with the blade clearly pointing DOWNWARD from a fist held above the head.
> - **atk2 vs anything else:** atk2 is the ONLY attack where Slice's supporting HAND is on the FLOOR. If F3 doesn't show the hand braced on the ground with the body low, it's not reading as a sweep — redraw.
> - **lunge "arrow" tell:** at atk1 F3 the body must be FULLY HORIZONTAL parallel to the ground (front leg extended, rear leg straight back, torso flat). If the torso is still upright with just the arm out, that's a jab, not a lunge — redraw.
> - **Knife-grip flip readability:** the blade is reverse/icepick (along the forearm) in idle, walk, sweep, and flying stab. It is FORWARD grip (blade leading from a clenched fist) ONLY on the lunge. The visible flip during atk1 F1 is part of the character's tell.

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
- **Three signature moves — lunge / flying stab / sweep kick.**
  - **`lunge`** — A fencer's forward thrust executed with a knife instead of a foil. **Visual signature: at peak extension the body is fully horizontal** — front leg fully extended forward, rear leg straight back, torso flat parallel to the ground, knife-arm leading like a spear. The pose is unmistakably an **arrow shape** pointing at the target. 14 dmg + 120 knockback. Self-pushes 220 px.
  - **`flying_stab`** — Mid-air leaping stab. **Visual signature: F3 silhouette is body AIRBORNE and tilted DIAGONAL (45° downward), knife held in OVERHEAD reverse grip (icepick grip pointing DOWN from the fist), free arm trailing behind — the body is a falling dart with the blade leading**. Lands and rolls to recover. 16 dmg + 100 knockback.
  - **`sweep_kick`** — Low spinning leg sweep. **Visual signature: F3 the body is LOW to the ground, supporting hand braced on the floor for balance, free leg swept in a horizontal arc at ankle height to trip the target. Knife held in the hand on the floor (still reverse grip).** 12 dmg + 60 knockback. Knocks the target down.
- **Crossup-prone.** If protagonist faces away, Slice routes around to attack from the back.
- **Knife grip:** reverse / icepick grip (blade along the forearm) in idle and walk. **Flips to forward grip (blade leading)** on the lunge wind-up — the visible flip is part of the visual identity. Reverse grip returns on the flying stab.

## Animations

| Slot     | Frames | Notes |
|----------|-------:|-------|
| `idle`   | 4 | **Bouncing weight shift** — never still. Knife reverse-grip against the right forearm. Body angled 30° toward the camera (boxer's blade-stance). |
| `walk`   | 6 | **Light prowling cycle that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT leg fwd + RIGHT arm fwd swing. F2 = passing. F3 = RIGHT leg fwd + LEFT arm fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Both arms swing in a relaxed arc AT THE SIDES** — knife arm swings too, blade still reverse-grip along the forearm. Arms NEVER extend forward past the body (would read as the lunge wind-up). No planted/stomp pose on F6. Feet barely lift. |
| `run`    | 4 | 4-frame loop that blends seamlessly (F4 → F1). F1 = LEFT foot strike + right arm fwd swing. F2 = airborne, arms pumping at sides. F3 = RIGHT foot strike + left arm fwd swing. F4 = airborne → blends into F1. **Arms PUMP at the sides** (elbows bent, hands at hip-to-chest height) — knife arm pumps too, blade still reverse-grip along the forearm. Arms NEVER extend forward past the body (would read as the lunge or flying stab). **2-px motion lines behind both heels** on F1 and F3. |
| `atk1`   | 6 | **Lunge.** F1 = coil (knees deep bent, knife at hip, **blade flips to forward grip**). F2 = launch (front leg explodes forward, rear leg extends back). F3 = **arrow pose — body fully horizontal, knife leading 24 px past the front foot, rear leg straight, 4-px motion-line streak behind the knife**. F4 = active stab held one frame. F5 = miss-pose (body extended, blade swung past). F6 = recoil pull-back. |
| `atk2`   | 5 | **Sweep kick.** F1 = body drops low, supporting hand reaches for the floor. F2 = body crouched, **supporting hand braced on the floor (knife in that hand, blade still reverse-grip)**, free leg starts sweeping. F3 = **peak — body low, supporting hand on floor, free leg horizontal at ankle height sweeping in a 90° arc**. F4 = follow-through, leg past midline. F5 = recovery, back to stance. |
| `jump_atk` | 5 | **Flying stab.** F1 = coil-and-leap (knees bend then explode upward). F2 = airborne, body rotating to diagonal, **knife arm rising overhead, blade in reverse grip pointing DOWN like an icepick**. F3 = **peak airborne — body diagonal at 45° downward angle, knife in icepick grip held overhead pointing down, free arm trailing behind, falling toward the target like a dart**. F4 = descent, blade leading downward. F5 = land + recover. |
| `dash`   | 4 | Backward dash after lunge. Body low (knees deep), **knife held across the chest** as a guard. Motion lines trail FORWARD from the heels because he's reversing direction. |
| `hurt`   | 3 | Body folds. Knife arm drops to hip. |
| `dead`   | 3 | Crumples sideways. **Knife slides 6 px from the open hand** on F3. |

## DO NOT include

- Multiple knives / dual wield — single bowie only.
- Bulky armor — Slice is FAST.
- Gun on the hip — Slices don't carry guns.
- The bandana from Runner's bicep.

## Visual VFX summary

Slice's identity is the **knife grip flips** + low fencer's stance + motion lines on rapid attacks. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` FENCER'S LUNGE — body fully HORIZONTAL arrow pointing at target (front leg extended, rear leg straight back, torso flat parallel to ground), knife in FORWARD grip leading, 4-px motion-line streak behind the knife
- `atk2` LOW SWEEP KICK — body LOW with supporting HAND BRACED ON THE FLOOR (the only attack that touches the ground with the hand), free leg sweeping horizontally at ankle height in a 120° arc, knife in floor-hand still in reverse grip
- `jump_atk` FLYING STAB — body AIRBORNE at 45° downward diagonal (falling dart), knife held OVERHEAD in REVERSE/icepick grip pointing DOWN, free arm trailing behind

**Hurt / flinch:** F1 body folds, knife arm drops to hip but doesn't release. F2 cocky half-smile finally drops. 1-px white impact spark.

**Dead:** Crumples sideways. Knife slides 6 px from the open hand on F3 — first frame he ever lets it go.

## Sheet specs

- 8 columns × 4 rows = 32 cells
- Cell size: **48 × 72**
- Magenta `#ff00ff` background
- Bottom-center anchor — Slice's knife should be visible at the silhouette edge in idle frames
