import pygame
import sys
import random

from constants import *

class StartMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Welcome to Bastiaan's silly little game!", True, BLACK)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.start_text = self.font.render("Press Space to Start", True, BLACK)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:  # Check for keydown event
            if event.key == pygame.K_SPACE:
                print("you pressed SPACE")
                return GRID_GAME  # Return gamestate if spacebar is pressed
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        return START_MENU  # Return default gamestate otherwise
    
    def draw(self, screen):
        # Load background image
        background_image = pygame.image.load("graphics/forest.jpg").convert()
        screen.blit(background_image, (0, 0))

        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_text, self.start_rect)
