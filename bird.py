import pygame
import config


class Bird:
    def __init__(self):
        # Initial position: left side of screen, vertically centered
        self.x = 100
        self.y = config.SCREEN_HEIGHT // 2
        
        # Velocity components
        self.vx = 0
        self.vy = 0
        
        # Dimensions
        self.width = 40
        self.height = 30
        
        # State machine: normal, jumping, ducking
        self.state = "normal"
        
        # Double jump tracking
        self.jumps_remaining = 2
        
        # Store normal height for unducking
        self.normal_height = self.height
        self.duck_height = self.height // 2
    
    def update(self, dt):
        """Apply physics and update position"""
        # Apply gravity
        self.vy += config.GRAVITY
        
        # Update position
        self.y += self.vy
        
        # Keep bird within screen boundaries
        if self.y < 0:
            self.y = 0
            self.vy = 0
        elif self.y + self.height > config.SCREEN_HEIGHT:
            self.y = config.SCREEN_HEIGHT - self.height
            self.vy = 0
            # Reset jumps when hitting bottom (landing)
            self.jumps_remaining = 2
            if self.state == "jumping":
                self.state = "normal"
        
        # Update state based on velocity
        if self.state == "jumping" and self.vy >= 0:
            self.state = "normal"
    
    def jump(self):
        """Handle jump with double jump capability"""
        if self.jumps_remaining > 0:
            # If ducking, unduck first (restores normal height and sets state to normal)
            # This MUST happen before setting state to 'jumping' so that unduck() can
            # properly detect the ducking state and restore the bird's normal height
            if self.state == "ducking":
                self.unduck()
            
            # Apply jump impulse (negative because up is negative y)
            self.vy = config.JUMP_FORCE
            self.jumps_remaining -= 1
            self.state = "jumping"
    
    def duck(self):
        """Reduce hitbox height by 50% while keeping bottom edge fixed"""
        if self.state != "ducking":
            # Store current bottom position
            bottom = self.y + self.height
            
            # Reduce height
            self.height = self.duck_height
            
            # Adjust y to keep bottom edge fixed
            self.y = bottom - self.height
            
            self.state = "ducking"
    
    def unduck(self):
        """Return to normal height"""
        if self.state == "ducking":
            # Store current bottom position
            bottom = self.y + self.height
            
            # Restore normal height
            self.height = self.normal_height
            
            # Adjust y to keep bottom edge fixed
            self.y = bottom - self.height
            
            self.state = "normal"
    
    def get_rect(self):
        """Return current collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
