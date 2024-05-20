import pygame
import sys
import random

from constants import *
from ui_widgets import centered_popup
from backgrounds import choose_combat_background

class StartMenu:
    def __init__(self):
        self.bigfont = pygame.font.Font(None, 70)
        self.smallfont = pygame.font.Font(None, 36)
        self.title = self.bigfont.render("Dreadworld", True, BLACK)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.start_text = self.smallfont.render("Press SPACE to start creating a character, ESCAPE to quit.", True, BLACK)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:  # Check for keydown event
            if event.key == pygame.K_SPACE:
                return CHARACTER_CREATION  # Return gamestate if spacebar is pressed
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        return START_MENU  # Return default gamestate otherwise
    
    def draw(self, screen):
        # Load background image
        background_image = choose_combat_background('Forest') # hardcoded forest texture for start menu
        #background_image = pygame.image.load("graphics/forest.jpg").convert()
        screen.blit(background_image, (0, 0))

        # add square
        centered_popup(
            r=92,
            g=64,
            b=51,
            transparency=220,
            width=800,
            height=500,
            text = ''
        )

        # Intro text
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_text, self.start_rect)
