import random
import config


class ObstacleManager:
    def __init__(self):
        self.reset()

    def reset(self):
        self._obstacles = []
        self._spawn_timer = 0
        self.passed = 0

    def update(self, dt):
        # Spawn
        self._spawn_timer += dt
        if self._spawn_timer >= config.OBSTACLE_SPAWN_INTERVAL:
            self._spawn_timer = 0
            gap_y = random.randint(
                config.OBSTACLE_MIN_GAP_Y, config.OBSTACLE_MAX_GAP_Y
            )
            self._obstacles.append({
                "x": config.SCREEN_WIDTH,
                "gap_y": gap_y,
                "scored": False,
            })

        # Scroll
        for obs in self._obstacles:
            obs["x"] -= config.OBSTACLE_SPEED * dt

        # Score check
        for obs in self._obstacles:
            if not obs["scored"] and obs["x"] + config.OBSTACLE_WIDTH < config.BIRD_X:
                obs["scored"] = True
                self.passed += 1

        # Cull off-screen
        self._obstacles = [
            obs for obs in self._obstacles
            if obs["x"] + config.OBSTACLE_WIDTH > 0
        ]

    def get_obstacles(self):
        return list(self._obstacles)
