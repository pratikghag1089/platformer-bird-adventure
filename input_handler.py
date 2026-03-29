import pygame


class InputHandler:
    def process_events(self, events, game_state):
        actions = []
        for event in events:
            if event.type == pygame.QUIT:
                actions.append("QUIT")

            elif event.type == pygame.KEYDOWN:
                if game_state == "MENU":
                    if event.key == pygame.K_SPACE:
                        actions.append("START")
                    elif event.key == pygame.K_ESCAPE:
                        actions.append("QUIT")

                elif game_state == "PLAYING":
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        actions.append("JUMP")
                    elif event.key == pygame.K_DOWN:
                        actions.append("DUCK")
                    elif event.key == pygame.K_ESCAPE:
                        actions.append("QUIT")

                elif game_state == "GAME_OVER":
                    if event.key == pygame.K_r:
                        actions.append("RESTART")
                    elif event.key == pygame.K_ESCAPE:
                        actions.append("QUIT")

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN and game_state == "PLAYING":
                    actions.append("UNDUCK")

        return actions
