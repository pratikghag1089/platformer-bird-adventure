import config


def check_obstacles(bird_rect, obstacles):
    """Return True if bird_rect overlaps any pipe rect."""
    for obs in obstacles:
        top_rect = _rect(0, obs["x"], obs["gap_y"])
        bottom_rect = _rect(
            1,
            obs["x"],
            obs["gap_y"] + config.OBSTACLE_GAP,
            config.SCREEN_HEIGHT - (obs["gap_y"] + config.OBSTACLE_GAP),
        )
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            return True
    return False


def check_boundaries(bird_rect, screen_h):
    """Return True if bird is outside vertical bounds."""
    return bird_rect.top < 0 or bird_rect.bottom > screen_h


def _rect(which, x, y, h=None):
    """Build a pipe rect. which=0 top, which=1 bottom."""
    import pygame
    if which == 0:
        return pygame.Rect(x, 0, config.OBSTACLE_WIDTH, y)
    else:
        return pygame.Rect(x, y, config.OBSTACLE_WIDTH, h)
