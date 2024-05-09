import pygame
import sys
import random

from constants import *

class CharacterCreation:
    def __init__(self, player):
        pygame.display.set_caption("Character Creation")
        self.font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.selected_profession = 0
        self.selected_race = 0
        self.player = player

        self.classes = ["Knight", "Mage", "Rogue"]
        self.races = ["Human", "Elf", "Dwarf"]

        self.still_creating_character = True

    def give_player_profession(self, profession):
        # update player object with chosen profession
        self.player.profession = self.classes[profession]
        #print("Chosen profession: " + self.classes[profession])

    def handle_input(self, event):
        gamestate = CHARACTER_CREATION
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.still_creating_character and self.selected_profession > 0:
                    self.selected_profession -= 1
                elif not self.still_creating_character and self.selected_race > 0:
                    self.selected_race -= 1
            elif event.key == pygame.K_s:
                if self.still_creating_character and self.selected_profession < len(self.classes) - 1:
                    self.selected_profession += 1
                elif not self.still_creating_character and self.selected_race < len(self.races) - 1:
                    self.selected_race += 1
            elif event.key == pygame.K_SPACE:
                if self.still_creating_character:
                    self.still_creating_character = False
                else:
                    return GRID_GAME

        return gamestate
         



    def render(self, screen):
        #print("blacken the screen")
        # screen.fill(BLACK)

        # Load background image
        background_image = pygame.image.load("graphics/forest.jpg").convert()
        screen.blit(background_image, (0, 0))

        if self.still_creating_character:
            select_text = self.font.render("Select Class:", True, WHITE)
            select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(select_text, select_rect)

            for i, class_name in enumerate(self.classes):
                text_color = RED if self.selected_profession == i else WHITE
                class_option_text = self.font.render(class_name, True, text_color)
                class_option_rect = class_option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 * (i + 1)))
                screen.blit(class_option_text, class_option_rect)
        else:
            select_text = self.font.render("Select Race:", True, WHITE)
            select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(select_text, select_rect)

            for i, race_name in enumerate(self.races):
                text_color = RED if self.selected_race == i else WHITE
                race_option_text = self.font.render(race_name, True, text_color)
                race_option_rect = race_option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 * (i + 1)))
                screen.blit(race_option_text, race_option_rect)

        pygame.display.flip()

    def run(self):
        self.render(self.screen)
        self.give_player_profession(self.selected_profession)


