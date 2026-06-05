# SHADE

The unsettling ones. Kane hires them from somewhere none of his other crews know about — they show up to jobs in unmarked black vans, do the work, leave. Rumored to be ex-special-ops contractors. The other crews don't ask questions. The Block's neighbors say they "appear out of nowhere."

In the engine, Shade vanishes briefly and reappears behind the protagonist. Story-wise: it's just very fast movement through alleys and shadows. *Mechanically* it teleports.

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
| `walk`     | 6 | **Smooth glide** — feet barely visible under the cloak hem (almost reads as hovering). Cloak trails 2 px behind the body. **Smoke wisps from the hem on each step** (small purple curls). |
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

## Sheet specs

- 7 columns × 5 rows = 35 cells (~33 frames used)
- Cell size: **48 × 72**
- Magenta `#ff00ff` background — Shade should look almost invisible against magenta because of how dark the palette is. That's intentional; the eye-glow IS the silhouette.
- Bottom-center anchor
