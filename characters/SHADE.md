# SHADE

The unsettling ones. Kane hires them from somewhere none of his other crews know about — they show up to jobs in unmarked black vans, do the work, leave. Rumored to be ex-special-ops contractors. The other crews don't ask questions. The Block's neighbors say they "appear out of nowhere."

In the engine, Shade vanishes briefly and reappears behind the protagonist. Story-wise: it's just very fast movement through alleys and shadows. *Mechanically* it teleports.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **12 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — SHADOW CHOP (4 frames) — **OPEN KNIFE-HAND drives forward at neck height**, cloak hem fans 180° behind in a comet-tail arc (the only EMPTY-HAND attack)
> 4. `atk2` — MATERIALISING BACKSTAB (4 frames) — **BLADE EMERGES FIRST from a purple smoke wisp BEFORE the body solidifies**, then forward thrust (the only single-blade attack)
> 5. `atk3` — CLOAK-CYCLONE HOOK KICK (5 frames) — **kicking leg HORIZONTAL at HEAD height with the HEEL leading**, cloak fanned in a complete 360° purple halo around the body (the only leg attack)
> 6. `atk4` — CLOAK-WHIP LOW SWEEP (5 frames) — **body CROUCHED low (lowest pose Shade takes), cloak hem WHIPS OUT in a HORIZONTAL ARC at ANKLE HEIGHT** to trip the target (the only ankle-height attack + only crouched pose)
> 7. `atk5` — TWIN-BLADE FAN (5 frames) — **TWO blades materialise simultaneously from purple smoke on EACH arm**, both arms explode outward in opposite directions in a horizontal slash (the only two-blade attack + only attack that hits both sides simultaneously)
> 8. `atk6` — PHANTOM-CLONE BACKSTAB (6 frames) — **body SPLITS into THREE purple after-images** that converge into one for a final stab; F2–F3 show three Shade silhouettes side-by-side, F4 they merge, F5 real Shade strikes (the only multi-clone attack + the only attack where multiple Shade silhouettes appear in one frame)
> 9. `vanish` (5 frames)
> 10. `reappear` (3 frames)
> 11. `hurt` (3 frames)
> 12. `dead` (4 frames)
>
> **Total: 54 frames in 12 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Shade's failure mode is **every attack reading as "cloaked figure with arm extended."** Six attacks now each occupy a different silhouette quadrant AND each carries a unique signature beat (empty open hand, single-blade-from-smoke, head-height heel, ankle-height cloak whip, dual-blade fan, three-clone convergence). If two attacks share a silhouette OR a signature beat, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique signature beat |
> |---|---|---|---|---|
> | `atk1` shadow chop | Vertical, body squared, knees soft | OPEN HAND (knife-hand, fingers extended, NO blade) | Horizontal forward at NECK height | EMPTY HAND with fingers extended (only attack with an empty open hand) + cloak fans 180° behind in a comet-tail arc + edge-of-hand leading at neck height |
> | `atk2` materialising backstab | Vertical, body PARTIALLY TRANSLUCENT on F1 then solidifies | ONE blade in clenched fist (forward grip) | Horizontal forward at chest height | BLADE EMERGES FIRST on F1 (blade + eye-glow only, body <40% alpha) + free arm flung BACK for balance + ONE blade at the front hand only |
> | `atk3` cloak-cyclone kick | Rotated mid-spin, body torqued through 360° | Kicking LEG, HEEL leading | Horizontal at HEAD height (whip hook) | Only LEG attack + heel at HEAD height + cloak fanned in a complete 360° purple halo around the body (vortex) |
> | `atk4` cloak-whip sweep | CROUCHED LOW (lowest pose Shade takes), supporting hand may brace floor | CLOAK HEM (used as a whip) | Horizontal arc at ANKLE height | Body lower than any other Shade pose + cloak hem extended HORIZONTALLY at ankle height in a 140° arc with purple smoke trailing behind it (the only attack where the cloak ITSELF is the weapon) |
> | `atk5` twin-blade fan | Vertical, arms exploding outward from chest centerline | TWO blades, one per fist | Horizontal slashes in OPPOSITE directions simultaneously | TWO blades MATERIALISING simultaneously from purple smoke at both wrists on F2 + both arms fully extended OUTWARD in opposite directions on F3 (forming a "+" or "T" silhouette) + hits both sides |
> | `atk6` phantom-clone | Vertical, splits across the X-axis | Real body's blade (front hand) | Convergence then forward thrust | THREE Shade silhouettes visible simultaneously on F2–F3 (left clone @40% alpha, center clone @70% alpha, right clone @40% alpha) + F4 they MERGE into one at center + F5 the real strike — only attack with multiple Shade silhouettes in one frame |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = OPEN HAND, fingers extended, NO blade, hand at NECK height; F1 already solid. atk2 = CLENCHED FIST holding ONE VISIBLE BLADE at CHEST height; F1 starts with the BLADE VISIBLE and the BODY <40% ALPHA (purple smoke wisp around). If atk2's F1 shows a solid body holding a knife, the materialising-blade tell isn't reading — redraw.
> - **atk1 cloak vs atk3 cloak vs atk4 cloak:** atk1 cloak fans 180° BEHIND only (comet tail rearward). atk3 cloak fans 360° around the body (full halo). atk4 cloak extends HORIZONTALLY at ANKLE height in a 140° arc (whip). Three different cloak shapes — if any two look alike, redraw.
> - **atk3 vs atk4:** atk3 has the LEG horizontal at HEAD height with the body rotating through a spin (cloak halo, body upright). atk4 has the CLOAK hem horizontal at ANKLE height with the BODY CROUCHED LOW (lowest Shade pose). Opposite heights, opposite body positions, opposite weapons (leg vs cloak).
> - **atk2 vs atk5 vs atk6:** all three involve blades. atk2 = ONE blade, front hand, single forward thrust. atk5 = TWO blades, both hands, outward slash to BOTH sides. atk6 = ONE blade but THREE bodies visible during the convergence frames. If atk5 shows only one blade, redraw — the dual-blade materialisation IS the move. If atk6 doesn't show three Shade silhouettes during F2–F3, the clone gimmick isn't reading — redraw.
> - **atk6 three-clone rule:** the three Shade silhouettes on F2–F3 must be clearly distinct — left clone at ~40% alpha, center clone at ~70% alpha (the brightest because it's about to be the real one), right clone at ~40% alpha. All three identical pose, just horizontally offset 14 px apart. The two outer clones fade as F4 progresses.
> - **Eye-glow rule:** the two eye-dots are the ONLY saturated colour on Shade in every frame including vanish/reappear/hurt/dead. If any frame shows the face below the eyes, redraw — the mask stays up.

> ## ⚠️ SHEET CONSISTENCY RULES — read first
>
> **Cells must contain only the character.** No anim labels, no row headers, no descriptive text overlays, no frame numbers.
>
> Shade is **the same hooded figure** in every cell — same cloak, same hood draping, same eye-glow color, same purple wisp at the hem. Only the pose changes.

## Physical

- **Age range:** Indeterminate. Body looks 25–35 but the eyes look older.
- **Height/build:** 5'9" – 5'11", lean-athletic. Whip-quick. Gender-ambiguous on purpose — Shades are *types*, not individuals.
- **Body language:** Composed. Doesn't bounce. Stands flat, arms loose at sides, weight perfectly centered. When about to vanish: a single inhale, eyes close briefly.
- **Face:** Almost entirely hidden by a smooth black hood + a featureless dark grey mask covering nose and mouth. Only the eyes are visible — pale grey-blue (`#a8c8d0`), unblinking.

## Hair

- Hidden under the hood entirely. Don't draw any.

## Costume (head to feet)

1. **Hooded utility cloak** — matte black (`#16161a`), draped, hood always up. Hangs to the lower thigh. **The cloak's hem trails as motion lines** during dash and vanish frames.
2. **Skin-tight black bodysuit** under, visible at neck, arms, legs.
3. **Mask** — featureless dark grey (`#2a2a2f`), nose-and-mouth coverage, no logo, no decoration.
4. **Soft-soled tactical shoes** — black, no laces visible.
5. **Black leather gloves** — fingertips removed, knuckles wrapped with thin tape.

## Identity item — REQUIRED IN EVERY FRAME

**A faint dark-purple glow at the eyes (`#3a2050` core, `#6a3080` edge), 1–2 px high, only visible because everything else is so matte black.** During vanish frames, the glow grows brighter and persists in the air for 2–3 frames after the body fades — like an after-image of the eyes. *This is the Shade's tell.*

Combined with: **wisps of black-purple smoke** trailing from the cloak hem during all movement frames.

## Palette (hex)

```
cloak (mid)        #16161a
cloak (shadow)     #08080a
cloak (highlight)  #2a2a2f
bodysuit           #1a1a1f
mask               #2a2a2f
glove              #16100a
boot               #0a0a10
eye glow core      #6a3080
eye glow edge      #3a2050
smoke trail        #3a2a4a
smoke trail edge   #1a0e22
```

## Personality / fighting style

- **Silent.** Never talks.
- **Vanishes every 2–3 seconds.** During vanish: cloak shimmers, body fades over ~0.4s. Reappears behind the protagonist (other side of screen if center, or opposite side from where Shade was).
- **Backstab on reappear.** 0.2s after reappearing, automatic forward strike — fast 3-frame startup. The protagonist learns to turn around the *moment* Shade disappears.
- **Six signature moves — three hands, two blades, one cloak-as-weapon. Cycles through them based on range and HP threshold; the materialising backstab still auto-fires after reappear.**
  - **`strike` — Shadow chop.** Open-palm knife-hand at neck height, cloak fans behind in a comet-tail arc. The only empty-hand attack. 13 dmg.
  - **`backstab` — Materialising blade.** F1: blade emerges first from purple smoke wisp, body at <40% alpha. F2: body solidifies behind the blade. F3: forward thrust. The reappear auto-attack. 18 dmg + 80 knockback.
  - **`cyclone` — Cloak-cyclone hook kick.** Full-body 360° spinning hook kick — kicking leg horizontal at HEAD height with HEEL leading, cloak forming a complete 360° purple halo. Only leg attack. 15 dmg + 110 knockback.
  - **`sweep` — Cloak-whip low sweep.** **Visual signature: body CROUCHES LOWER than any other Shade pose, supporting hand braces the floor for stability, and the CLOAK HEM ITSELF whips out in a horizontal arc at ANKLE HEIGHT with a purple-smoke trail behind the whip.** The cloak is the weapon — not a hand, not a leg. Trips the player. 12 dmg + 80 knockback.
  - **`twin_blade` — Twin-blade fan.** **Visual signature: F2 both fists clench and TWO blades materialise simultaneously from purple smoke at both wrists (mirror of the backstab tell, but doubled). F3 both arms EXPLODE OUTWARD in opposite directions — one blade left, one blade right — body forming a perfect "T" silhouette.** Hits both sides at once. The only dual-blade attack and the only attack that hits both flanks simultaneously. 14 dmg + 100 knockback. Multi-hit (1 per side).
  - **`phantom` — Phantom-clone backstab.** **Visual signature: F2–F3 Shade SPLITS into THREE side-by-side silhouettes** (left + center + right, each 14 px apart). The center clone is brightest (70% alpha), the two outer clones are 40% alpha (the deception). F4 the three silhouettes converge into one. F5 the real Shade — at the CENTER position — drives the blade forward in a thrust. Player can't read which clone is real until the convergence resolves. 17 dmg + 120 knockback. The only multi-clone attack.
- **No ranged attacks.** Pure melee + teleport + clone gimmickry.
- **Eye-glow color is the only saturation** in the sprite — pick one (cyan `#5acfff`, ice blue `#8accff`, or pale violet `#cfaaff`) and use it on every frame, every animation, every time. The two eye-dots are the **only thing that should be visible** during the vanish frames.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Subtle. Hood breathes (rises 1 px on F2). **Eye-glow steady.** Cloak hem sways 1 px. Purple wisp curls from the hem on F3. |
| `walk`     | 6 | **Smooth predator glide that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT foot fwd under the hem + RIGHT shoulder rotates fwd 1 px (opposite-side, tight). F2 = passing position. F3 = RIGHT foot fwd + LEFT shoulder rotates fwd 1 px. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Arms hang loose AT THE SIDES inside the cloak** — they don't visibly swing wide (the cloak masks them), but the shoulders rotate slightly each step so the body still reads as walking, not hovering still. Arms NEVER extend forward past the body (would read as the shadow chop or backstab wind-up). Feet barely visible under the cloak hem — cloak trails 2 px behind the trailing leg. **Small purple smoke wisps from the hem on F1, F3, F5** (the strike frames). No planted/stomp pose on F6 — the cycle blends straight back into F1. |
| `atk1`     | 4 | **Shadow chop.** F1 = front hand cocks back across the chest, cloak gathers behind. F2 = forward drive (chopping hand starts extending, cloak begins fanning). F3 = **peak — chopping hand fully extended forward, cloak hem fanned 180° behind in a comet-tail arc**. F4 = retract, cloak resettles. |
| `atk2`     | 4 | **Materialising backstab.** F1 = **blade visible first** emerging from a purple smoke wisp, body still partially translucent (<40% alpha). F2 = body solidifies fully, blade leading. F3 = forward thrust (blade 18 px past body, free arm flung back for balance). F4 = retract. |
| `atk3`     | 5 | **Cloak-cyclone hook kick.** F1 = body coils, supporting foot pivots, kicking leg starts rising sideways. F2 = body starts rotating, cloak beginning to fan. F3 = **peak — body rotated mid-spin, kicking leg horizontal at head height with HEEL leading, free arm extended for balance, cloak fanned in a FULL 360° purple halo around the body (motion blur)**. F4 = leg follows through, body continuing rotation. F5 = recovery, cloak resettles around body. |
| `atk4`     | 5 | **Cloak-whip low sweep.** F1 = body drops into a crouch, supporting hand reaches toward floor. F2 = body LOW (lowest pose Shade ever takes), supporting hand braced on the floor, cloak gathering on one side. F3 = **peak — body crouched LOW with supporting hand on floor, CLOAK HEM extended HORIZONTALLY at ANKLE HEIGHT in a 140° arc, purple-smoke trail behind the whipping hem (the cloak ITSELF is the weapon)**. F4 = cloak past the sweep line, body still crouched. F5 = body rises back to stance, cloak resettles. |
| `atk5`     | 5 | **Twin-blade fan.** F1 = body squared, both arms cross in front of the chest, fists clenched (the load — arms ready to explode outward). F2 = **TWO blades MATERIALISE SIMULTANEOUSLY at both wrists from purple smoke wisps (mirror of the backstab tell, but doubled — both blades visible at once)**. F3 = **peak — both arms FULLY EXPLODED OUTWARD in opposite directions, body forming a "T" silhouette, left blade pointing left and right blade pointing right, each ~16 px past the body, purple smoke trailing behind both blades**. F4 = arms hold extension for 1 frame (the hit window for both sides). F5 = arms retract toward body, blades dissipating back into purple smoke. |
| `atk6`     | 6 | **Phantom-clone backstab.** F1 = real Shade in center position, cloak gathering, eye-glow pulses brighter. F2 = **body SPLITS — THREE side-by-side silhouettes appear: left clone @40% alpha (offset -14 px), center clone @70% alpha, right clone @40% alpha (offset +14 px); all identical pose, blade visible at each one's front hand**. F3 = three silhouettes hold, all three blades raised together (the deception window — player can't tell which is real). F4 = **CONVERGENCE — the left and right clones FADE to 0% alpha sliding toward center, the center silhouette brightens to 100% alpha**. F5 = real Shade (at center) drives the blade forward in a thrust, free arm flung back. F6 = retract, recovery. |
| `vanish`   | 5 | F1 = inhale, cloak puffs outward. F2 = body fades to 60% alpha, hem dissolving into smoke. F3 = body 30% alpha, only the head/cloak outline + eye-glow legible. F4 = body gone, just eye-glow + thick purple smoke. F5 = **eye-glow alone, no body** — the iconic vanish frame. |
| `reappear` | 3 | F1 = eye-glow + smoke only. F2 = body reforms at 50% alpha behind the smoke. F3 = full opacity, smoke dissipating. |
| `hurt`     | 3 | Body folds. **Hood briefly drops back 4 px on F2**, exposing more of the upper mask (but never the face below the eyes). |
| `dead`     | 4 | Body crumples. **Cloak pools out around the body in a wide circle.** Eye-glow fades — bright on F1, dim on F2, gone by F3. Purple smoke dissipates upward over the death frames. |

## DO NOT include

- **Any text inside cells** — no anim labels, row headers, or frame numbers.
- **Cell separator lines or borders.**
- **Different shade designs across frames** — same cloak silhouette, same eye-glow placement, same wisp colour in every cell.
- Visible scifi / glowing energy weapons — Shade is *grounded*. The only glow is the eyes.
- Capes / dramatic flowing robes — the cloak is fitted utility, not a costume.
- Bright colors anywhere — black, grey, dark purple ONLY.
- Visible face below the eyes.
- Multiple shades / clones in one frame — one body at a time, even during vanish.

## Visual VFX summary

Shade's identity is the **purple cloak wisps + eye-glow (the only saturated colour) + smoke from the cloak hem + the materialising-from-smoke trick**. **Every attack occupies a distinct silhouette quadrant AND a unique signature beat** (see the SILHOUETTE DIFFERENTIATION table near the top).

- `atk1` SHADOW CHOP — OPEN knife-hand (fingers extended, NO blade, edge of hand leading) drives forward at neck height + cloak hem fans 180° BEHIND in a comet-tail arc (only empty-hand attack)
- `atk2` MATERIALISING BACKSTAB — ONE blade in fist EMERGES FIRST from a purple smoke wisp on F1 before the body solidifies (body <40% alpha) + forward thrust at chest height with free arm flung back (only single-blade attack)
- `atk3` CLOAK-CYCLONE HOOK KICK — body rotated mid-spin, kicking LEG horizontal at HEAD height with HEEL leading + cloak fanned in a complete 360° purple halo around the body (only leg attack + only full-circle cloak halo)
- `atk4` CLOAK-WHIP LOW SWEEP — body CROUCHED LOW with supporting hand braced on floor + CLOAK HEM ITSELF whips horizontally at ANKLE HEIGHT in a 140° arc with purple smoke trail (only attack where the cloak is the weapon + lowest body pose + only ankle-height attack)
- `atk5` TWIN-BLADE FAN — TWO blades MATERIALISE simultaneously from purple smoke at BOTH wrists + both arms EXPLODE OUTWARD in opposite directions forming a "T" silhouette + hits both sides (only dual-blade attack + only attack hitting both flanks at once)
- `atk6` PHANTOM-CLONE BACKSTAB — body SPLITS into THREE side-by-side silhouettes on F2–F3 (left @40% / center @70% / right @40% alpha) + clones CONVERGE on F4 + real Shade strikes from center on F5 (only multi-clone attack + only attack with multiple Shade silhouettes in one frame)
- `vanish` — body fades over 5 frames: solid → 60% alpha → 30% alpha → just hood/eyes → eye-glow alone with purple smoke
- `reappear` — reverse of vanish: smoke + eyes → 50% alpha body → full opacity

**Signature-beat dictionary (read from across the screen).** Each beat appears EXACTLY ONCE in Shade's whole sheet:
- Open empty hand (knife-hand) — atk1 only
- ONE blade materialising at the front hand — atk2 only
- Leg horizontal at HEAD height + 360° cloak halo — atk3 only
- Body crouched LOW + supporting hand on floor + cloak as ankle-height whip — atk4 only
- TWO blades materialising at both wrists + "T" silhouette — atk5 only
- THREE Shade silhouettes visible side-by-side in one frame — atk6 only

**Hurt / flinch:** F1 body folds. F2 hood briefly drops back 4 px exposing more of the upper mask (BUT NEVER the face below the eyes — that's the rule). 1-px white impact spark.

**Dead:** Body crumples. Cloak pools around the body in a wide circle. Eye-glow fades — bright on F1, dim on F2, gone by F3. Purple smoke dissipates upward over the death frames.

## Sheet specs

- 7 columns × 5 rows = 35 cells (~33 frames used)
- Cell size: **48 × 72**
- Magenta `#ff00ff` background — Shade should look almost invisible against magenta because of how dark the palette is. That's intentional; the eye-glow IS the silhouette.
- Bottom-center anchor
