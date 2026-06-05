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
- **No ranged attacks.** Pure melee + teleport.

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Subtle. Hood breathes. Eyes glow steady. |
| `walk`     | 6 | Smooth glide. Cloak trails. Smoke wisps from hem on each step. |
| `atk1`     | 4 | Strike: front arm extends in a straight chop. Fast (16 fps). |
| `atk2`     | 4 | Backstab — same beats as `atk1` but cloak still trailing reappear smoke for 2 frames. |
| `vanish`   | 5 | F1 = inhale, F2–F3 = body fades to outline, F4–F5 = only the eye-glow + smoke remain. |
| `reappear` | 3 | F1 = smoke + eye-glow only, F2 = body reforms at low alpha, F3 = full opacity. |
| `hurt`     | 3 | Body folds. Hood briefly drops back, exposing more of the mask. |
| `dead`     | 4 | Body crumples. Cloak pools. Eye-glow fades over the death frames. |

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
