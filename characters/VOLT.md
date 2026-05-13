# VOLT — Stage 9 Boss

Kane's loyal lieutenant. Real name **Daniel Vega.** Lost both legs and his left arm in a car accident three years ago. Kane paid for the prosthetics — top-end military-grade cybernetic limbs that nobody at his pay grade should be able to afford. Volt knows exactly what he owes.

He guards Kane's tower because Kane gave him the legs back. He'll fight whoever climbs the building, no questions, until he can't anymore.

## Physical

- **Age:** 34
- **Height/build:** 6'1" *with the prosthetics*. Originally was 5'10". Athletic-toned upper body (organic). Below the shoulders / waist: cybernetic.
- **Skin:** Latino, medium brown (`#a87858`).
- **Body language:** *Heavy* below the waist — the cyber legs are powerful but lack the bounce of organic. Plants every step. Upper body moves naturally. The mismatch is part of the character.
- **Face:** Mid-30s, short scruff, tired eyes. Gauntness from rehab months. Resting expression: focused, not angry.

## Hair

- Buzz-cut black, ~2 px short.

## Costume (head to feet)

1. **Sleeveless dark grey tactical shirt** — `#2a2a32`, fitted across the chest. The right (organic) arm is bare and visible.
2. **CYBERNETIC LEFT ARM** — matte gun-metal grey (`#5a5e6a`) with darker shadow (`#2a2e36`) and **a thin blue power-line glow (`#4a8ad0`) running along the forearm**. Mechanical joints visible at the shoulder, elbow, wrist. The hand is articulated, plates instead of skin.
3. **CYBERNETIC LEGS (both)** — same gun-metal palette, replaced from mid-thigh down. Heavy plate construction, exposed pneumatic pistons at the knees. Glowing blue power-lines along the outside of each thigh and calf. Feet are stylized armored plates, not boots.
4. **Cargo shorts** — black (`#16161a`), end at mid-thigh where the cyber legs begin. The transition (organic skin to mechanical) is *visible* and not hidden.
5. **Belt** — black tactical belt with a small power-pack module on the right hip (`#1a1a22` with a single blue LED `#6aa0e8`).

## Identity items — REQUIRED IN EVERY FRAME

1. **The cybernetic left arm + both cyber legs** — these define Volt entirely. Always visible.
2. **Glowing blue power-lines** running along the cyber limbs. They pulse subtly (1-px glow variation per frame). Brighter during attacks.
3. **The hip-mounted power pack** with its single blue LED.

## Palette (hex)

```
shirt mid          #2a2a32
shirt shadow       #16161a
shorts             #16161a
skin (light)       #a87858
skin (shadow)      #6e4e30
hair               #1a1410
stubble            #2a201a
cyber metal mid    #5a5e6a
cyber metal shadow #2a2e36
cyber metal hi     #8a8e9a
cyber joint dark   #1a1c22
power line blue    #4a8ad0
power line hi      #8acbf4
power line shadow  #1a4a8a
LED bright         #6aa0e8
power pack body    #1a1a22
```

## Personality / fighting style

- **Three attacks:**
  - `strike` — heavy cybernetic punch with the left arm. 14 dmg, 130 knockback.
  - `uppercut` — telegraphed launcher, both organic + cyber arms. 22 dmg, 80 knockback, **launches the protagonist into the air** for juggle followups.
  - `shock` — fires a `shock` projectile (electric ball, 14 dmg, 120 knockback). Used at long range.
- **Phase 2 (<50% HP):** more shock spam, mixes uppercut into combos.
- **Quiet during fights.** Speaks only at start: "Kane built me. So I owe him a building."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | Heavy stance. Power-lines pulse. Right shoulder rises and falls on breath. |
| `walk`     | 6 | Cyber-leg stomp. Each footstep should clearly read as METAL on concrete. |
| `atk1`     | 6 | Cybernetic strike. F1–F2 = wind-up (power-lines on cyber arm BRIGHT), F3 = drive forward, F4–F6 recovery. |
| `atk2`     | 8 | Uppercut: F1–F2 deep crouch, F3–F4 explosive rise (both arms drive up), F5 peak, F6–F8 recovery. Power-lines flash white at peak. |
| `atk3`     | 8 | Shock: F1–F4 charge (cyber arm raised, growing blue glow at palm), F5 release (projectile spawns), F6–F8 recovery. |
| `hurt`     | 3 | Body recoils. Cyber limbs less affected — they don't flinch the way organic does. |
| `dead`     | 6 | Falls. Cyber limbs spasm briefly (sparks at the joints). Power-lines fade to dark over the death frames. |

## DO NOT include

- Full-body armor — organic torso + cyber limbs is the iconic mix.
- Bright cape / coat — Volt is utility-grade.
- A face mask — face is fully visible.
- Multiple visible weapons — his body IS the weapon.
- Glowing red — blue power-lines only.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~36 frames used)
- Cell size: **64 × 96**
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 280.
- Music: `kane` theme during this fight (the most aggressive of the cast).
- Defeat: drops to his knees, cyber legs lock up audibly. The blue power-lines flicker out. He says "Tell Kane I held the door."
