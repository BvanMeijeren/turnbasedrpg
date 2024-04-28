import pygame
import sys
import random

from main import SCREEN_HEIGHT,SCREEN_WIDTH, WHITE, BLACK

class CombatScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.text, self.text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return True
        return False
