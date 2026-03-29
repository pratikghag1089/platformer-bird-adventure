import config
from bird import Bird
from obstacle_manager import ObstacleManager
from collision import check_obstacles, check_boundaries


class Game:
    def __init__(self):
        self.bird = Bird()
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.state = "MENU"  # MENU | PLAYING | GAME_OVER

    def start_game(self):
        self.state = "PLAYING"

    def restart(self):
        self.bird.reset()
        self.obstacle_manager.reset()
        self.score = 0
        self.state = "PLAYING"

    def update(self, dt):
        if self.state != "PLAYING":
            return

        self.bird.update(dt)
        self.obstacle_manager.update(dt)
        self.score = self.obstacle_manager.passed

        bird_rect = self.bird.get_rect()
        obstacles = self.obstacle_manager.get_obstacles()

        if check_obstacles(bird_rect, obstacles) or check_boundaries(bird_rect, config.SCREEN_HEIGHT):
            self.state = "GAME_OVER"
