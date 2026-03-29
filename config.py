# Configuration constants for Platformer Bird Adventure

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Physics
GRAVITY = 0.5
JUMP_FORCE = -10  # Negative because up is negative y in Pygame
BIRD_SPEED = 3
OBSTACLE_SPEED = 3

# Obstacle configuration
OBSTACLE_SPAWN_INTERVAL = 90  # Frames between spawns (1.5 seconds at 60 FPS)
OBSTACLE_GAP_SIZE = 150       # Vertical gap between pipes in pixels
PIPE_WIDTH = 80               # Width of each pipe
PIPE_MIN_HEIGHT = 50          # Minimum pipe height (ensures gap is always passable)

# Colors
SKY_COLOR = (135, 206, 235)  # Light blue
BIRD_COLOR = (255, 215, 0)    # Gold
BIRD_DUCK_COLOR = (255, 165, 0)  # Orange
PIPE_COLOR = (34, 139, 34)    # Forest green
PIPE_HIGHLIGHT = (50, 205, 50)  # Lime green
SCORE_COLOR = (255, 255, 255)  # White
GAME_OVER_COLOR = (255, 0, 0)  # Red

# Font sizes
FONT_SIZE_LARGE = 48
FONT_SIZE_MEDIUM = 36
FONT_SIZE_SMALL = 24

# Game states
STATE_MENU = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2
