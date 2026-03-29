import pygame
import sys
import config
from bird import Bird
from obstacle_manager import ObstacleManager
from collision import check_obstacles, check_boundaries
from game import Game
from renderer import Renderer
from input_handler import InputHandler


def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer Bird Adventure")
    
    # Create a clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Initialize game components
    game = Game()
    renderer = Renderer(screen)
    input_handler = InputHandler()
    
    # Main game loop
    running = True
    while running:
        # Get all events
        events = pygame.event.get()
        
        # Process input
        actions = input_handler.process_events(events, game.state)
        
        # Handle actions
        for action in actions:
            if action == "QUIT":
                running = False
            
            elif action == "START":
                game.start_game()
            
            elif action == "JUMP":
                game.bird.jump()
            
            elif action == "DUCK":
                game.bird.duck()
            
            elif action == "UNDUCK":
                game.bird.unduck()
            
            elif action == "RESTART":
                game.restart()
        
        # Update game state
        game.update(1)  # Fixed timestep, dt=1
        
        # Get current game objects for rendering
        bird = game.bird
        obstacles = game.obstacle_manager.get_obstacles()
        score = game.score
        game_state = game.state
        
        # Render the frame
        renderer.draw_game(bird, obstacles, score, game_state)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate at 60 FPS
        clock.tick(60)
    
    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
