import pygame
import sys
import random
from constants import *

from constants import SCREEN_HEIGHT,SCREEN_WIDTH, WHITE, BLACK

class CombatScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.text, self.text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # return to grid game TO DO
                self.try_move_player(0, -1)  # Move up
            elif event.key == pygame.K_q:
                return START_MENU
        return COMBAT_SCREEN

    def run(self):
        self.draw(self.screen)
