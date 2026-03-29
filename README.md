# Platformer Bird Adventure

A standalone desktop game where a bird character automatically moves forward through a side-scrolling environment, requiring the player to perform actions like jumping and ducking to navigate obstacles and survive.

## Goals

- Create a responsive, challenging, and fun core gameplay loop that captures the "one more try" spirit.
- Establish a foundational game structure that can be expanded for future commercial release.
- Deliver a polished, playable desktop application focused on perfecting core platformer mechanics.

---
## Architecture

**Python 3.x + Pygame** — Pygame is the ideal fit for a minimalist 2D desktop game: zero boilerplate, immediate window/input/surface primitives, and a tight game-loop model. No engine overhead, no build step. Targeting Windows via `pygame` wheel but inherently cross-platform.
---

### Project Files

- `main.py` — Entry point: initializes Pygame, runs the 60 FPS game loop, delegates events to InputHandler, calls Game.update and Renderer.draw each frame
- `config.py` — All game constants: screen dimensions, physics (gravity, jump velocity), bird sizes (normal/ducking height), obstacle parameters (speed, gap size, spawn interval), colors, and font size
- `bird.py` — Bird class: stores position, velocity, and ducking state; applies gravity each update, executes jump and double-jump impulses, toggles duck mode (shrinks hitbox height while pinning bottom edge), exposes get_rect() for collision
- `obstacles.py` — ObstacleManager class: spawns pipe-pair dicts at timed intervals with randomized gap positions, scrolls all obstacles left each update, removes off-screen obstacles, tracks passed-obstacle count for scoring
- `collision.py` — Pure-function module with check_obstacles(bird_rect, obstacles) for AABB overlap tests against pipe rects and check_boundaries(bird_rect, screen_h) for top/bottom screen edge detection
- `renderer.py` — Renderer class: draws sky background, bird shape (color-coded by state), green pipe obstacles, score HUD in top-right corner, and game-over overlay with final score and restart prompt
- `input_handler.py` — InputHandler class: maps Pygame KEYDOWN events to semantic action strings (jump, duck, restart, quit) based on configurable key bindings from config
- `game.py` — Game class: state machine (menu/playing/game_over) owning Bird, ObstacleManager, and score; update() orchestrates physics, obstacle scrolling, collision checks, and score increments; restart() resets all state for immediate replay

_See `architecture.md` for the full design._

---

_Development log will be appended as issues are completed._

## Development Log

### Cycle 1 — #1: Set up project structure and configuration

**APPROVE** — The implementation fully satisfies all acceptance criteria. config.py contains all required constants including screen dimensions, physics parameters, colors, and font sizes. main.py properly initializes Pygame, sets up a 60 FPS game loop, handles QUIT and ESC events, and displays a window with the correct title and background color.
