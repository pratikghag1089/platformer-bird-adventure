import pygame
import config


class Renderer:
    """Handles all drawing operations for the game."""

    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, config.FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, config.FONT_SIZE_SMALL)

    def draw(self, game_state, bird, obstacles, score):
        """Main draw call - renders entire frame based on current game state."""
        self.screen.fill(config.SKY_COLOR)

        # Draw obstacles (pipes)
        for obstacle in obstacles:
            self._draw_pipe(obstacle.top_rect, is_top=True)
            self._draw_pipe(obstacle.bottom_rect, is_top=False)

        # Draw bird
        self._draw_bird(bird)

        # Draw HUD
        self._draw_score(score)

        # Draw overlays based on game state
        if game_state == config.STATE_GAME_OVER:
            self._draw_game_over(score)
        elif game_state == config.STATE_MENU:
            self._draw_menu()

    def _draw_pipe(self, pipe_rect, is_top):
        """Draw a single pipe with highlight accent."""
        pygame.draw.rect(self.screen, config.PIPE_COLOR, pipe_rect)
        # Highlight strip on left edge
        highlight_rect = pygame.Rect(pipe_rect.x, pipe_rect.y, 10, pipe_rect.height)
        pygame.draw.rect(self.screen, config.PIPE_HIGHLIGHT, highlight_rect)

    def _draw_bird(self, bird):
        """Draw the bird with color based on current state."""
        bird_rect = bird.get_rect()

        # Select color based on bird state
        if bird.state == 'jumping':
            color = config.BIRD_JUMP_COLOR
        elif bird.state == 'ducking':
            color = config.BIRD_DUCK_COLOR
        else:
            color = config.BIRD_COLOR

        # Draw bird body
        pygame.draw.rect(self.screen, color, bird_rect)
        # Draw outline
        pygame.draw.rect(self.screen, (0, 0, 0), bird_rect, 2)

    def _draw_score(self, score):
        """Draw current score in top-right corner."""
        score_text = self.font_small.render(f"Score: {score}", True, config.SCORE_COLOR)
        score_rect = score_text.get_rect(topright=(config.SCREEN_WIDTH - 20, 20))
        self.screen.blit(score_text, score_rect)

    def _draw_game_over(self, score):
        """Draw game over overlay with final score and restart prompt."""
        # Semi-transparent overlay
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))

        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, config.GAME_OVER_COLOR)
        game_over_rect = game_over_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, game_over_rect)

        # Final score
        score_text = self.font_medium.render(f"Final Score: {score}", True, config.SCORE_COLOR)
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 20))
        self.screen.blit(score_text, score_rect)

        # Restart prompt
        restart_text = self.font_small.render("Press R to restart (SPACE also works)", True, config.SCORE_COLOR)
        restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(restart_text, restart_rect)

    def _draw_menu(self):
        """Draw main menu screen."""
        title_text = self.font_large.render("Platformer Bird Adventure", True, config.BIRD_COLOR)
        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(title_text, title_rect)

        start_text = self.font_small.render("Press SPACE to Start", True, config.SCORE_COLOR)
        start_rect = start_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2 + 30))
        self.screen.blit(start_text, start_rect)
