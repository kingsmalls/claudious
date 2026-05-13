# LAMPLIGHT

Kane's ranged threat. Hired guns — most of them ex-private-security with a permit and a chip on their shoulder. They don't want to brawl; they want to keep distance and put holes in things. Named "Lamplight" because they always work the streetlight gaps where the cameras don't cover.

## Physical

- **Age range:** 28–40
- **Height/build:** 5'10" – 6'1", lean. Steady hands.
- **Body language:** Composed. Doesn't bounce; reads the room. Holds the gun raised in a two-handed grip.
- **Face:** Mostly hidden by a balaclava or bandana mask covering nose-down. Eyes are visible — flat, bored.

## Hair

- Buzz cut or shaved, mostly hidden by a beanie. Gender ambiguous on purpose.

## Costume (head to feet)

1. **Black balaclava** covering the lower face. Just the eyes visible.
2. **Leather jacket** — dark brown (`#2a1f15`), fitted. Two front pockets.
3. **Black tactical pants** — `#1a1a22`, slim cut.
4. **Combat boots** — `#0a0a10`, laced full.
5. **Pistol** — `#3a3a40` body with a visible muzzle. Held two-handed at chest level by default; raises to fire.

## Identity item — REQUIRED IN EVERY FRAME

**A small orange-yellow muzzle flash dot (`#ffd76a`) at the gun barrel during `atk1`'s active frame.** And in idle/walk frames, the pistol itself is the identity tell — always visible, always held. Lamplight is *defined* by carrying the gun.

## Palette (hex)

```
balaclava black    #1a1a1f
jacket (mid)       #2a1f15
jacket (shadow)    #16100a
pants              #1a1a22
boot               #0a0a10
skin (visible eyes) #d4a888
gun body           #3a3a40
gun barrel         #4a4a50
muzzle flash hi    #fff8c0
muzzle flash mid   #ffd76a
muzzle flash edge  #ff8a40
```

## Personality / fighting style

- **Holds 70–110 px range** from the protagonist. Backs up if you close in.
- **Two attacks:**
  - Regular `shot` — 9 dmg straight bullet. Fired roughly every 1.2 s.
  - `charged` shot (every 4th attack) — 36-frame telegraphed wind-up with sparkle particles, fires a heavy 18-dmg orange-tracer projectile. Devastating if it lands.
- **Never melees.** If pinned, dashes back to range first.
- **Calm.** Doesn't talk during combat.

## Animations

| Slot      | Frames | Notes |
|-----------|-------:|-------|
| `idle`    | 4 | Gun held two-handed at chest height. Eyes scan. |
| `walk`    | 6 | Backwards walk while keeping gun raised — for retreating. Mirror for forward walk if needed. |
| `atk1`    | 5 | Regular shot. F1–F2 = raise + aim, F3 = trigger pull (muzzle flash), F4–F5 = recoil + recover. |
| `atk2`    | 8 | Charged shot. F1–F4 = long aim with glow particles around barrel, F5 = bigger muzzle flash, F6–F8 = harder recoil. |
| `hurt`    | 3 | Body twists from the hit. Gun arm drops one frame. |
| `dead`    | 4 | Falls. Gun lands on ground beside body. |

## DO NOT include

- Visible KANE branding — Lamplights are deniable. No badges.
- Long flowing coats — fitted only.
- Eye exposure beyond a slit — face stays masked.
- Two visible guns / dual wield — single pistol only.

## Sheet specs

- 8 columns × 4 rows = 32 cells (~30 frames used)
- Cell size: **48 × 72**
- Magenta `#ff00ff` background
- Bottom-center anchor
