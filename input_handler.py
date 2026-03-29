import pygame
import config


class InputHandler:
    def __init__(self):
        # Track duck key state for continuous ducking
        self.duck_key_held = False
    
    def process_events(self, events, game_state):
        """
        Process pygame events and return semantic actions.
        
        Args:
            events: List of pygame events
            game_state: Current game state (STATE_MENU, STATE_PLAYING, STATE_GAME_OVER)
            
        Returns:
            list: List of action strings
        """
        actions = []
        
        for event in events:
            if event.type == pygame.QUIT:
                actions.append("QUIT")
            
            elif event.type == pygame.KEYDOWN:
                # Jump keys (SPACE or UP)
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    if game_state == config.STATE_MENU:
                        actions.append("START")
                    elif game_state == config.STATE_PLAYING:
                        actions.append("JUMP")
                    elif game_state == config.STATE_GAME_OVER:
                        # In game over, SPACE also restarts for convenience
                        actions.append("RESTART")
                
                # Duck key (DOWN)
                elif event.key == pygame.K_DOWN:
                    if game_state == config.STATE_PLAYING:
                        actions.append("DUCK")
                        self.duck_key_held = True
                
                # Restart key (R)
                elif event.key == pygame.K_r:
                    if game_state == config.STATE_GAME_OVER:
                        actions.append("RESTART")
                
                # Quit key (ESC)
                elif event.key == pygame.K_ESCAPE:
                    actions.append("QUIT")
            
            elif event.type == pygame.KEYUP:
                # Unduck when DOWN key is released
                if event.key == pygame.K_DOWN:
                    if game_state == config.STATE_PLAYING and self.duck_key_held:
                        actions.append("UNDUCK")
                        self.duck_key_held = False
        
        return actions
    
    def reset(self):
        """Reset input handler state"""
        self.duck_key_held = False