import pygame
import config


def check_obstacles(bird_rect, obstacles):
    """
    Check collision between bird and obstacle rectangles.
    
    Args:
        bird_rect: pygame.Rect of the bird
        obstacles: list of pygame.Rect for all pipe segments
    
    Returns:
        bool: True if collision detected
    """
    for obstacle_rect in obstacles:
        if bird_rect.colliderect(obstacle_rect):
            return True
    return False


def check_boundaries(bird_rect, screen_h):
    """
    Check collision with screen top/bottom boundaries.
    
    Args:
        bird_rect: pygame.Rect of the bird
        screen_h: screen height in pixels
    
    Returns:
        bool: True if bird is outside boundaries
    """
    # Check top boundary
    if bird_rect.top < 0:
        return True
    
    # Check bottom boundary
    if bird_rect.bottom > screen_h:
        return True
    
    return False