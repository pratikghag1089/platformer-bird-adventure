## Architecture: Platformer Bird Adventure

### Tech Stack
**Python 3.x + Pygame** — Pygame is the ideal fit for a minimalist 2D desktop game: zero boilerplate, immediate window/input/surface primitives, and a tight game-loop model. No engine overhead, no build step. Targeting Windows via `pygame` wheel but inherently cross-platform.

---

### Component Design

**`Bird`** — Owns the player entity: position, velocity, hitbox, and state machine (normal / jumping / ducking). Applies gravity each tick, handles jump impulse (with double-jump gate via `jumps_remaining`), and toggles duck by reducing hitbox height while pinning the bottom edge. Exposes `get_rect()` for collision.

**`ObstacleManager`** — Spawns pipe-pair obstacles at timed intervals, scrolls them left at constant speed, and culls off-screen entries. Each obstacle stores a randomized gap position. Tracks which obstacles have been passed to increment score. Exposes `passed` count for the HUD.

**`CollisionDetector`** — Pure-function module: `check_obstacles(bird_rect, obstacles)` tests axis-aligned rectangles; `check_boundaries(bird_rect, screen_h)` tests top/bottom screen edges. Returns `bool`.

**`Game`** — Central state machine (`MENU → PLAYING → GAME_OVER`). Owns `Bird`, `ObstacleManager`, and score. `update(dt)` orchestrates: bird physics → obstacle scroll → collision test → score update. `restart()` resets all mutable state.

**`Renderer`** — All drawing in one place: sky gradient background, bird shape (color-coded by state), green pipe rectangles, score HUD (top-right), and game-over overlay with final score + restart prompt. Stateless — receives current game state each frame.

**`InputHandler`** — Maps `KEYDOWN` events to semantic actions (`JUMP`, `DUCK`, `RESTART`, `QUIT`). Returns an action enum so `main.py` stays a thin loop.

**`main.py`** — Pygame init, clock, event loop. Delegates to `InputHandler` → `Game` → `Renderer`. Fixed 60 FPS tick.

**`config.py`** — All numeric constants (screen size, gravity, speeds, colors, font size). Single source of truth; every other module imports from here.

---

### Data Flow

```
┌──────────┐   KEYDOWN    ┌──────────────┐
│  Pygame   │────────────▶│ InputHandler  │
│  Events   │             └──────┬───────┘
└──────────┘                    │ action enum
                                ▼
                         ┌─────────────┐
                         │    Game      │
                         │  .update()   │
                         │             │
                         │  Bird       │◀── gravity, jump, duck
                         │  Obstacles  │◀── spawn, scroll, cull
                         │  Collision  │◀── rect overlap test
                         │  Score      │◀── passed count
                         └──────┬──────┘
                                │ state + entities
                                ▼
                         ┌─────────────┐
                         │  Renderer   │
                         │  .draw()    │──▶ screen flip
                         └─────────────┘
```

---

### Key Design Decisions

1. **No ground plane** — Bird is fully aerial (Flappy Bird model). Obstacles are pipe pairs with vertical gaps. Ducking shrinks the hitbox to pass under high top-pipes. This keeps physics simple (one axis of gravity) while enabling both jump and duck to be meaningful.

2. **Hitbox pinning on duck** — When ducking, the bird's rect height shrinks but the *bottom* edge stays fixed. This means ducking makes the bird "shorter upward," naturally helping it pass under high obstacles without weird coordinate math.

3. **AABB collision only** — No pixel-perfect or circle collision. Rectangles are fast, predictable, and match the minimalist visual style (players learn exact hitboxes).

4. **Fixed timestep (60 FPS)** — No delta-time accumulation. Simple, deterministic, and sufficient for this scope. Physics constants are tuned for 60 Hz.

5. **Single renderer file** — All draw functions share the same surface/font context and are each ~15 lines. Splitting would add import overhead for no clarity gain.

---