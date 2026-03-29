import pygame
import sys
import config

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer Bird Adventure")
    
    # Create a clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Fill the screen with sky color (blank window)
        screen.fill(config.SKY_COLOR)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate at 60 FPS
        clock.tick(60)
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
