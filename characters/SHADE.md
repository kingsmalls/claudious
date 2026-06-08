# SHADE

The unsettling ones. Kane hires them from somewhere none of his other crews know about — they show up to jobs in unmarked black vans, do the work, leave. Rumored to be ex-special-ops contractors. The other crews don't ask questions. The Block's neighbors say they "appear out of nowhere."

In the engine, Shade vanishes briefly and reappears behind the protagonist. Story-wise: it's just very fast movement through alleys and shadows. *Mechanically* it teleports.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **9 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — SHADOW CHOP (4 frames) — **OPEN KNIFE-HAND drives forward at neck height**, cloak hem fans 180° behind in a comet-tail arc (the only EMPTY-HAND attack)
> 4. `atk2` — MATERIALISING BACKSTAB (4 frames) — **BLADE EMERGES FIRST from a purple smoke wisp BEFORE the body solidifies**, then forward thrust (the only attack with a visible weapon)
> 5. `atk3` — CLOAK-CYCLONE HOOK KICK (5 frames) — **kicking leg HORIZONTAL at HEAD height with the HEEL leading**, cloak fanned in a complete 360° purple halo around the body (the only leg attack)
> 6. `vanish` (5 frames)
> 7. `reappear` (3 frames)
> 8. `hurt` (3 frames)
> 9. `dead` (4 frames)
>
> **Total: 38 frames in 9 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Shade's biggest sheet-generation failure is **chop / backstab blurring together** because both are forward arm extensions in a black cloak. Every attack must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` shadow chop | Vertical, body squared, knees soft | OPEN HAND (knife-hand, fingers extended, edge leading) — NO BLADE | Horizontal forward at neck height | EMPTY HAND with fingers extended (the only attack with an empty open hand) + cloak fans 180° behind in a comet-tail arc + edge-of-hand leading at neck height (chop, not stab) |
> | `atk2` backstab | Vertical, body PARTIALLY TRANSLUCENT on F1 then solidifies | BLADE in clenched fist (forward grip) | Horizontal forward at chest height | BLADE EMERGES FIRST from a purple smoke wisp before the body is fully solid (F1: blade + eye-glow only, no body) + free arm flung BACK for balance + blade visible at the fist (only attack with a weapon) |
> | `atk3` cloak-cyclone | Rotated mid-spin, body torqued through 360° | Kicking LEG, HEEL leading | Horizontal at HEAD height (whip hook) | Only LEG attack + heel at HEAD height (higher than the chop's neck-level hand) + cloak fanned in a complete 360° purple halo (the only attack with the cloak as a full circle) |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = OPEN HAND, fingers extended, NO blade, hand at neck height; F1 already solid. atk2 = CLENCHED FIST holding a VISIBLE BLADE at chest height; F1 starts WITH THE BLADE VISIBLE and the BODY STILL TRANSLUCENT (purple smoke wisp around). If both attacks show a solid body throwing a forward strike with similar arm angles, redraw — atk2's identity is the blade appearing BEFORE he does.
> - **atk1 cloak vs atk3 cloak:** atk1's cloak fans 180° BEHIND only (comet tail rearward). atk3's cloak fans a full 360° CIRCLE around the body (vortex halo). If atk1 shows a full halo it's drawn as atk3 — redraw with the cloak swept only to the rear.
> - **atk3 vs jump_atk (other characters):** Shade does NOT have an airborne knee attack. atk3 stays GROUNDED on the supporting foot — only the kicking leg leaves the ground. If F3 shows both feet airborne, redraw with the pivot foot planted.
> - **Eye-glow rule:** the two eye-dots are the ONLY saturated colour on Shade in every frame including vanish/reappear/hurt/dead. If any frame shows the face below the eyes, redraw — the mask stays up.
> - **Backstab-before-body rule:** atk2 F1 MUST show the blade and eye-glow only, with the body at <40% alpha. If F1 shows a fully solid body holding a knife, the materialising-blade tell isn't reading — redraw.

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
- **Signature moves — strike + backstab + spinning kick.**
  - **`strike` — Shadow chop.** Front hand drives forward as an open-palm knife-hand chop (fingers extended, edge of hand leading), the cloak **swirls wide behind** in a half-circle from the motion. **Visual signature: F3 shows the chopping hand fully extended forward while the cloak hem fans outward to the rear in a 180° arc — like a comet tail**. 13 dmg.
  - **`backstab` — Materialising blade.** The strike that comes RIGHT after the reappear. **Visual signature: F1 shows only the eye-glow + cloak silhouette with the BLADE EMERGING FIRST from a wisp of purple smoke** (the blade is visible before the body), F2 the body solidifies behind the blade, F3 the forward thrust. 18 dmg + 80 knockback.
  - **`spin_kick` — Cloak-cyclone hook kick.** Full-body 360° spinning hook kick. **Visual signature: F3 silhouette has the body rotated mid-spin, kicking leg horizontal at head height with the HEEL leading (whip-style hook kick), free arm extended out for balance, AND the cloak fanned out in a complete circle around the body (a full 360° purple-cloth halo with motion blur)**. The cloak is the kick's signature — it spins with him forming a vortex. Eye-glow visible through the spinning cloak. 15 dmg + 110 knockback.
- **No ranged attacks.** Pure melee + teleport.
- **Eye-glow color is the only saturation** in the sprite — pick one (cyan `#5acfff`, ice blue `#8accff`, or pale violet `#cfaaff`) and use it on every frame, every animation, every time. The two eye-dots are the **only thing that should be visible** during the vanish frames.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Subtle. Hood breathes (rises 1 px on F2). **Eye-glow steady.** Cloak hem sways 1 px. Purple wisp curls from the hem on F3. |
| `walk`     | 6 | **Smooth predator glide that LOOPS SEAMLESSLY** (F6 blends back into F1). F1 = LEFT foot fwd under the hem + RIGHT shoulder rotates fwd 1 px (opposite-side, tight). F2 = passing position. F3 = RIGHT foot fwd + LEFT shoulder rotates fwd 1 px. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Arms hang loose AT THE SIDES inside the cloak** — they don't visibly swing wide (the cloak masks them), but the shoulders rotate slightly each step so the body still reads as walking, not hovering still. Arms NEVER extend forward past the body (would read as the shadow chop or backstab wind-up). Feet barely visible under the cloak hem — cloak trails 2 px behind the trailing leg. **Small purple smoke wisps from the hem on F1, F3, F5** (the strike frames). No planted/stomp pose on F6 — the cycle blends straight back into F1. |
| `atk1`     | 4 | **Shadow chop.** F1 = front hand cocks back across the chest, cloak gathers behind. F2 = forward drive (chopping hand starts extending, cloak begins fanning). F3 = **peak — chopping hand fully extended forward, cloak hem fanned 180° behind in a comet-tail arc**. F4 = retract, cloak resettles. |
| `atk2`     | 4 | **Materialising backstab.** F1 = **blade visible first** emerging from a purple smoke wisp, body still partially translucent. F2 = body solidifies fully, blade leading. F3 = forward thrust (blade 18 px past body, free arm flung back for balance). F4 = retract. |
| `atk3`     | 5 | **Cloak-cyclone hook kick.** F1 = body coils, supporting foot pivots, kicking leg starts rising sideways. F2 = body starts rotating, cloak beginning to fan. F3 = **peak — body rotated mid-spin, kicking leg horizontal at head height with HEEL leading, free arm extended for balance, cloak fanned in a FULL 360° purple halo around the body (motion blur)**. F4 = leg follows through, body continuing rotation. F5 = recovery, cloak resettles around body. |
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

Shade's identity is the **purple cloak wisps** + the eye-glow (the only saturated colour on him) + smoke from the cloak hem. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so the chop and the backstab never blur together.

- `atk1` SHADOW CHOP — OPEN knife-hand (fingers extended, NO blade, edge of hand leading) drives forward at neck height + cloak hem fans 180° BEHIND in a comet-tail arc (the only empty-hand attack)
- `atk2` MATERIALISING BACKSTAB — BLADE in fist EMERGES FIRST from a purple smoke wisp on F1 before the body solidifies + forward thrust at chest height with the free arm flung back (the only attack with a visible weapon + body partially translucent on F1)
- `atk3` CLOAK-CYCLONE HOOK KICK — body rotated mid-spin, kicking LEG horizontal at HEAD height with the HEEL leading + cloak fanned in a complete 360° purple halo around the body (the only leg attack + the only full-circle cloak halo)
- `vanish` — body fades over 5 frames: solid → 60% alpha → 30% alpha → just hood/eyes → eye-glow alone with purple smoke
- `reappear` — reverse of vanish: smoke + eyes → 50% alpha body → full opacity

**Hurt / flinch:** F1 body folds. F2 hood briefly drops back 4 px exposing more of the upper mask (BUT NEVER the face below the eyes — that's the rule). 1-px white impact spark.

**Dead:** Body crumples. Cloak pools around the body in a wide circle. Eye-glow fades — bright on F1, dim on F2, gone by F3. Purple smoke dissipates upward over the death frames.

## Sheet specs

- 7 columns × 5 rows = 35 cells (~33 frames used)
- Cell size: **48 × 72**
- Magenta `#ff00ff` background — Shade should look almost invisible against magenta because of how dark the palette is. That's intentional; the eye-glow IS the silhouette.
- Bottom-center anchor
