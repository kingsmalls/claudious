# RIO

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **16 distinct animation rows** in this exact order, one anim per row, no skipping, no merging:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `run` (6 frames)
> 4. `jump` (3 frames)
> 5. `atk1` — JAB (4 frames) — **FRONT fist HORIZONTAL forward** at head height
> 6. `atk2` — CROSS (5 frames) — **REAR fist HORIZONTAL forward**, body rotated 45°
> 7. `atk3` — ROUNDHOUSE KICK (6 frames) — **leg HORIZONTAL at chest height**, shin parallel to floor, body torqued 90°
> 8. `atk4` — SPINNING BACK KICK (6 frames) — **AIRBORNE 270° spin**, heel VERTICAL above the head, bandana traces a full circle
> 9. `heavy` — UPPERCUT LAUNCHER (7 frames) — **ONE front fist RISING vertically** from hip to above the head
> 10. `jump_atk` — FLYING KNEE (4 frames) — **AIRBORNE**, lead knee forward at chest height
> 11. `back_atk` — REAR ELBOW (4 frames) — **body twisted BACKWARD 60°**, elbow behind body
> 12. `special` — SUNSET SPIN (12 frames) — sweep halo at hip + rising double-uppercut (multi-phase)
> 13. `throw` (5 frames) — overhead spin throw
> 14. `counter` — CHECK HOOK (6 frames) — **body PIVOTED 90° sideways off-line**, lead fist hooks tight at head height (the only sideways-facing punch)
> 15. `hurt` (3 frames)
> 16. `dodge` — backward roll (5 frames)
>
> **Total: 86 frames in 16 rows.** If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Rio's sheet kept producing attacks that all looked like "boxer in stance throwing a similar punch." Every attack below must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one.
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` jab | Vertical, ~5° rotation | FRONT (left) fist | Horizontal forward | Body almost upright, front shoulder forward; bandana 12-px horizontal ribbon trail |
> | `atk2` cross | Rotated 45° from hip | REAR (right) fist | Horizontal forward | Hip drove forward; bandana whips OPPOSITE the cross fist (yellow X across body) |
> | `atk3` roundhouse | Torqued sideways 90° | LEFT shin (chamber) | Horizontal at chest height | Leg parallel to ground at chest height — only chest-height side kick |
> | `atk4` spinning back kick | AIRBORNE mid-rotation | Right heel | Vertical, heel UP | Body airborne with heel ABOVE the head + bandana traces full 360° circle |
> | `heavy` uppercut | Vertical, extending upward | ONE front fist | Ascending vertical | Single rising fist + bandana streaks STRAIGHT UP as vertical yellow column |
> | `jump_atk` flying knee | AIRBORNE, angled forward | Lead knee | Forward at chest height (mid-air) | Body airborne with the KNEE leading + bandana diagonal ribbon |
> | `back_atk` rear elbow | Twisted BACKWARD 60° | Right elbow | Backward | Body turned AWAY from camera — only rear-facing attack |
> | `special` sunset spin | Multi-phase, grounded | Leg sweep + double fist | Hip sweep + ascending double | Yellow HALO ribbon at hip level + free-floating yellow streak above head |
> | `throw` overhead spin | Body rotating 90° overhead | Both hands grip | Overhead spin | Both hands gripping at chest height then enemy pivots overhead — only grappling pose |
> | `counter` check hook | PIVOTED 90° SIDEWAYS off-line | Lead fist | Tight horizontal hook to the SIDE | Body fully sideways to the camera (profile silhouette) — only sideways-facing punch |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = FRONT fist, body almost vertical with ~5° rotation. atk2 = REAR fist, hip drove forward 45°. If both look like the same arm punching, redraw atk2 so the rear shoulder is clearly rotated over.
> - **atk3 vs atk4:** atk3 = horizontal shin at chest height with body torqued but planted. atk4 = AIRBORNE mid-spin with heel VERTICAL above the head. Different orientation (horizontal vs vertical) and different grounding (planted vs airborne).
> - **atk3/atk4 vs jump_atk:** all leg attacks — but atk3 is GROUNDED, atk4 is airborne SPINNING with heel up, jump_atk is airborne with KNEE forward (not heel up). Three distinct silhouettes.
> - **heavy vs counter:** heavy goes straight UP (single fist ascending vertical column). counter is a hook arcing INWARD HORIZONTALLY with body PIVOTED SIDEWAYS. Opposite directions and opposite body orientations.
> - **counter vs any other punch:** counter is the only attack where Rio is fully PROFILE-SIDEWAYS to the camera. If counter shows her facing forward, redraw — the off-line pivot IS the move's identity.
> - **special vs heavy:** special's uppercut uses BOTH fists rising; heavy uses ONE fist. If they look the same, redraw heavy with the rear fist clearly DOWN at the hip on F1–F2 so the rise is visible.

## Physical

- **Age:** 24
- **Height/build:** 5'5", lean athletic — boxer's frame. Visible deltoids and forearms; not bulky, not slight. Tapered waist. Knees slightly bent in idle (fighting stance).
- **Ethnicity:** Black; deep brown skin.
- **Body language:** Centered, low. Stays on the balls of her feet. Hands up by default — guard never fully drops.
- **Face:** Strong jaw, broad cheekbones. Dark eyebrows, deep brown eyes. Straight nose, full lips. Resting expression is calm/focused, not angry. **The smile only appears on a clean combo finisher** — that's the one moment her face changes.

## Hair

- **Style:** Full afro, dark brown to black, ~3–4 inches deep. Round, soft silhouette around the head; not picked super-tall, not pressed down — natural shape. A few strands fall forward over the forehead.
- **Movement:** The afro **bounces visibly with hard motion** — compresses on landings, rises with the Sunset Spin, lifts at the apex of jumps. Springy, not flowing.

## Costume (head to feet)

1. **Earring:** Single small gold hoop (≈1px sprite), camera-side ear only.
2. **Neck:** Bare. No jewelry.
3. **Tank top:** Black ribbed, snug. Visible only where the cropped jacket leaves it exposed (lower torso strip and upper chest collar).
4. **Bomber jacket:** Cropped (ends at lower ribs). Olive/sage green, faded. Two slash pockets at hip line. Knit collar, cuffs, and hem in slightly darker olive. Zipper open about a third of the way down. **Sleeves end mid-forearm**, leaving wrists exposed.
5. **Hand wraps:** Off-white/cream cotton, wrapped 4 times around the knuckles and back of hand. Clean white, slightly worn at the edges. Knuckles exposed (no full glove). Both wrists wrapped.
6. **YELLOW BANDANA:** **Bright marigold yellow, tied around the LEFT wrist over the hand wraps.** A small knot tail (2 pixels) hangs off. The bandana is the single most important visual element — it must be visible in every frame, on the camera side of her body when possible. It TRAILS through fast motion (jabs, the spin, the uppercut, the dodge roll).
7. **Pants:** Slim-cut cargo pants, near-black charcoal. Two cargo pockets on the thighs, low-profile (not bulky). Tapered to the ankle.
8. **Boots:** Ankle-high lace-up boxing boots, black with white soles. Laces black. Toe slightly worn.

## Palette (hex)

```
skin (light)        #8a5235
skin (shadow)       #6b3f2a
hair (afro)         #1a1410
hair (highlight)    #2a201a
jacket (mid)        #7d8d4f
jacket (shadow)     #5a6b3a
jacket (highlight)  #9bab6a
tank black          #0a0a10
pants               #1a1a22
pants shadow        #0e0e15
boot                #0a0a10
boot sole           #d8d8c0
hand wraps          #dcd6c4
hand wraps shadow   #a8a294
BANDANA highlight   #ffd76a
BANDANA mid         #e8c04a
BANDANA shadow      #b89426
earring             #e8c04a
eye whites          #ffffff
```

## Personality cues that should show in poses

- **Calm head, busy hands.** In idle, her face is neutral but her fists are always ready.
- **Economy of motion.** No wasted limbs. Every frame's silhouette reads as deliberate.
- **The SMILE.** Reserved for the third hit of a combo (atk3) and the Sunset Spin's uppercut finisher. One frame, brief, almost imperceptible — but there.
- **Defensive footwork.** Walks on the balls of her feet, never flat-footed.

## Animations (per slot — pose + key pose details)

### `idle` (4 frames, loops, 6 fps)
- Frames 1, 3: bounce-down — knees bent slightly, weight on the front foot, hands at chin level.
- Frames 2, 4: bounce-up — slight rise, afro lifts 1px.
- Bandana visible on left wrist throughout, hanging slightly.
- Eyes scanning forward. Mouth neutral.

### `walk` (6 frames, 8 fps) — **must read clearly as LOCOMOTION, never an attack**
- 6-frame stride cycle that LOOPS SEAMLESSLY (F6 blends back into F1).
- F1 = LEFT leg forward + RIGHT arm forward swing (opposite-side arm)
- F2 = passing position (feet roughly under body, arms at sides)
- F3 = RIGHT leg forward + LEFT arm forward swing
- F4 = passing position
- F5 = LEFT leg forward again (mirror of F1)
- F6 = passing position — blends straight back into F1
- **Both arms swing in a relaxed arc AT THE SIDES.** Fists loosely closed at hip level.
- Afro bounces subtly (1–2 px).
- Bandana sways with the wrist on the swinging arm.
- **NEVER**: arms reaching forward past the body, fists extended like a punch, a planted stomp-foot pose, body leaned forward in attack stance. Walk is calm forward travel — not combat prep.

### `run` (6 frames, 12 fps) — locomotion, NOT a punch chain
- 6-frame run cycle, looping seamlessly.
- Body leans forward 5–10° (slightly more committed than walk).
- Knees lift HIGHER than walk; brief airborne stride frames (F2 and F5 both feet off ground for 1 frame).
- **Arms pump UP and DOWN at the sides like a sprinter** — fists loosely closed at hip-to-chest height, elbows bent.
- **Arms NEVER extend forward past the body.** No punching motion, no grab pose.
- Frames 3 and 6 have horizontal speedlines (2 px) behind the trailing heel.
- Afro bounces more visibly than walk.
- Bandana trails behind on the back-swing.
- **NEVER**: a frame where her arm reaches forward (reads as grab attempt), a frame with fist extended at chest height (reads as shadow-boxing).

### `jump` (3 frames, 8 fps — non-looping)
- F1: anticipation crouch — knees deep bend, arms drop.
- F2: peak/airborne — body extended, knees tucked slightly under, both fists raised.
- F3: landing — knees absorb, body re-collapsing toward idle.

### `atk1` — JAB (4 frames, 12 fps)
**Visual signature:** quick straight punch — **the yellow wrist bandana trails behind the fist in a 12-px horizontal ribbon** through F2–F3. This is the move's identity; the bandana is what reads as "Rio's jab" from across the screen.
- F1: wind-up — front arm cocks back 4–6 px, body rotates slightly. Bandana hangs at the wrist.
- F2: extend — front fist reaches forward to ~14 px past the body. **Yellow bandana streaks behind the fist as a 12-px horizontal ribbon trail**.
- F3: peak — fist fully extended, knuckles forward, **bandana fully extended forward like a yellow comet tail**.
- F4: retract — fist returns 75%, bandana settling back to the wrist.

### `atk2` — CROSS (5 frames, 11 fps)
**Visual signature:** the rear fist drives across the body line — the bandana is on the NOW-RETREATING front arm, so it whips behind the body in the OPPOSITE direction from the cross fist (creating an X of motion).
- F1: wind-up — REAR arm cocks back, hip rotates back. Bandana hangs.
- F2: rotation — hip drives forward, rear shoulder rotates over. Bandana arm pulls back, **bandana whipping backward**.
- F3: extend — rear fist crosses the body line, reaching ~18 px forward. **Bandana streaks BEHIND the body on the retreating front arm — opposite direction from the cross fist**.
- F4: peak — fist fully extended, body rotated ~45°.
- F5: retract — body unwinds back toward forward stance, bandana settles.

### `atk3` — ROUNDHOUSE KICK (6 frames, 11 fps) — chains into atk4
**Visual signature:** chest-height side roundhouse. **F3 silhouette: supporting leg planted, kicking leg horizontal at chest height with the shin parallel to the ground, top-of-foot leading, body torqued 90°. Yellow bandana streaks behind the kicking foot as a horizontal yellow ribbon.**
- F1: wind-up — body coils, kicking (rear) leg starts lifting, supporting foot pivots.
- F2: chamber — kicking knee rises to chest height to the side, body torquing back.
- F3: **peak kick — leg horizontal at chest height, shin parallel to ground, body rotated 90°. Yellow bandana ribbon trails behind the kicking foot.**
- F4: follow-through — leg past target, body fully torqued.
- F5: leg retraction, body unwinds.
- F6: recovery — leg returns to stance, bandana settles. **Chains into atk4 if light pressed.**

### `atk4` — SPINNING BACK KICK (6 frames, 11 fps) — combo finisher
**Visual signature:** the FINISHER is a full 270° spin into a vertical heel kick — completely different silhouette from atk3's horizontal roundhouse. **F4 peak: body airborne mid-spin, kicking leg VERTICAL with heel up over the head, free arm extended for balance, yellow bandana traces a complete 360° CIRCLE around her body across the four spin frames (F2–F5). F5 the reserved smile appears — the finisher tell.**
- F1: wind-up — supporting foot pivots 90°, body starts rotating away from the target (giving them her back briefly).
- F2: spin begins — body 90° through rotation, kicking leg lifting OFF the ground. Bandana arcs out.
- F3: spin continues — body 180° (back fully to target), kicking leg horizontal at chest height. Bandana at 9 o'clock position.
- F4: **peak — body 270° rotation completed, kicking leg now VERTICAL with the heel raised above her head (heel-up axe-kick orientation), body airborne. Bandana at 12 o'clock above her, having traced a full circle**.
- F5: **BRIEF SMILE — mouth corner lifts 1 px. The only Rio frame where she smiles.** Heel drives downward toward the target.
- F6: landing — supporting foot plants, kicking leg retracts, body squares back up to neutral facing. Bandana resettles at the wrist.

### `heavy` — UPPERCUT LAUNCHER (7 frames, 10 fps)
**Visual signature:** vertical upward fist drive — **the bandana rockets STRAIGHT UP with the rising fist, creating a vertical yellow streak from wrist to above her head**. The only vertical-bandana move.
- F1: deep crouch — body drops, weight on rear leg, front fist drops to hip.
- F2: load — front fist near hip, body coiled.
- F3–F4: rise — body straightens explosively, front fist drives upward in a vertical line. **Bandana trails STRAIGHT UP as a vertical yellow streak following the rising wrist**.
- F5: peak — fist directly above body line, arm fully extended skyward. **Bandana drawn as a vertical streak from her wrist to 14 px above her head**.
- F6: hold — pose held for emphasis (1 frame).
- F7: recovery — body lowers back to stance, fist comes down, bandana settles.

### `jump_atk` — FLYING KNEE (4 frames, 10 fps)
**Visual signature:** mid-air diving knee strike. **F3 silhouette is body airborne at peak height, lead knee driven HIGH and FORWARD with the lower leg tucked under for compactness, both arms thrown wide for balance, bandana streaking behind the leading wrist as a downward diagonal ribbon**. Knee-leading shape reads from across the screen.
- F1: airborne preparation — body airborne and rising, front knee lifts toward chest.
- F2: extend — front knee drives forward and slightly downward, body angles 30° forward.
- F3: **peak — knee fully forward at chest-of-target height, lower leg tucked, body airborne, arms wide. Bandana trails behind the wrist as a diagonal yellow ribbon**.
- F4: recovery — body resets toward landing.

### `back_atk` — REAR ELBOW (4 frames, 12 fps)
- F1: wind-up — body turns slightly toward the rear, rear elbow lifts.
- F2: drive — elbow drives back behind the body.
- F3: peak — elbow fully extended *behind* her, body twisted.
- F4: recovery — body unwinds.

### `special` — SUNSET SPIN (12 frames, 12 fps)
The signature.
**Visual signature:** TWO distinct phases. First the spinning leg sweep — the bandana traces a complete **horizontal yellow halo** around her body (motion-blurred ribbon at ankle level). Then the rising double-fist uppercut — both bandana and both fists rocket UP, and on F10 the **bandana is drawn ABOVE her head as a free-floating yellow streak**, having flown off the wrist trajectory.
- F1: low crouch, weight loaded on the back foot.
- F2: pivot — front foot plants, body begins to rotate.
- F3–F4: **leg sweep — back leg sweeps in a 180° arc at ankle height. Bandana trails wide tracing a horizontal yellow halo around her at hip level (motion-blurred ribbon)**.
- F5: rotation continues — body fully rotated, leg planting.
- F6: recovery from sweep — body straightens.
- F7: load — feet plant wide, both fists drop to hips.
- F8: BOTH ARMS RISE — vertical fist drive, both fists rocketing upward.
- F9: peak — both arms fully extended overhead, body leaning slightly into the upward motion.
- F10: **bandana trail — bandana drawn as a free yellow streak 8 px above her head, separated from the wrist as if it has flown upward off her arm**.
- F11: hold — pose for emphasis. **Brief smile (1 px corner lift)**.
- F12: recovery — arms come down, body returns to stance.

### `throw` (5 frames, 11 fps)
- F1: grab — both arms forward, hands on enemy's collar.
- F2: lift — body straightens, enemy hoisted off-ground.
- F3: rotation — body twists, enemy pivots overhead.
- F4: release — enemy released downward, Rio's body in a forward lean.
- F5: recovery.

### `counter` — CHECK HOOK (6 frames, 12 fps)
**Visual signature:** the boxer's textbook counter — Rio steps off-line and pivots her body 90° SIDEWAYS to the camera while throwing a tight lead hook at head height. **F4 silhouette: Rio is fully PROFILE-FACING to the camera (the only attack pose where she's sideways), lead arm hooked inward at head height with the elbow bent 90°, rear hand still up at chin for guard, weight planted on the pivot foot. Yellow bandana traces a TIGHT inward arc across her own face line** (different from atk3's wide arc — counter's hook is short and compact). **The reserved SMILE appears for one frame** (F5) — the satisfaction of a clean counter. Must NOT show Rio facing forward; the off-line pivot IS the move's identity.
- F1: read — Rio's weight shifts onto the lead (left) foot, body starts pivoting off-line. Lead shoulder dips slightly. Bandana still at the wrist.
- F2: pivot — front foot rotates 60° to the side, body following the pivot, rear arm tucking up at chin. Lead fist starts coming around in a tight horizontal arc.
- F3: drive — body now 75° pivoted (almost full profile to camera), lead fist arcing inward at head height with the elbow bent 90°. Bandana streaks across her face line in a tight 8-px yellow arc.
- F4: **PEAK — body FULLY SIDEWAYS to camera (90° pivot, profile silhouette), lead fist at peak hook position with elbow bent 90° at head height, rear hand at chin for guard. Bandana fully across the face line as a tight yellow arc. 1-px white impact spark at the fist**. Eyes locked.
- F5: **hold + brief SMILE — pose held one extra frame for the counter's weight, mouth corner lifts 1 px**. The clean-counter smile.
- F6: recovery — body un-pivots back to forward stance, lead fist retracts, hands resume guard. Bandana settles back at the wrist.

### `hurt` (3 frames, 12 fps)
- F1: impact — body folds, head rocks back 5°.
- F2: recoil — torso bent slightly, arms momentarily out.
- F3: recovery — body straightening back to stance.

### `dodge` — backward roll (5 frames, 14 fps)
- F1: drop — body crouches sharply.
- F2: tuck — body curls forward, head down.
- F3: roll — body fully tucked, mid-roll silhouette (compact ball).
- F4: extend — body uncoiling out of the roll.
- F5: stand — back to stance.
- **Bandana stays visible** even during the tucked frames — a small yellow strip on the curled-up side.

## DO NOT include for Rio

- Glowing energy auras around hands or body
- Elemental effects (fire, lightning, ice) — she's a boxer, not a magic user
- Cape/scarf/long flowing items — only the bandana
- Modern combat boots (military style) — hers are sport boxing boots
- Long hair flowing — afro is contained, not flowing
- Open jacket flapping wildly — it's cropped and tight

## Visual VFX summary

Rio's identity in motion is the **yellow bandana ribbon**. Every attack should leave a visible bandana trail in a different shape so each move has its own colour-streak signature. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` JAB — body vertical, FRONT fist forward; bandana 12-px horizontal ribbon behind the fist
- `atk2` CROSS — body rotated 45°, REAR fist forward; bandana whips OPPOSITE the cross fist (yellow X across body)
- `atk3` ROUNDHOUSE — grounded, leg horizontal at chest height (shin parallel to floor); bandana arcs with the kicking foot
- `atk4` SPINNING BACK KICK — AIRBORNE mid-spin, heel VERTICAL above the head; bandana traces complete 360° circle
- `heavy` UPPERCUT — ONE front fist rising from the hip to overhead; bandana streaks STRAIGHT UP as vertical yellow column
- `jump_atk` FLYING KNEE — AIRBORNE, lead knee forward at chest height (the only knee strike)
- `back_atk` REAR ELBOW — body twisted BACKWARD 60°, elbow behind body (the only rear-facing attack)
- `special` SUNSET SPIN — yellow HALO at hip level during sweep + free-floating yellow streak above head at the peak double-uppercut
- `throw` OVERHEAD SPIN — both hands grip, enemy pivots overhead (the only grappling pose)
- `counter` CHECK HOOK — body fully PROFILE-SIDEWAYS to camera, lead fist hooked tight at head height, bandana tight inward arc across face line, reserved SMILE on F5

**Hurt / flinch:** F1 body folds forward at the waist, head rocks back 5°. F2 a 2-px white impact spark at the contact point + bandana lifts away from the wrist by 4 px (whipped by the hit). F3 body returns toward stance, bandana settles.

**Dead:** Falls to one knee then forward. Bandana slides 4 px from the wrist on the final frame, visible against the dark ground.

## Sheet specs (same for all three characters)

### Color discipline
- Each body part stays within its 3-color palette (mid, shadow, highlight). Don't blend pixels between palettes.
- Identity-item colors are reserved — bandana yellow, wedding-band silver, cigarette cream are unique to that character. Don't reuse them on other parts.

### Outline
- 1-pixel hard outline at the silhouette boundary, in the deepest shadow color of that body part (not pure black).
- No anti-aliasing along the outline.

### Lighting direction
- Light comes from the upper-front-right of the character (the camera-side, slightly above).
- Highlights along the upper-front edges, shadows along the lower-back edges.

### Reference quality target
- Streets of Rage 4 character pixel quality (not the SoR4 final art — they're 2D-vector — but the same readability and silhouette discipline).
- Fight'N Rage character density and hand-poses.
- Castle Crashers tier of expressive poses (a bit more cartoon-readable than realistic).

### Frame counts (Rio total: 80)

| Slot | Frames |
|---|---:|
| idle | 4 |
| walk | 6 |
| run | 6 |
| jump | 3 |
| atk1 | 4 |
| atk2 | 5 |
| atk3 | 6 |
| heavy | 7 |
| jump_atk | 4 |
| back_atk | 4 |
| special | 12 |
| throw | 5 |
| counter | 6 |
| hurt | 3 |
| dodge | 5 |

### Sheet layout
- Uniform grid, **8 columns × 10 rows = 80 cells**.
- Each cell: **64 wide × 96 tall**.
- Background: solid magenta `#ff00ff` for keying, OR transparent PNG.
- Anchor each frame's character at **bottom-center** of the cell.

### Final integration step

When this sheet lands:
1. Save to project root as `rio.png`.
2. Open `sprite_slicer.html`, load the PNG, click through to label all 15 anim slots.
3. Export `rio_atlas.json` next to the PNG.
4. `python3 pipeline.py validate-atlas rio_atlas.json`.
5. Reload `the_block.html`. The atlas loader picks it up automatically — Rio switches from procedural to sprite rendering. Any anim slot that's missing falls back to procedural for that animation only, so partial atlases are fine.

