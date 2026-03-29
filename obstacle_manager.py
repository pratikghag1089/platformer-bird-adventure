import pygame
import random
import config


class ObstacleManager:
    def __init__(self):
        # List of obstacles, each as dict with 'x', 'gap_y', and 'passed' flag
        self.obstacles = []
        
        # Spawn timer (counts down each frame)
        self.spawn_timer = config.OBSTACLE_SPAWN_INTERVAL
        
        # Track how many obstacles have been passed
        self.passed = 0
    
    def update(self, bird_x):
        """Update obstacle positions and spawn new ones"""
        # Spawn new obstacle when timer expires
        self.spawn_timer -= 1
        if self.spawn_timer <= 0:
            self._spawn_obstacle()
            self.spawn_timer = config.OBSTACLE_SPAWN_INTERVAL
        
        # Move obstacles left and check for passed ones
        obstacles_to_remove = []
        for obstacle in self.obstacles:
            obstacle['x'] -= config.OBSTACLE_SPEED
            
            # Check if bird has passed this obstacle
            if not obstacle['passed'] and obstacle['x'] + config.PIPE_WIDTH < bird_x:
                obstacle['passed'] = True
                self.passed += 1
            
            # Mark for removal if off-screen
            if obstacle['x'] + config.PIPE_WIDTH < 0:
                obstacles_to_remove.append(obstacle)
        
        # Remove off-screen obstacles
        for obstacle in obstacles_to_remove:
            self.obstacles.remove(obstacle)
    
    def _spawn_obstacle(self):
        """Create a new obstacle with randomized gap position"""
        # Calculate valid range for gap position
        # Gap must leave at least PIPE_MIN_HEIGHT above and below
        min_gap_y = config.PIPE_MIN_HEIGHT
        max_gap_y = config.SCREEN_HEIGHT - config.OBSTACLE_GAP_SIZE - config.PIPE_MIN_HEIGHT
        
        # Random gap position within valid range
        gap_y = random.randint(min_gap_y, max_gap_y)
        
        # Create obstacle with initial position off-screen right
        obstacle = {
            'x': config.SCREEN_WIDTH,
            'gap_y': gap_y,
            'passed': False
        }
        
        self.obstacles.append(obstacle)
    
    def get_obstacles(self):
        """Return list of all obstacle rectangles for collision detection"""
        rects = []
        
        for obstacle in self.obstacles:
            x = obstacle['x']
            gap_y = obstacle['gap_y']
            
            # Top pipe (from top of screen to gap)
            top_pipe_height = gap_y
            if top_pipe_height > 0:
                top_rect = pygame.Rect(x, 0, config.PIPE_WIDTH, top_pipe_height)
                rects.append(top_rect)
            
            # Bottom pipe (from gap to bottom of screen)
            bottom_pipe_y = gap_y + config.OBSTACLE_GAP_SIZE
            bottom_pipe_height = config.SCREEN_HEIGHT - bottom_pipe_y
            if bottom_pipe_height > 0:
                bottom_rect = pygame.Rect(x, bottom_pipe_y, config.PIPE_WIDTH, bottom_pipe_height)
                rects.append(bottom_rect)
        
        return rects
    
    def reset(self):
        """Reset obstacle manager to initial state"""
        self.obstacles.clear()
        self.spawn_timer = config.OBSTACLE_SPAWN_INTERVAL
        self.passed = 0
