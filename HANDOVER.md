# HANDOVER.md

## 1. What Was Built
A minimalist 2D platformer game where the player controls a bird that must navigate through gaps in moving pipe obstacles. The game features three states: a menu screen, active gameplay, and a game-over screen with score display. Players can jump (including a double-jump) and duck to adjust the bird's hitbox, with the goal of surviving as long as possible to achieve a high score.

## 2. Getting Started
**Prerequisites:** Python 3.x installed on your system.

1. **Install dependencies:**
   ```bash
   pip install pygame
   ```
2. **Run the game:**
   ```bash
   python main.py
   ```
3. **Controls:**
   - **SPACE/UP Arrow:** Jump (from menu or during gameplay)
   - **DOWN Arrow:** Duck (during gameplay)
   - **R:** Restart (from game-over screen)
   - **ESC:** Quit

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #34 | Remove UP arrow restart functionality from game over state | ✅ Done |

## 4. Known Issues
None — all implemented features passed QA review.

## 5. How to Resume
No further development cycles are required. All issues have been resolved and approved.