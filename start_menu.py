import pygame
import sys
import random

from constants import *

class StartMenu:
    def __init__(self):
        self.gamestate = START_MENU  # Initialize gamestate attribute
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Welcome to Bastiaan's silly little game!", True, WHITE)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.start_text = self.font.render("Press Space to Start", True, WHITE)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self, screen):
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_text, self.start_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:  # Check for keydown event
            if event.key == pygame.K_SPACE:
                print("you pressed SPACE")
                return GRID_GAME  # Return gamestate if spacebar is pressed
        return START_MENU  # Return default gamestate otherwise
