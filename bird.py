import pygame
import config


class Bird:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = config.BIRD_X
        self.y = config.SCREEN_HEIGHT // 2
        self.velocity_y = 0
        self.jumps_remaining = config.MAX_JUMPS
        self.is_ducking = False
        self._height = config.BIRD_HEIGHT

    def jump(self):
        if self.jumps_remaining > 0:
            self.velocity_y = config.BIRD_JUMP_VELOCITY
            self.jumps_remaining -= 1

    def duck(self):
        if not self.is_ducking:
            self.is_ducking = True
            self._height = config.BIRD_DUCK_HEIGHT
            # Pin bottom edge so bird shrinks upward
            self.y += (config.BIRD_HEIGHT - config.BIRD_DUCK_HEIGHT)

    def unduck(self):
        if self.is_ducking:
            # Restore height, pin bottom edge back
            self.y -= (config.BIRD_HEIGHT - config.BIRD_DUCK_HEIGHT)
            self._height = config.BIRD_HEIGHT
            self.is_ducking = False

    def update(self, dt):
        # Apply gravity
        self.velocity_y += config.GRAVITY * dt
        if self.velocity_y > config.MAX_FALL_SPEED:
            self.velocity_y = config.MAX_FALL_SPEED
        self.y += self.velocity_y * dt

        # Reset jumps when falling downward
        if self.velocity_y >= 0:
            self.jumps_remaining = config.MAX_JUMPS

    def get_rect(self):
        return pygame.Rect(self.x, int(self.y), config.BIRD_WIDTH, self._height)
