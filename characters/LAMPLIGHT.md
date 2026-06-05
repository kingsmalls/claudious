# LAMPLIGHT

Kane's ranged threat. Old-school hired guns — the kind who learned the trade from someone who learned it in the 1970s. They don't want to brawl; they want to keep distance and put holes in things. Named "Lamplight" because they work the gaps between streetlights where the cameras don't cover.

Visually they read **immediately as noir**: long dark trench coat, fedora pulled low, scarf across the lower face. The silhouette is the threat — you see the hat from across the screen and you know a gun's coming out.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **6 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — pistol shot (5 frames)
> 4. `atk2` — charged shot (8 frames)
> 5. `hurt` (3 frames)
> 6. `dead` (4 frames)
>
> **Total: 30 frames in 6 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.

## Physical

- **Age range:** 35–50 — old enough to have done this for a long time.
- **Height/build:** 5'10"–6'1", lean but not athletic. Steady hands. Carries weight at the shoulders from years of holding the gun raised.
- **Body language:** Composed. Walks slowly, hands in trench coat pockets until they need to draw. When the gun comes out it's a fluid two-handed grip held at chest level. Gender ambiguous — the trench coat and fedora hide most of the body.
- **Face:** Almost entirely hidden. Only a strip showing the eyes (between the fedora brim above and the scarf below) — flat, bored. Skin colour visible in that narrow strip varies per spawn.

## Hair

- Whatever's there is hidden under the fedora. Don't draw any.

## Costume (head to feet) — noir gunman silhouette

1. **Black fedora** — wide-ish brim pulled low over the eyes. The brim casts a shadow across the upper face so only the eye-slit is brightly visible. The hat is the single most recognizable silhouette element. Slightly battered band of darker leather around the crown.
2. **Long dark trench coat** — charcoal-black (`#1a1a22` body, `#0a0a10` shadow, `#2a2a36` highlight). **Mid-calf length** — covers nearly the whole body. Collar popped UP, reaching the bottom of the scarf. Belt cinched at the waist with a steel buckle. The coat **flares behind during the dash-back animation** like a cape.
3. **Long white scarf** — `#dcd6c4` with `#9a9482` shadow, wrapped twice around the neck and pulled up over the nose and mouth. The ends hang loose from the neck — visible 14–18 px tail down the front of the coat.
4. **Black gloves** — fitted leather (`#16100a`), no fingers exposed.
5. **Dark tactical pants** under the coat — `#1a1a22`, only the lower legs (below the coat hem) visible.
6. **Heavy combat boots** — black (`#0a0a10`), laced full. Visible below the coat.
7. **The pistol** — held two-handed at chest level. Body `#3a3a40`, barrel `#4a4a50`. Raised to fire.

## Identity item — REQUIRED IN EVERY FRAME

The **silhouette combination** — fedora + popped collar + white scarf over face + long coat — is the identity. **All three accessories visible from any camera angle**:

1. **Fedora** with the wide brim casting an eye-shadow.
2. **White scarf** wrapped twice, ends visible hanging down the coat front. The white scarf against the black coat is the high-contrast tell.
3. **Pistol** always visible in idle/walk (two-handed at chest); raised to aim during attacks.
4. **A small orange-yellow muzzle flash dot** (`#ffd76a`) at the barrel during `atk1` active frame.

## Palette (hex)

```
fedora black       #0a0a10
fedora highlight   #1c1c22
fedora band dark   #050507
coat (mid)         #1a1a22
coat (shadow)      #0a0a10
coat (highlight)   #2a2a36
coat lining        #4a1018   (deep burgundy, visible only on flares)
belt steel         #5a5a5a
scarf white        #dcd6c4
scarf shadow       #9a9482
glove black        #16100a
pants              #1a1a22
boot               #0a0a10
boot sole          #050507
skin (visible eyes) #d4a888    (vary per spawn — keep narrow)
gun body           #3a3a40
gun barrel         #4a4a50
muzzle flash hi    #fff8c0
muzzle flash mid   #ffd76a
muzzle flash edge  #ff8a40
charged glow blue  #4a8ad0    (telegraph during charged shot wind-up)
```

## Personality / fighting style

- **Holds 70–110 px range** from the protagonist. Backs up if you close in.
- **Signature moves — shot + charged. The fedora + white scarf + pistol silhouette is the visual identity at rest; the muzzle flash is the identity in combat.**
  - **`shot` (regular) — Aimed pistol shot.** **Visual signature: F2 the fedora tilts DOWN 1 px** as he sights along the barrel (the aiming tell). F3 muzzle flash — a **4-px orange-yellow burst at the barrel tip**, visible past the scarf. Two-handed grip stays steady. 9 dmg.
  - **`charged` (every 4th attack) — Heavy tracer.** **Visual signature: F1–F4 the barrel develops a GROWING BLUE GLOW** (2 px → 3 px → 5 px → 7 px) — a charging blue orb at the muzzle that tints the white scarf one shade cooler for one frame at peak charge. F5 release is a **bigger muzzle flash (8 px, white-orange core)** and the body rocks back. The coat flares behind him on the recoil. 36-frame telegraph. 18 dmg + orange tracer projectile.
- **Never melees.** If pinned, dashes back to range first.
- **Calm.** Doesn't talk during combat.

## Animations — unchanged from previous spec

| Slot      | Frames | Notes |
|-----------|-------:|-------|
| `idle`    | 4 | Gun held two-handed at chest height. Eye-slit visible under fedora brim. Scarf tails sway 1 px on breath. |
| `walk`    | 6 | Backwards walk while keeping gun raised — for retreating. Mirror for forward walk if needed. Coat hem sways behind. |
| `atk1`    | 5 | Regular shot. F1–F2 = raise + aim (fedora tilts down 1 px), F3 = trigger pull (muzzle flash at barrel, visible past the scarf), F4–F5 = recoil + recover. |
| `atk2`    | 8 | Charged shot. F1–F4 = long aim with growing blue glow at barrel (also tints the scarf for one frame), F5 = bigger muzzle flash, F6–F8 = harder recoil — body rocks back, coat flares behind. |
| `hurt`    | 3 | Body twists from the hit. Gun arm drops one frame. Fedora and scarf stay in place. |
| `dead`    | 4 | Falls. Fedora rolls off the head on F3 revealing the buzz cut underneath (no face — face is still scarf-covered). Gun lands on ground beside body. |

## DO NOT include

- **Visible face below the eyes** — scarf stays up on every frame, including hurt.
- Visible hair — fedora covers it.
- Modern tactical gear — vests, plate carriers, knee pads. Lamplight is noir, not military.
- Visible logos or badges of any kind. Lamplight is deniable.
- Two visible guns / dual-wield — single pistol only.
- A cigarette — that's Duke's identity item, not Lamplight's.
- A long flowing cape — the coat flares slightly on motion but isn't a cape.

## Sheet specs

- 8 columns × 4 rows = 32 cells (~30 frames used)
- Cell size: **64 × 88** (taller than before to accommodate the fedora + the scarf tails)
- Magenta `#ff00ff` background or transparent PNG
- Bottom-center anchor

## Why the redesign

The previous version (balaclava + brown jacket + tactical pants) was reading as generic tactical-shooter henchman. The fedora + trench coat + white scarf gives Lamplight a **silhouette nobody else in the cast has**:
- Tank has the vest + bald head
- Slice is mesh + knife
- Chains has the chain wrap
- Shade has the cloak with eye-glow
- Lamplight now has the hat + scarf

When you see all eight enemy types in `STAGE_INTRO_LINES`, each should be readable at a glance from silhouette alone. The fedora hat shape is uniquely Lamplight's — no other enemy or boss has headwear like it.
