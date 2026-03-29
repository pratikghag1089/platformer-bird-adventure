import pygame
import config


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        
        # Initialize fonts
        pygame.font.init()
        self.font_large = pygame.font.Font(None, config.FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, config.FONT_SIZE_SMALL)
        
        # Pre-create gradient background surface
        self.background = self._create_gradient_background()
    
    def _create_gradient_background(self):
        """Create a sky gradient background surface"""
        background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        
        # Create gradient from light blue at top to slightly darker at bottom
        for y in range(config.SCREEN_HEIGHT):
            # Calculate color interpolation (0.0 at top, 1.0 at bottom)
            ratio = y / config.SCREEN_HEIGHT
            r = int(config.SKY_COLOR[0] * (1 - ratio * 0.3))
            g = int(config.SKY_COLOR[1] * (1 - ratio * 0.2))
            b = int(config.SKY_COLOR[2] * (1 - ratio * 0.1))
            
            # Ensure values stay within 0-255
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            
            pygame.draw.line(background, (r, g, b), (0, y), (config.SCREEN_WIDTH, y))
        
        return background
    
    def draw_game(self, bird, obstacles, score, game_state):
        """Main drawing method - renders entire game frame"""
        # Draw background
        self.screen.blit(self.background, (0, 0))
        
        # Draw obstacles (pipes)
        self._draw_obstacles(obstacles)
        
        # Draw bird
        self._draw_bird(bird)
        
        # Draw score if playing
        if game_state == config.STATE_PLAYING:
            self._draw_score(score)
        
        # Draw game over overlay if needed
        if game_state == config.STATE_GAME_OVER:
            self._draw_game_over(score)
        
        # Draw menu if in menu state
        if game_state == config.STATE_MENU:
            self._draw_menu()
    
    def _draw_obstacles(self, obstacles):
        """Draw all pipe obstacles"""
        for obstacle_rect in obstacles:
            # Draw main pipe body
            pygame.draw.rect(self.screen, config.PIPE_COLOR, obstacle_rect)
            
            # Draw highlight on left edge for 3D effect
            highlight_rect = pygame.Rect(
                obstacle_rect.x,
                obstacle_rect.y,
                5,  # Narrow highlight
                obstacle_rect.height
            )
            pygame.draw.rect(self.screen, config.PIPE_HIGHLIGHT, highlight_rect)
            
            # Draw darker right edge
            dark_rect = pygame.Rect(
                obstacle_rect.right - 3,
                obstacle_rect.y,
                3,
                obstacle_rect.height
            )
            dark_color = (
                max(0, config.PIPE_COLOR[0] - 30),
                max(0, config.PIPE_COLOR[1] - 30),
                max(0, config.PIPE_COLOR[2] - 30)
            )
            pygame.draw.rect(self.screen, dark_color, dark_rect)
    
    def _draw_bird(self, bird):
        """Draw the bird with state-based coloring"""
        rect = bird.get_rect()
        
        # Choose color based on bird state
        if bird.state == "normal":
            color = config.BIRD_COLOR
        elif bird.state == "jumping":
            color = (255, 165, 0)  # Orange for jumping
        elif bird.state == "ducking":
            color = (180, 140, 0)  # Dark yellow for ducking
        else:
            color = config.BIRD_COLOR
        
        # Draw bird body (ellipse)
        pygame.draw.ellipse(self.screen, color, rect)
        
        # Draw eye (white circle with black pupil)
        eye_x = rect.x + rect.width * 0.6
        eye_y = rect.y + rect.height * 0.3
        pygame.draw.circle(self.screen, (255, 255, 255), (int(eye_x), int(eye_y)), 5)
        pygame.draw.circle(self.screen, (0, 0, 0), (int(eye_x), int(eye_y)), 2)
        
        # Draw beak (small triangle)
        beak_points = [
            (rect.right, rect.centery),
            (rect.right + 8, rect.centery - 3),
            (rect.right + 8, rect.centery + 3)
        ]
        pygame.draw.polygon(self.screen, (255, 100, 0), beak_points)
    
    def _draw_score(self, score):
        """Draw score in top-right corner"""
        score_text = self.font_large.render(str(score), True, config.SCORE_COLOR)
        text_rect = score_text.get_rect()
        text_rect.top = 20
        text_rect.right = config.SCREEN_WIDTH - 20
        
        # Draw shadow for better visibility
        shadow_text = self.font_large.render(str(score), True, (0, 0, 0))
        shadow_rect = text_rect.copy()
        shadow_rect.x += 2
        shadow_rect.y += 2
        self.screen.blit(shadow_text, shadow_rect)
        
        # Draw main text
        self.screen.blit(score_text, text_rect)
    
    def _draw_game_over(self, score):
        """Draw game over overlay with final score and restart prompt"""
        # Semi-transparent overlay
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # Black with alpha
        self.screen.blit(overlay, (0, 0))
        
        # Game Over title
        game_over_text = self.font_large.render("GAME OVER", True, config.GAME_OVER_COLOR)
        title_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3))
        self.screen.blit(game_over_text, title_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Score: {score}", True, config.SCORE_COLOR)
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        self.screen.blit(score_text, score_rect)
        
        # Restart prompt
        restart_text = self.font_small.render("Press SPACE to restart", True, config.SCORE_COLOR)
        restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT * 2 // 3))
        self.screen.blit(restart_text, restart_rect)
    
    def _draw_menu(self):
        """Draw main menu screen"""
        # Title
        title_text = self.font_large.render("Platformer Bird", True, config.BIRD_COLOR)
        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3))
        self.screen.blit(title_text, title_rect)
        
        # Instructions
        instructions = [
            "Press SPACE to start",
            "SPACE/UP: Jump (double jump available)",
            "DOWN: Duck",
            "ESC: Quit"
        ]
        
        for i, line in enumerate(instructions):
            text = self.font_small.render(line, True, config.SCORE_COLOR)
            rect = text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + i * 30))
            self.screen.blit(text, rect)