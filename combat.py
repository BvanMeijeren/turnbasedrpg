import pygame
import sys
import random
from constants import *
from enemy import *
from ui_widgets import *
from backgrounds import choose_combat_background
from skills import *

class CombatScreen:
    def __init__(self, player):
        self.font = font_normal
        self.screen = screen
        self.player = player
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

        enemy_names = ''
        for enemy in self.player.encountered_enemies:
            enemy_names = enemy_names + enemy.name

        enemy_names = enemy_names + '!'

        # visualize texts
        self.text = self.font.render("You are attacked by" + enemy_names, True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 400) ))
        screen.blit(self.text, self.text_rect)

        # show player image
        player_image = pygame.transform.scale(self.player.image, (SCREEN_WIDTH*0.2, SCREEN_WIDTH*0.2))
        self.screen.blit(player_image, (SCREEN_WIDTH*0.1, SCREEN_HEIGHT*0.3) )

        # show enemy image
        if self.player.encountered_enemies:
            enemy = self.player.encountered_enemies[0]
            enemy_image = pygame.transform.scale(enemy.image, (SCREEN_WIDTH * 0.2, SCREEN_WIDTH * 0.2) )
            self.screen.blit(enemy_image, ((SCREEN_WIDTH*0.75), (SCREEN_HEIGHT*0.15) ) )

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
            # execute player action
            print('select action type: ' + str(self.selected_action_type) )
            if self.selected_action_type == 0:
                attack(self.player, self.player.encountered_enemies[0])
            elif self.selected_action_type == 1:
                chosen_spell = all_spells[self.selected_action]
                if chosen_spell:
                    chosen_spell(self.player, self.player.encountered_enemies[0])
                else:
                    print('Spell not found')

            print('enemy HP remaining: ' + str(self.player.encountered_enemies[0].hitpoints) )

            # reset variable for next player turn
            self.has_selected_action_type = False
            self.has_selected_action = False

            # check if player died:
            print('player HP is ' + str(self.player.hitpoints) ) 
            if self.player.hitpoints <= 0:
                centered_popup(
                    r = 139,
                    g = 69,
                    b = 19,
                    transparency = 90,
                    width = 800,
                    height = 800,
                    text = 'YOU DIED!'
                )

            # enemy turn
            self.enemy_turn()

    def run(self):
        self.draw_visuals(self.screen)
        self.draw_combat_menu(self.screen)
        player_status_menu(self, self.screen)
        self.player_turn()
        pygame.display.flip()
