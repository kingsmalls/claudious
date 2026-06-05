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

- **Four signature moves — strike / uppercut / shock / cyber-axe-kick. The cyber-arm BLUE POWERLINES are the visual identity — every move involves them brightening, dimming, or arcing. The cyber LEG joins in on the axe kick.**
  - **`strike` — Cyber-haymaker.** Heavy cybernetic punch with the cyber arm. **Visual signature: F1–F2 the blue power-lines on the cyber arm BRIGHTEN from dim cyan to electric-bright white** (the charge tell — visible from across the screen). F3 the cyber fist drives forward leaving a 4-px blue plasma trail behind the knuckles. F4 the powerlines dim back. Organic arm stays back as counter-weight. 14 dmg, 130 knockback.
  - **`uppercut` — Twin-fist launcher.** Telegraphed launcher with both arms driving upward. **Visual signature: F3–F5 silhouette is an upward V — both arms vertical above the head, organic fist on one side, cyber fist on the other, body extended fully. F5 peak has a WHITE LIGHTNING FLASH erupting from the cyber elbow's joint** (a 6-px star-burst, white core fading to blue). 22 dmg, 80 knockback. Launches the protagonist into the air for juggle followups.
  - **`shock` — Plasma orb.** Fires a glowing ball of electricity. **Visual signature: F1–F4 the cyber palm cradles a GROWING BLUE ORB** — 2 px on F1, 4 px on F2, 6 px on F3, 8 px on F4 (peak charge). The orb has a white-hot core and a blue-cyan halo, with 2–3 small lightning arcs jumping from the orb to the cyber forearm. F5 release — orb leaves the hand. 14 dmg, 120 knockback.
  - **`cyber_axe` — Servo-driven axe kick.** Heavy overhead axe kick with the cybernetic leg. **Visual signature: F1–F2 the cyber leg rises STRAIGHT UP past head height (the powerlines on the cyber thigh BRIGHTEN from cyan to white as the servos load). F3 peak — leg vertical above the head, the foot at the top of the silhouette, a 1-px white glow at the cyber knee-joint. F4 drives DOWNWARD with the heel leading — leaving a vertical 4-px blue plasma trail behind the descending heel. F5 impact — heel at chest-of-target height, body slightly leaned back.** 20 dmg + 160 knockback. The only kick in the game with a tech tell — the powerline charge predicts the strike.
- **Phase 2 (<50% HP):** more shock spam, mixes uppercut into combos.
- **Quiet during fights.** Speaks only at start: "Kane built me. So I owe him a building."

## Animations

| Slot       | Frames | Notes |
|------------|-------:|-------|
| `idle`     | 4 | **Heavy planted stance**, organic arm relaxed, cyber arm slightly raised (always at the ready). **Power-lines pulse blue** — dim on F1/F3, brighter cyan on F2/F4 (heartbeat rhythm). Shoulder rises 1 px on breath. |
| `walk`     | 6 | **Cyber-leg stomp** — the metal leg lands heavy with a 1-px highlight on the joint, the organic leg lands soft. Asymmetric gait. Power-lines pulse with each cyber-leg step. |
| `atk1`     | 6 | **Cyber-haymaker.** F1 = cyber arm cocks back, **powerlines start brightening from dim to bright white**. F2 = arm fully cocked, **powerlines at peak white intensity**. F3 = forward drive (cyber fist forward, **4-px blue plasma trail behind the knuckles**). F4 = peak punch, fist 18 px past body. F5 = retract. F6 = powerlines dim back to idle cyan. |
| `atk2`     | 8 | **Twin-fist launcher.** F1 = deep crouch (both arms drop, knees bend). F2 = load (both fists at hip, body coiled). F3 = explosive rise begins, both arms swinging up. F4 = both arms rising past chest. F5 = **peak — upward V silhouette, both fists vertical above head, body fully extended skyward, WHITE LIGHTNING STAR-BURST erupting from the cyber elbow joint (6-px white core fading to blue)**. F6 = held peak. F7 = arms lowering. F8 = recovery. |
| `atk3`     | 8 | **Plasma orb.** F1 = cyber arm raises, palm forward, **2-px blue orb forming at palm center**. F2 = orb grows to 4 px, first lightning arc visible from orb to forearm. F3 = orb at 6 px, 2 lightning arcs. F4 = **peak charge — orb at 8 px, white-hot core, blue-cyan halo, 3 lightning arcs jumping to forearm**. F5 = release — orb leaves the palm 12 px ahead, cyber palm still glowing faintly. F6–F7 = recovery, palm dimming. F8 = back to stance. |
| `atk4`     | 5 | **Cyber axe kick.** F1 = cyber leg starts rising, **powerlines on the cyber thigh BRIGHTEN from dim cyan to electric white** as the servos load. F2 = leg continues rising straight up past head height. F3 = **peak — cyber leg fully vertical above the head, foot at the top of the silhouette, 1-px white glow at the cyber knee-joint, body leaned back for balance**. F4 = drive downward (heel leading, **4-px vertical blue plasma trail behind the descending heel**). F5 = impact — heel at chest-of-target height, body settling, powerlines dimming. |
| `hurt`     | 3 | Body recoils. **Cyber limbs less affected** — organic side flinches harder. Powerlines flicker on F2. |
| `dead`     | 6 | F1 = falls to knees. F2 = collapses forward. F3–F4 = **cyber limbs spasm — small white sparks at the cyber elbow and knee joints** (3-pixel star-bursts). F5 = sparks fading. F6 = powerlines fully dark, body settled. |

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
