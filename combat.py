import pygame
import sys
import random
from constants import *
from enemy import *
from player import Player


class CombatScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player

    def draw_text(self, screen):
        screen.fill(BLACK)
        screen.blit(self.text, self.text_rect)

    def handle_input(self, event):
        gamestate = COMBAT_SCREEN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gamestate = GRID_GAME
            # if event.key == pygame.K_1:
            #     se
            elif event.key == pygame.K_q:
                gamestate = START_MENU
        return gamestate

    def run(self):
        self.draw_text(self.screen)
