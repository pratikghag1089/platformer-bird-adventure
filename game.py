import pygame
import config
from bird import Bird
from obstacle_manager import ObstacleManager
from collision import check_obstacles, check_boundaries


class Game:
    def __init__(self):
        # Initialize game state
        self.state = config.STATE_MENU
        
        # Create game objects
        self.bird = Bird()
        self.obstacle_manager = ObstacleManager()
        
        # Score tracking
        self.score = 0
    
    def update(self, dt):
        """
        Update game logic for one frame.
        
        Args:
            dt: delta time (unused in fixed timestep, but kept for interface)
        """
        if self.state != config.STATE_PLAYING:
            return
        
        # Update bird physics
        self.bird.update(dt)
        
        # Update obstacles (pass bird's x position for scoring)
        self.obstacle_manager.update(self.bird.x)
        
        # Get current bird rectangle for collision
        bird_rect = self.bird.get_rect()
        
        # Check collisions with obstacles
        obstacle_rects = self.obstacle_manager.get_obstacles()
        if check_obstacles(bird_rect, obstacle_rects):
            self.state = config.STATE_GAME_OVER
            return
        
        # Check collisions with screen boundaries
        if check_boundaries(bird_rect, config.SCREEN_HEIGHT):
            self.state = config.STATE_GAME_OVER
            return
        
        # Update score from passed obstacles
        self.score = self.obstacle_manager.passed
    
    def restart(self):
        """
        Reset game to initial playing state.
        """
        # Reset bird to initial state
        self.bird = Bird()
        
        # Reset obstacle manager
        self.obstacle_manager.reset()
        
        # Reset score
        self.score = 0
        
        # Set state to playing
        self.state = config.STATE_PLAYING
    
    def start_game(self):
        """
        Start a new game from menu state.
        """
        if self.state == config.STATE_MENU:
            self.restart()