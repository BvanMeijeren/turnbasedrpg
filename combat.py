import pygame
import sys
import random
from constants import *
from enemy import *

class CombatScreen:
    def __init__(self,player):
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = player

        # UI elements
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw_text(self, screen):
        screen.fill(BLACK)

        # visualize texts
        screen.blit(self.text, self.text_rect)

        # scale images
        player_image = pygame.transform.scale(self.player.image, (SCREEN_WIDTH*0.2, SCREEN_WIDTH*0.2))

        # Load images
        self.screen.blit(player_image, (0, SCREEN_HEIGHT*0.3))

    def handle_input(self, event):
        gamestate = COMBAT_SCREEN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gamestate = GRID_GAME
            # if event.key == pygame.K_1:
            #     se
            elif event.key == pygame.K_ESCAPE:
                gamestate = START_MENU
        return gamestate

    def run(self):
        self.draw_text(self.screen)
