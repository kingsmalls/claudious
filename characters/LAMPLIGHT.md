# LAMPLIGHT

Kane's ranged threat. Old-school hired guns — the kind who learned the trade from someone who learned it in the 1970s. They don't want to brawl; they want to keep distance and put holes in things. Named "Lamplight" because they work the gaps between streetlights where the cameras don't cover.

Visually they read **immediately as noir**: long dark trench coat, fedora pulled low, scarf across the lower face. The silhouette is the threat — you see the hat from across the screen and you know a gun's coming out.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **9 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — PISTOL SHOT (5 frames) — **two-handed pistol HORIZONTAL FORWARD at chest height**, fedora tilts DOWN 1 px to sight, small orange muzzle flash (the bread-and-butter shot)
> 4. `atk2` — CHARGED SHOT (8 frames) — **same horizontal grip but GROWING BLUE GLOW at the muzzle (2→3→5→7 px)** across F1–F4, bigger 8-px white-orange muzzle flash on release, body ROCKS BACK with the coat flaring
> 5. `atk3` — PISTOL WHIP (6 frames) — **GUN-BUTT ARCS HORIZONTALLY at HEAD HEIGHT**, gun reversed so the grip leads, free hand braced at chest, no muzzle flash (the only no-shot attack — close-range cosh strike)
> 6. `atk4` — HIPFIRE FAN (7 frames) — **gun drops to HIP HEIGHT (the only attack where the gun is NOT at the chest)**, three rapid muzzle flashes left → center → right fanning across the lane, body squared and steady (no recoil rock)
> 7. `atk5` — COAT-FLARE KICK (5 frames) — **REAR LEG kicks forward at gut height, COAT FLARES OPEN BEHIND like a cape** revealing the burgundy lining `#4a1018` (the only frame the lining is visible), pistol arm crosses the body for balance (the only kick + the only lining reveal)
> 8. `hurt` (3 frames)
> 9. `dead` (4 frames)
>
> **Total: 48 frames in 9 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Lamplight's failure mode is **every attack reading as "guy aiming a pistol forward at chest height."** The new moveset breaks that with three non-shot attacks (whip, hipfire, coat-kick) each occupying a clearly different silhouette quadrant. Each attack must read as a different move from across the screen:
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` shot | Vertical, body squared, slight 5° forward lean | Pistol two-handed at CHEST height | Horizontal forward | Fedora tilts DOWN 1 px to sight + small 4-px ORANGE-YELLOW muzzle flash; coat sits straight (no flare); body steady (no recoil rock); ONE muzzle flash |
> | `atk2` charged | Vertical aim then ROCKED BACK 10° on release | Pistol two-handed at CHEST height | Horizontal forward | GROWING BLUE GLOW at the muzzle across F1–F4 (2 → 3 → 5 → 7 px) + scarf tints one shade cooler at peak charge + bigger 8-px WHITE-ORANGE flash + body rocks BACK with the coat flaring behind on recoil |
> | `atk3` whip | Body LUNGES forward 6 px on the swing | Pistol REVERSED, grip leading like a cosh | Horizontal arc at HEAD height | Gun is REVERSED in the hand (grip leading, barrel pointing back at his own wrist) + NO muzzle flash anywhere + body lunged forward — only no-shot attack |
> | `atk4` hipfire fan | Vertical, body squared, gun dropped LOW | Pistol ONE-HANDED at HIP HEIGHT | Three horizontal shots fanning left → center → right | Gun at HIP (well below chest — the only attack where the gun isn't at the chest) + THREE muzzle flashes in sequence + no aim (no fedora-tilt sight pose) |
> | `atk5` coat kick | Body pivots 30°, REAR LEG arcs forward | REAR boot at gut height | Horizontal forward at gut height | COAT FLARES OPEN BEHIND revealing BURGUNDY LINING (`#4a1018`) — the only frame the lining is ever visible + gun crosses the body for balance + only leg attack |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 has ONE small (4-px) orange flash and no body rock. atk2 has the GROWING BLUE GLOW pre-shot + ONE bigger (8-px) white-orange flash + body rocked back + coat flared. The pre-shot blue charge is the differentiator — if atk2's wind-up looks like atk1 with a blue tint instead of a visibly growing orb, redraw.
> - **atk1/atk2 vs atk4:** atk1 and atk2 have the gun at CHEST height in a two-handed grip. atk4 has the gun at HIP HEIGHT in a one-handed grip. If atk4's gun is at chest, redraw — the dropped-low gun IS atk4's identity.
> - **atk4 fan rule:** atk4 fires THREE shots across the active frames (F3, F5, F7 — staggered). Three distinct muzzle flashes must appear in sequence, each pointed slightly differently (left-of-center, center, right-of-center) so the spray is visible. If only one flash is drawn, the fan isn't reading.
> - **atk3 reversed grip:** atk3's pistol is REVERSED so the grip leads (Lamplight is holding it by the barrel like a cosh). The hand wraps around the BARREL with the GRIP pointing FORWARD. If the gun shows the barrel forward or shows a muzzle flash, redraw — atk3 is a melee strike with the gun, NOT a shot.
> - **atk5 lining reveal:** atk5 is the ONLY frame in the sheet that shows the coat's burgundy lining. If walk/idle/atk1–4 show the lining, redraw — the lining reveal is reserved for the kick's coat-flare moment.
> - **atk5 vs other attacks:** atk5 is the only LEG attack. If F3 doesn't show the rear boot extended forward at gut height with the coat flaring behind, the kick isn't reading.
> - **Scarf rule:** the white scarf is UP across the nose and mouth in EVERY frame including hurt and dead. If any frame shows the mouth/nose visible, redraw — the scarf is identity.

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

- **Holds 70–110 px range** from the protagonist. At long range fires shots and the charged tracer. At mid range can hipfire-fan to deny ground. **Close range now triggers a melee response (pistol whip or coat kick) instead of just retreating** — the noir gunslinger has a couple of dirty tricks for someone who closes the gap.
- **Five signature moves — three shots, two melees. The fedora + white scarf + pistol silhouette is the visual identity at rest; the moveset rotates by distance.**
  - **`shot` (regular) — Aimed pistol shot.** **Visual signature: F2 the fedora tilts DOWN 1 px** as he sights along the barrel (the aiming tell). F3 muzzle flash — a **4-px orange-yellow burst at the barrel tip**, visible past the scarf. Two-handed grip stays steady. 9 dmg. Default long-range.
  - **`charged` (every 4th long-range shot) — Heavy tracer.** **Visual signature: F1–F4 the barrel develops a GROWING BLUE GLOW** (2 px → 3 px → 5 px → 7 px) — a charging blue orb at the muzzle that tints the white scarf one shade cooler for one frame at peak charge. F5 release is a **bigger muzzle flash (8 px, white-orange core)** and the body rocks back. The coat flares behind him on the recoil. 36-frame telegraph. 18 dmg + orange tracer projectile.
  - **`hipfire` (mid range) — Three-shot fan.** **Visual signature: gun DROPS from the chest to HIP HEIGHT in a one-handed grip** (the only attack where the pistol is below the chest). Three rapid muzzle flashes across the active frames (F3 left, F5 center, F7 right) fanning the shots across the lane. Body squared, no aim-down. No fedora tilt. 6 dmg per shot × 3 = 18 dmg total. Sprays a horizontal band.
  - **`whip` (close range, when pinned) — Pistol-whip cosh.** **Visual signature: gun is REVERSED in the hand** (Lamplight grips the barrel; the metal frame's grip leads forward like a brass-knuckle club). Body lunges forward 6 px. Free hand braces at chest. **No muzzle flash anywhere — this is melee, not a shot**. 12 dmg, 140 knockback. The only no-shot attack.
  - **`coat_kick` (close range alternate) — Coat-flare kick.** **Visual signature: body pivots 30° on the lead foot, REAR LEG arcs forward at gut height, and the COAT FLARES OPEN BEHIND like a cape** revealing the deep burgundy lining `#4a1018` (the only frame in Lamplight's entire sheet where the lining is visible). Pistol arm crosses the body for balance. 11 dmg, 120 knockback. Cinematic noir-villain leg sweep — the only leg attack.
- **Calm.** Doesn't talk during combat. The face is unreadable.

## Animations — unchanged from previous spec

| Slot      | Frames | Notes |
|-----------|-------:|-------|
| `idle`    | 4 | Gun held two-handed at chest height. Eye-slit visible under fedora brim. Scarf tails sway 1 px on breath. Coat hangs straight (no flare). |
| `walk`    | 6 | **Composed gunslinger gait that LOOPS SEAMLESSLY** (F6 blends back into F1). Lamplight walks backwards while keeping the gun raised — mirror the cycle for forward travel. F1 = LEFT leg fwd + RIGHT arm-shoulder fwd swing (opposite-side). F2 = passing. F3 = RIGHT leg fwd + LEFT arm-shoulder fwd swing. F4 = passing. F5 = mirror of F1. F6 = passing → blends into F1. **Both arms keep the two-handed pistol grip at the chest — they don't swing wide, but the SHOULDERS rotate AT THE SIDES with each step (1–2 px sway)** so the body still reads as walking, not as a static aim pose. Arms NEVER extend forward past chest height (would read as taking a shot). Coat hem sways 2 px behind the trailing leg per step — never flares (flare is reserved for charged recoil). Scarf tails drift 1 px lateral per step. No planted/stomp pose on F6 — the cycle blends straight back. |
| `atk1`    | 5 | **Regular shot.** F1–F2 = raise + aim (fedora tilts down 1 px), F3 = trigger pull (4-px orange-yellow muzzle flash at the barrel, visible past the scarf), F4–F5 = recoil + recover. Two-handed grip stays steady — body does not rock back. |
| `atk2`    | 8 | **Charged shot.** F1–F4 = long aim with GROWING BLUE GLOW at the barrel (2 → 3 → 5 → 7 px; also tints the scarf one shade cooler on F4), F5 = bigger 8-px white-orange muzzle flash, F6–F8 = harder recoil — body rocks BACK 10°, COAT FLARES behind on F6 (the only flare across the whole sheet). |
| `atk3`    | 6 | **Pistol whip.** F1 = body coils, GUN ROTATES IN THE HAND so Lamplight grips the BARREL (the metal frame's grip now leads forward like a club). F2 = wind-up, free hand braces at chest. F3 = body LUNGES forward 6 px, GUN-BUTT ARCS HORIZONTALLY at HEAD HEIGHT (the only frame the pistol is at head height + the only frame the pistol is held by the barrel). F4 = peak impact, 1-px white impact spark at the gun-butt, scarf tails whip with the lunge. F5 = follow-through. F6 = recovery — gun rotates back to normal forward grip. NO muzzle flash anywhere in this anim. |
| `atk4`    | 7 | **Hipfire fan.** F1 = gun DROPS from chest to HIP HEIGHT in a ONE-HANDED grip (the only attack where the pistol leaves chest level — and the only one-handed grip). F2 = aim set, body squared, no fedora tilt. F3 = **first muzzle flash** angled LEFT-of-center (3-px orange burst). F4 = recoil ride. F5 = **second muzzle flash** angled CENTER (3-px orange burst). F6 = recoil ride. F7 = **third muzzle flash** angled RIGHT-of-center (3-px orange burst). Three distinct flashes must appear, gun rotating slightly across the fan. Body squared and steady through all 7 frames. |
| `atk5`    | 5 | **Coat-flare kick.** F1 = body pivots 30° on the lead foot, rear knee starts lifting, pistol arm crosses the body for balance (gun pointing down-and-away). F2 = rear leg chambering, knee at hip height. F3 = **peak — REAR BOOT extended forward at GUT HEIGHT (~22 px past the body), COAT FLARES OPEN BEHIND like a cape revealing the BURGUNDY LINING (`#4a1018`) — the only frame in the entire sheet where the lining is visible.** Pistol arm crossed at the chest, scarf tails whipping with the pivot. F4 = follow-through, leg past impact, coat starting to fall back. F5 = recovery — leg returns to stance, coat closes, lining no longer visible. |
| `hurt`    | 3 | Body twists from the hit. Gun arm drops one frame. Fedora and scarf stay in place. Coat does NOT flare (no lining reveal in hurt). |
| `dead`    | 4 | Falls. Fedora rolls off the head on F3 revealing the buzz cut underneath (no face — face is still scarf-covered). Gun lands on ground beside body. |

## DO NOT include

- **Visible face below the eyes** — scarf stays up on every frame, including hurt.
- Visible hair — fedora covers it.
- Modern tactical gear — vests, plate carriers, knee pads. Lamplight is noir, not military.
- Visible logos or badges of any kind. Lamplight is deniable.
- Two visible guns / dual-wield — single pistol only.
- A cigarette — that's Duke's identity item, not Lamplight's.
- A long flowing cape — the coat flares slightly on motion but isn't a cape.

## Visual VFX summary

Lamplight's identity is the **orange muzzle flash** + blue charged glow + fedora tilt to aim + scarf as the high-contrast white silhouette against the black coat. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so the regular shot and the charged shot never blur into one move.

- `atk1` PISTOL SHOT — fedora tilts DOWN 1 px on F2 (aiming tell) + small 4-px ORANGE-YELLOW muzzle flash at the barrel tip on F3 + body steady (no recoil rock, coat does not flare)
- `atk2` CHARGED SHOT — barrel develops a GROWING BLUE GLOW (2 → 3 → 5 → 7 px) across F1–F4 (the blue tints the white scarf one shade cooler at peak charge) + bigger 8-px WHITE-ORANGE muzzle flash on F5 + body rocks BACK 10° with the coat flaring behind on recoil
- `atk3` PISTOL WHIP — gun REVERSED in the hand (Lamplight grips the BARREL; the grip leads forward like a cosh) + body LUNGES forward 6 px + gun-butt arcs horizontally at HEAD HEIGHT + 1-px white impact spark at the gun-butt + NO muzzle flash (the only no-shot attack)
- `atk4` HIPFIRE FAN — gun DROPS from chest to HIP HEIGHT in a ONE-HANDED grip (the only attack with the pistol below chest level + the only one-handed grip) + THREE muzzle flashes across the active frames (F3 left, F5 center, F7 right) fanning the shots across the lane + body squared (no aim tilt, no recoil rock)
- `atk5` COAT-FLARE KICK — body pivots 30° on the lead foot + REAR LEG extended forward at gut height + COAT FLARES OPEN BEHIND revealing BURGUNDY LINING `#4a1018` (the only frame in the sheet where the lining is visible) + pistol arm crosses the body for balance + the only kick

**Hurt / flinch:** F1 body twists from the hit. F2 gun arm drops one frame (the only time the gun is not in firing position). Fedora and scarf STAY UP. 1-px white impact spark on the coat.

**Dead:** Falls. Fedora rolls off the head on F3 revealing the buzz cut underneath (still no face — scarf still up). Gun lands on the ground beside the body.

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
