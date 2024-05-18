import pygame
import sys
import random

from constants import *
from ui_selection_menu import *

class CharacterCreation:
    def __init__(self, player):
        pygame.display.set_caption("Character Creation")
        self.font = pygame.font.Font(None, 36)
        self.screen = screen
        self.selected_profession = 0
        self.selected_race = 0
        self.player = player

        self.classes = ["Knight", "Mage", "Rogue"]
        self.races = ["Human", "Elf", "Dwarf"]

        self.still_creating_character = True

    def give_player_profession(self, profession):
        # update player object with chosen profession
        self.player.profession = self.classes[profession]
        
        # Update player sprite accroding to selected profession
        if self.player.profession == 'Knight':
            self.player.image = pygame.image.load("graphics/knight.png").convert_alpha()
        elif self.player.profession == 'Mage':
            self.player.image = pygame.image.load("graphics/wizard.png").convert_alpha()
        elif self.player.profession == 'Rogue':
            self.player.image = pygame.image.load("graphics/thief.png").convert_alpha()

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
            selection_menu(
                self=self, 
                attribute= self.selected_profession,
                title="Select your class:", 
                options=self.classes
                )
        else:
            selection_menu(
                self=self,
                attribute=self.selected_race,
                title="Select your race:",
                options=self.races
            )

        pygame.display.flip()

    def run(self):
        self.render(self.screen)
        self.give_player_profession(self.selected_profession)



