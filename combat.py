import pygame
import sys
import random
from constants import *
from enemy import *
from ui_selection_menu import *

class CombatScreen:
    def __init__(self, player):
        self.font = pygame.font.Font(None, 36)
        self.screen = screen
        self.player = player

        # UI elements
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 400) ))

        self.action_types = ['Attack', 'Spells', 'Items']
        self.selected_action_type = 0
        self.selected_action = 0
        self.has_selected_action_type = False
        self.has_selected_action = False
        self.combat_ongoing = True

    def draw_visuals(self, screen):
        screen.fill(BLACK)

        # visualize texts
        screen.blit(self.text, self.text_rect)

        # scale images
        player_image = pygame.transform.scale(self.player.image, (SCREEN_WIDTH*0.2, SCREEN_WIDTH*0.2))

        # Load images
        self.screen.blit(player_image, (0, SCREEN_HEIGHT*0.3))

    def draw_combat_menu(self, screen):
        selection_menu(
            self=self,
            attribute=self.selected_action_type,
            title="What will you do?",
            options=self.action_types
        )
        if self.selected_action_type == 'Spells':
            selection_menu(
                self=self,
                attribute=self.selected_action,
                title="What will you do?",
                options=self.player.skills
            )

    def handle_input(self, event):
        gamestate = COMBAT_SCREEN
        if event.type == pygame.KEYDOWN:

            #selection buttons w and s
            if event.key == pygame.K_w:
                if self.combat_ongoing and self.selected_action_type > 0:
                    self.selected_action_type -= 1
                elif not self.combat_ongoing and self.selected_action > 0:
                    self.selected_action -= 1
            elif event.key == pygame.K_s:
                if self.combat_ongoing and self.selected_action_type < len(self.action_types) - 1:
                    self.selected_action_type += 1
                elif not self.combat_ongoing and self.selected_action < len(self.skills) - 1:
                    self.selected_action += 1

            # escape to start menu
            elif event.key == pygame.K_ESCAPE:
                gamestate = START_MENU

            # SPACE
            elif event.key == pygame.K_SPACE:
                if self.combat_ongoing == False:
                    if self.has_selected_action_type == False:
                        self.has_selected_action_type == True 
                    elif self.has_selected_action == False:
                        self.has_selected_action = True
                else:
                    gamestate = GRID_GAME
        return gamestate

    def run(self):
        self.draw_visuals(self.screen)
        self.draw_combat_menu(self.screen)
