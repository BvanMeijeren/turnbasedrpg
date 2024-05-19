import pygame
import sys
import random
from constants import *
from enemy import *
from ui_widgets import *
from backgrounds import choose_combat_background

class CombatScreen:
    def __init__(self, player):
        self.font = pygame.font.Font(None, 36)
        self.screen = screen
        self.player = player
        self.encountered_enemies = player.encountered_enemies
        self.action_types = ['Attack', 'Spells', 'Items']
        self.skills = ['Fireball', 'Ice Shard']
        self.selected_action_type = 0
        self.selected_action = 0
        self.has_selected_action_type = False
        self.has_selected_action = False
        self.combat_ongoing = True

    def draw_visuals(self, screen):
        # draw background
        background_image = choose_combat_background('Forest')
        screen.blit(background_image, (0, 0))
        #screen.fill(BLACK)

        print('encountering nr of enemies: ' + str(len(self.encountered_enemies)) )
        enemy_names = ''
        for enemy in self.encountered_enemies:
            enemy_names = enemy_names + 'and a ' + enemy.name

        enemy_names = enemy_names + '!'

        # visualize texts
        self.text = self.font.render("You are attacked by" + enemy_names, True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 400) ))
        screen.blit(self.text, self.text_rect)

        # scale images
        player_image = pygame.transform.scale(self.player.image, (SCREEN_WIDTH*0.2, SCREEN_WIDTH*0.2))

        # Load images
        self.screen.blit(player_image, (SCREEN_WIDTH*0.1, SCREEN_HEIGHT*0.3))

    def draw_combat_menu(self, screen):
        if self.has_selected_action_type == False:
            selection_menu(
                self=self,
                attribute=self.selected_action_type,
                title="What will you do?",
                options=self.action_types
            )
        if self.selected_action_type == 1 and self.has_selected_action_type:
            selection_menu(
                self=self,
                attribute=self.selected_action,
                title="What will you do?",
                options=self.skills
            )

        pygame.display.flip()


    def handle_input(self, event):
        gamestate = COMBAT_SCREEN
        if event.type == pygame.KEYDOWN:

            #selection buttons w and s
            if event.key == pygame.K_w:
                if not self.has_selected_action_type and self.selected_action_type > 0:
                    self.selected_action_type -= 1
                elif self.has_selected_action_type and self.selected_action > 0:
                    self.selected_action -= 1

            elif event.key == pygame.K_s:
                if  not self.has_selected_action_type and self.selected_action_type < len(self.action_types) - 1:
                    self.selected_action_type += 1
                elif self.has_selected_action_type and  self.selected_action < len(self.skills) - 1:
                    self.selected_action += 1

            # escape to start menu
            elif event.key == pygame.K_ESCAPE:
                gamestate = START_MENU

            # SPACE
            elif event.key == pygame.K_SPACE:
                if self.combat_ongoing == True and self.has_selected_action_type == False:
                    self.has_selected_action_type = True 
                elif self.combat_ongoing == True and self.has_selected_action_type == True:
                    self.has_selected_action = True
                else:
                    gamestate = GRID_GAME
        return gamestate
    
 
    def enemy_turn(self):
        self.player.hitpoints = self.player.hitpoints - 20
        print('enemy turn')


    def player_turn(self):
        if self.has_selected_action_type == True and self.has_selected_action == True:
            self.has_selected_action_type = False
            self.has_selected_action = False
            self.enemy_turn()

    def run(self):
        self.draw_visuals(self.screen)
        self.draw_combat_menu(self.screen)
        player_status_menu(self)
        self.player_turn()
