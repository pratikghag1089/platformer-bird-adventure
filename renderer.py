import pygame
import config


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, config.FONT_SIZE)
        self.large_font = pygame.font.SysFont(None, config.FONT_SIZE * 2)

    def draw_game(self, bird, obstacles, score, game_state):
        """Main draw entry point — dispatches based on game state."""
        self.screen.fill(config.COLOR_SKY)

        if game_state == "MENU":
            self._draw_menu()
        elif game_state == "PLAYING":
            self._draw_obstacles(obstacles)
            self._draw_bird(bird)
            self._draw_score(score)
        elif game_state == "GAME_OVER":
            self._draw_obstacles(obstacles)
            self._draw_bird(bird)
            self._draw_score(score)
            self._draw_game_over_overlay(score)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _draw_bird(self, bird):
        rect = bird.get_rect()
        color = config.COLOR_BIRD
        if bird.is_ducking:
            color = config.COLOR_BIRD_DUCK
        elif bird.velocity_y < 0:
            color = config.COLOR_BIRD_JUMP
        pygame.draw.rect(self.screen, color, rect)
        # Eye
        eye_x = rect.right - 6
        eye_y = rect.top + 6
        pygame.draw.circle(self.screen, config.COLOR_EYE, (eye_x, eye_y), 3)

    def _draw_obstacles(self, obstacles):
        for obs in obstacles:
            top_rect = pygame.Rect(obs["x"], 0, config.OBSTACLE_WIDTH, obs["gap_y"])
            bottom_rect = pygame.Rect(
                obs["x"],
                obs["gap_y"] + config.OBSTACLE_GAP,
                config.OBSTACLE_WIDTH,
                config.SCREEN_HEIGHT - (obs["gap_y"] + config.OBSTACLE_GAP),
            )
            pygame.draw.rect(self.screen, config.COLOR_PIPE, top_rect)
            pygame.draw.rect(self.screen, config.COLOR_PIPE, bottom_rect)
            # Pipe lips
            lip_h = 8
            pygame.draw.rect(
                self.screen,
                config.COLOR_PIPE_DARK,
                (obs["x"] - 4, obs["gap_y"] - lip_h, config.OBSTACLE_WIDTH + 8, lip_h),
            )
            pygame.draw.rect(
                self.screen,
                config.COLOR_PIPE_DARK,
                (
                    obs["x"] - 4,
                    obs["gap_y"] + config.OBSTACLE_GAP,
                    config.OBSTACLE_WIDTH + 8,
                    lip_h,
                ),
            )

    def _draw_score(self, score):
        text = self.font.render(f"Score: {score}", True, config.COLOR_TEXT)
        rect = text.get_rect(topright=(config.SCREEN_WIDTH - 16, 16))
        self.screen.blit(text, rect)

    def _draw_menu(self):
        title = self.large_font.render("Platformer Bird", True, config.COLOR_TEXT)
        prompt = self.font.render("Press SPACE to start", True, config.COLOR_TEXT)
        title_rect = title.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3))
        prompt_rect = prompt.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        self.screen.blit(title, title_rect)
        self.screen.blit(prompt, prompt_rect)

    def _draw_game_over_overlay(self, score):
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill(config.COLOR_OVERLAY)
        self.screen.blit(overlay, (0, 0))

        go_text = self.large_font.render("Game Over", True, config.COLOR_TEXT)
        score_text = self.font.render(f"Final Score: {score}", True, config.COLOR_TEXT)
        restart_text = self.font.render("Press R to restart", True, config.COLOR_TEXT)

        go_rect = go_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3))
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT * 2 // 3))

        self.screen.blit(go_text, go_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
