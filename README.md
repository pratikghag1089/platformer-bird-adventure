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

### Cycle 2 — #2: Implement Bird class with physics and controls

**REQUEST_CHANGES** — The Bird class implementation meets most acceptance criteria, including position, velocity, state machine, gravity, ducking with hitbox pinning, and screen boundaries. However, there is a critical bug in the jump() method where the state is set to 'jumping' before checking for ducking, preventing the unduck logic from executing when jumping from a ducking state.

### Cycle 3 — #3: Create obstacle generation and movement system

**APPROVE** — The implementation fully meets all acceptance criteria for the obstacle generation and movement system. The ObstacleManager class correctly spawns pipe pairs with randomized gaps, moves them left at constant speed, removes off-screen obstacles, and tracks passed obstacles for scoring. All required constants are properly defined in config.py.

### Cycle 4 — #4: Implement collision detection and game state management

**REQUEST_CHANGES** — The Game class and collision detection meet all acceptance criteria, but main.py is not updated to use the Game class, making the game non-functional. Additionally, there is a bug in bird.py where the jump method does not properly handle unducking when ducking.

### Cycle 5 — #5: Create renderer and visual elements

**REQUEST_CHANGES** — The renderer implementation meets most acceptance criteria with proper visual elements, but has a critical bug in bird state handling and missing integration with the main game loop. The bird's jump method incorrectly changes state after checking ducking, and the renderer isn't being used in main.py.

### Cycle 6 — #6: Implement input handling and integrate all components

**REQUEST_CHANGES** — The implementation meets most acceptance criteria with proper input handling and component integration. However, there's a critical bug in the bird's jump() method where the ducking state check occurs after setting state to 'jumping', preventing proper unducking when jumping while ducking. Additionally, the restart key mapping doesn't match the issue requirement (R key) in the game over screen.

### Cycle 7 — #9: Fix jump method to handle unducking properly

**APPROVE** — The implementation correctly modifies the jump() method to check for ducking state before changing to jumping state, ensuring the bird unducks first (restores normal height) before applying the jump impulse. The jumps_remaining counter is decremented correctly regardless of ducking state. All acceptance criteria are met without introducing any new bugs.

### Cycle 8 — #12: Integrate Game class into main loop

**APPROVE** — The implementation fully meets all acceptance criteria: main.py imports and instantiates Game, calls Game.update() each frame, handles input via InputHandler with proper action routing, and reflects all game state transitions in the loop. The code is well-structured with clear separation of concerns.

### Cycle 9 — #13: Fix bird jump method to handle unducking

**APPROVE** — The implementation correctly reorders the jump logic to unduck before applying the jump impulse and updating state. All acceptance criteria are met: ducking is properly reversed, jump is applied after unducking, and state transitions to 'jumping' correctly.

### Cycle 10 — #15: Fix bird state logic in jump method

**APPROVE** — The implementation correctly fixes the jump method's state transition logic. When ducking, the bird now properly unducks before applying the jump impulse, and jumps_remaining is decremented appropriately in all cases. The code meets all acceptance criteria without introducing new bugs.

### Cycle 11 — #16: Integrate renderer with main game loop

**APPROVE** — The implementation correctly integrates the Game and Renderer classes into the main game loop. All acceptance criteria are met: Game and Renderer are instantiated, game state is passed to the renderer each frame, and the game loop properly updates and renders the game state.

### Cycle 12 — #17: Add missing bird color constants to config

**REQUEST_CHANGES** — The config constants have been correctly added and updated as specified, but the renderer still uses hard-coded color values for jumping and ducking states instead of referencing the new config constants.

### Cycle 13 — #19: Fix bird jump() method ducking state logic

**APPROVE** — The implementation correctly moves the ducking state check before setting state to 'jumping' in the jump() method. The unduck() method is now properly called when jumping while ducking, restoring the bird's normal height. All acceptance criteria are met with no critical bugs found.

### Cycle 14 — #20: Fix restart key mapping in game over screen

**REQUEST_CHANGES** — The implementation correctly adds R key restart functionality and documents SPACE as a convenience feature. However, the UP arrow key also triggers restart in the game over state but is not mentioned in the restart prompt text, creating a mismatch between actual key bindings and displayed instructions.
