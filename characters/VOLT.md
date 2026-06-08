# VOLT — Stage 9 Boss

Kane's loyal lieutenant. Real name **Daniel Vega.** Lost both legs and his left arm in a car accident three years ago. Kane paid for the prosthetics — top-end military-grade cybernetic limbs that nobody at his pay grade should be able to afford. Volt knows exactly what he owes.

He guards Kane's tower because Kane gave him the legs back. He'll fight whoever climbs the building, no questions, until he can't anymore.

> ## 🛑 REQUIRED ANIMATION ROWS — read first
>
> The sheet must contain **12 distinct animation rows** in this exact order, one anim per row, no skipping:
>
> 1. `idle` (4 frames)
> 2. `walk` (6 frames)
> 3. `atk1` — CYBER-HAYMAKER (6 frames) — **CYBER (left) fist HORIZONTAL forward at chest height**, blue powerlines on the cyber arm BRIGHTEN white during F1–F2 wind-up
> 4. `atk2` — TWIN-FIST LAUNCHER UPPERCUT (8 frames) — **BOTH fists ASCENDING vertically into an overhead V**, white lightning star-burst at the cyber elbow at peak
> 5. `atk3` — PLASMA ORB (8 frames) — **cyber palm cradles a GROWING BLUE ORB** (2→4→6→8 px), then releases it forward as a projectile (the only projectile attack)
> 6. `atk4` — CYBER AXE KICK (5 frames) — **CYBER (left) leg fully VERTICAL above the head**, heel DROPS straight down with a vertical blue plasma trail (the only kick)
> 7. `atk5` — THUNDER CLAP (7 frames) — **BOTH fists CLAP TOGETHER at chest centerline**, horizontal shockwave rings radiate LEFT and RIGHT simultaneously (the only bilateral AOE)
> 8. `clinch` — LIGHTNING CLINCH GRAB (8 frames) — **CYBER hand CLAMPS the opponent's shoulder at arm's length**, lightning arcs travel UP the held opponent's body (the only grab + only sustained-current attack)
> 9. `special` — OVERDRIVE SURGE (12 frames) — **cyber arm RAISED OVERHEAD then POINTS DOWN**, expanding LIGHTNING RING radiates outward 360° at chest height (the only full-ring AOE)
> 10. `counter` — CYBER-REFLECT + ELBOW SMASH (6 frames) — **cyber palm forms a flat lightning SHIELD-PLANE in front of the chest** absorbing the strike, then a close-range CYBER ELBOW drives forward through the shield (no projectile return — that's atk3)
> 11. `hurt` (3 frames)
> 12. `dead` (6 frames)
>
> **Total: 79 frames in 12 rows.** Every row must be present. If any row is missing, the engine substitutes a fallback that may not match the intended move.
>
> ## 🛑 SILHOUETTE DIFFERENTIATION — read before drawing any attack
>
> Volt's sheet kept producing attacks that all looked like "cyborg with glowing arm throwing blue VFX." Every attack below must occupy a DIFFERENT silhouette quadrant — if two attacks share a silhouette, redraw one. The cyber-arm and cyber-leg VFX are designed as a **chart of directions and ranges** — every move has a different electrical signature shape.
>
> | Attack | Body axis | Striking limb | Direction | Unique silhouette tell |
> |---|---|---|---|---|
> | `atk1` cyber-haymaker | Vertical, rotated 30° on the hip drive | CYBER (left) fist | Horizontal forward at chest height | Single cyber-fist forward + 4-px blue plasma trail behind the knuckles (the only single-fist forward strike) |
> | `atk2` twin-fist uppercut | Vertical, extending UP | BOTH fists | Ascending vertical into overhead V | Both arms above the head in a V-shape + white lightning star-burst at the cyber ELBOW (the only attack going UP + only twin-fist attack) |
> | `atk3` plasma orb | Vertical, body squared to target | Cyber palm (open) | Releases a projectile forward | The orb is DETACHED from the hand by F5 (the only attack with a free-flying projectile) + visible 2→4→6→8 px charge growth |
> | `atk4` cyber axe kick | Vertical with one leg raised above the head | CYBER (left) leg / heel | Descending vertical (leg) | Cyber LEG fully VERTICAL above the head silhouette + vertical blue plasma trail on the descending heel (the only kick) |
> | `atk5` thunder clap | Vertical, body squared and slightly crouched | BOTH fists meet at center | Horizontal outward LEFT and RIGHT simultaneously | Both fists clenched together at chest centerline + horizontal shockwave rings on BOTH sides (the only symmetric bilateral AOE) |
> | `clinch` lightning grab | Vertical, arm extended forward at arm's length | CYBER hand (closed grip) | Held forward + current travels UP | Imagined opponent dangling in the cyber-grip at arm's length + lightning arcs jumping UP their body (the only grab + only sustained current) |
> | `special` overdrive surge | Vertical, arm raised overhead then pointing DOWN at the floor | Whole cyber arm | 360° expanding ring at chest height | Expanding ring of pure electricity radiates outward in ALL directions from Volt's feet/chest (the only full 360° ring) + whole-body electric arcs |
> | `counter` cyber-reflect + elbow | Vertical, cyber arm across the chest as a shield-plane | Shield-plane → cyber ELBOW | Defensive then forward at chest height | F2 visible flat shield-plane of 3 lightning arcs in front of the chest (only flat-plane VFX); F4 close-range cyber ELBOW driving forward (only elbow attack) — NO free projectile (that's atk3's job) |
>
> Cross-checks before approving the sheet:
> - **atk1 vs atk2:** atk1 = ONE cyber fist forward HORIZONTAL at chest height. atk2 = BOTH fists ASCENDING VERTICAL into an overhead V. If atk1 shows both arms moving or atk2 shows a horizontal punch, redraw — atk1 is a single forward strike, atk2 is the dual rising launcher.
> - **atk3 vs special:** atk3 RELEASES an orb FORWARD as a single projectile (line-shaped trajectory). Special radiates a RING 360° outward from Volt's body (omni-directional). If special looks like a single forward blast, redraw — it must be a closing ring of light around him.
> - **atk3 vs counter:** atk3 is OFFENSIVE — cyber palm charges an orb then THROWS it forward as a free projectile. Counter is DEFENSIVE — cyber palm holds a flat shield-plane in front of the chest, then a CYBER ELBOW (not a projectile) strikes forward. If counter shoots a free projectile, redraw — that overlaps with atk3 and breaks the differentiation.
> - **atk4 vs atk2:** both put a limb above the head. atk2 = ARMS up in an overhead V. atk4 = ONE cyber LEG fully vertical above the head. If atk4 shows arms overhead, redraw — atk4 is the only kick and the leg IS the weapon at peak.
> - **atk5 vs special:** both involve electricity radiating outward. atk5 = horizontal shockwaves ONLY left+right (bilateral, planar). special = full 360° ring at chest height (omni-directional). If atk5 shows a circular ring, redraw — atk5's wave is a flat horizontal bar, special's is the full ring.
> - **clinch vs atk1:** both use the cyber arm forward. clinch has the cyber HAND CLAMPED on an imagined target at arm's length with current flowing UP the target's body across multiple frames. atk1 is a single-frame impact + retract. If clinch reads as a one-frame punch, redraw — clinch is a sustained hold with visible electric arcs jumping UP.
> - **counter vs atk1:** counter's F4 cyber elbow strikes CLOSE-RANGE (the elbow is the contact, body folded forward), not a fully extended fist. If counter shows a long-extended cyber fist, it's atk1 — redraw counter so the ELBOW is the contact point with the forearm folded back.

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
  - **`counter` — Cyber-reflect + elbow smash.** Defensive shield-plane absorb followed by a close-range cyber elbow. **Visual signature: F2 the cyber palm faces outward forming a flat SHIELD-PLANE of 3 lightning arcs in front of the chest (the only flat-plane VFX in his kit). F3 the incoming strike hits the plane, sparks burst at the contact point. F4 the cyber arm FOLDS — forearm pulls back hard so the ELBOW leads, then drives forward at close range into the opponent's sternum with a white discharge spark at the elbow tip. F5 follow-through, plane dissipates. F6 recovery.** Reads as "she hit a wall, and then the wall punched her with its elbow." Keeps the projectile job entirely with atk3 — counter never throws anything. 18 dmg + parry effect.
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
| `atk4`     | 5 | **Cyber axe kick.** F1 = cyber leg starts rising, **powerlines on the cyber thigh BRIGHTEN from dim cyan to electric white**. F2 = leg continues rising straight up past head height. F3 = **peak — cyber leg fully vertical above the head, foot at the top of the silhouette**. F4 = drive downward (heel leading, **4-px vertical blue plasma trail behind the descending heel**). F5 = impact — heel at chest-of-target height. |
| `atk5`     | 7 | **Thunder clap.** F1 = both arms wide apart at shoulder height, powerlines on cyber arm BRIGHT. F2 = arms start swinging inward toward chest. F3 = **arms approaching each other at center, both fists clenched, body crouching slightly**. F4 = **CLAP — fists meet at chest height with a WHITE LIGHTNING STAR-BURST at the impact point, 6-px shockwave rings radiating LEFT and RIGHT simultaneously to ~24 px on each side**. F5 = shockwaves continue outward (smaller rings). F6 = recovery, arms drop. F7 = back to stance. **Visual identity: both fists colliding + horizontal shockwave both directions.** |
| `clinch`   | 8 | **Lightning clinch.** F1 = cyber arm extends forward, palm open. F2 = **cyber hand CLAMPS shut on the imagined opponent's shoulder, powerlines BRIGHTEN to white instantly**. F3 = held grip — imagined opponent locked in cyber-grip at arm's length. F4 = **CURRENT FLOWS — 4-5 small white lightning arcs jump from the cyber hand UP the imagined opponent's body**. F5 = current peaks, opponent visibly convulsing in his grip. F6 = current peak +1, more arcs. F7 = release — cyber hand opens, opponent flies back. F8 = recovery. **Multi-hit electric grab.** |
| `special`  | 12 | **OVERDRIVE SURGE — signature.** F1 = cyber arm raised vertically at the side, powerlines start brightening. F2 = powerlines reach normal-bright. F3 = **powerlines GO WHITE-HOT, cyber arm visibly trembling**. F4 = **cyber arm RAISED OVERHEAD, body coiled, electricity arcing all around the body now (8+ visible arcs)**. F5 = **CYBER ARM POINTS DOWN, body explodes outward**. F6 = **expanding LIGHTNING RING radiates outward from Volt at chest height — a 16-px ring of pure blue-white electricity** (first wave). F7 = ring at 24 px out, arcs jumping in all directions. F8 = ring at 32 px out, peaks. F9 = ring fading. F10 = arcs dissipating. F11–F12 = recovery, body returns to stance, powerlines dim back. **Visual identity: expanding lightning ring centred on Volt + entire screen flashes blue.** Multi-hit AOE. Launches. |
| `counter`  | 6 | **Cyber-reflect + elbow smash.** F1 = cyber arm rises across the body in a defensive guard, powerlines starting to brighten. F2 = **cyber palm faces outward forming a flat SHIELD-PLANE — 3 lightning arcs in a flat plane suspended in front of the chest (the only flat-plane VFX in Volt's kit)**. F3 = incoming strike IMPACTS the shield-plane, sparks burst at the contact point. F4 = **cyber arm FOLDS — forearm pulls back hard so the ELBOW leads, then drives FORWARD at close range into the opponent's sternum, white discharge spark at the elbow tip, body folded slightly forward (the only elbow attack in his kit)**. F5 = follow-through, elbow held one frame, shield-plane dissipating. F6 = recovery, arm returns to guard. **Visual identity: flat shield-plane catch + close-range cyber elbow. No free projectile (that's atk3's job).** |
| `hurt`     | 3 | Body recoils. **Cyber limbs less affected** — organic side flinches harder. Powerlines flicker on F2. |
| `dead`     | 6 | F1 = falls to knees. F2 = collapses forward. F3–F4 = **cyber limbs spasm — small white sparks at the cyber elbow and knee joints** (3-pixel star-bursts). F5 = sparks fading. F6 = powerlines fully dark, body settled. |

## DO NOT include

- Full-body armor — organic torso + cyber limbs is the iconic mix.
- Bright cape / coat — Volt is utility-grade.
- A face mask — face is fully visible.
- Multiple visible weapons — his body IS the weapon.
- Glowing red — blue power-lines only.

## Visual VFX summary

Volt's identity is the **blue cyber-arm powerlines** brightening before strikes + electricity discharge on impacts. **Every attack occupies a distinct silhouette quadrant** (see the SILHOUETTE DIFFERENTIATION table near the top) so no two moves blur together.

- `atk1` CYBER-HAYMAKER — single CYBER fist horizontal forward at chest height; powerlines BRIGHTEN from dim cyan to electric white in F1–F2 + 4-px blue plasma trail behind the cyber fist (the only single-fist forward strike)
- `atk2` TWIN-FIST LAUNCHER UPPERCUT — BOTH arms ASCENDING into an overhead V silhouette + WHITE LIGHTNING STAR-BURST (6-px) erupting from the cyber elbow at peak (the only ascending attack + only twin-fist)
- `atk3` PLASMA ORB — cyber palm cradles a GROWING orb (2→4→6→8 px during charge) with 3 lightning arcs jumping to the forearm at peak charge, then RELEASES the orb forward as a free projectile (the only projectile)
- `atk4` CYBER AXE KICK — CYBER (left) LEG fully VERTICAL above the head, then heel DROPS straight down with a vertical 4-px blue plasma trail behind the descending heel (the only kick)
- `atk5` THUNDER CLAP — both fists CLAP at chest centerline + WHITE LIGHTNING STAR-BURST at the impact point + 6-px shockwave rings radiating LEFT and RIGHT simultaneously (the only bilateral / symmetric AOE)
- `clinch` LIGHTNING CLINCH GRAB — cyber hand CLAMPED on the opponent's shoulder at arm's length with 4–5 lightning arcs jumping UP the held opponent's body (the only sustained grab + only sustained-current attack)
- `special` OVERDRIVE SURGE — cyber arm overhead then pointing DOWN; expanding LIGHTNING RING radiates outward 360° from Volt's chest height (16 px → 24 → 32 px) + entire body wreathed in electric arcs (the only full 360° ring AOE)
- `counter` CYBER-REFLECT + ELBOW SMASH — flat SHIELD-PLANE of 3 lightning arcs in front of the chest absorbing the strike, then a close-range CYBER ELBOW driving forward into the opponent's sternum (the only elbow attack; NO projectile return — that's atk3's job)

**Hurt / flinch:** F1 body recoils, cyber limbs LESS affected (organic side flinches harder). F2 powerlines FLICKER (brightness drops then surges). 1-px white impact spark on the cyber armour.

**Dead:** Falls to knees, collapses forward. F3–F4 cyber limbs SPASM with small white sparks at the elbow and knee joints. Powerlines fully dark by F6.

## Sheet specs

- 8 columns × 5 rows = 40 cells (~36 frames used)
- Cell size: **64 × 96**
- Magenta `#ff00ff` background
- Bottom-center anchor

## Boss-fight design notes

- HP ≈ 280.
- Music: `kane` theme during this fight (the most aggressive of the cast).
- Defeat: drops to his knees, cyber legs lock up audibly. The blue power-lines flicker out. He says "Tell Kane I held the door."
