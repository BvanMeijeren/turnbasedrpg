# game_manager.py
import pygame
import sys

from start_menu import StartMenu
from dungeon_crawl import GridGame
from combat import CombatScreen
from character_creation import CharacterCreation
from constants import *
from characters import Character
from weapons import *

class GameManager:
    def __init__(self):
        pygame.init()

        # default player settings until player creation menu
        self.player = Character(x=0, 
                                y=0, 
                                name="Bas", 
                                level=1, 
                                xp=0,
                                hitpoints=50, 
                                max_hitpoints=50,
                                critical_chance=0.05, 
                                critical_multiplier=1.5,
                                species="Human", 
                                fire_def=100,
                                ice_def=100,
                                electricity_def=100,
                                skills='Fireball', # should be set to skills, firebal is just for testing 
                                items=None,
                                equipped_weapon=create_starterweapon(),
                                profession="Knight"
                                )
        self.start_menu = StartMenu()
        self.character_creation = CharacterCreation(player = self.player)
        self.grid_game = GridGame(GRID_WIDTH, GRID_HEIGHT, player = self.player)
        self.combat_screen = CombatScreen(player = self.player)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.gamestate= START_MENU # initial gamestate

    ### Global Input handler function ###
    def handle_input(self, event):
        if self.gamestate == START_MENU:
            #print("Input handler: start menu")
            self.gamestate = self.start_menu.handle_input(event)
        elif self.gamestate == CHARACTER_CREATION:
            #print("Input handler: character creation")
            self.gamestate = self.character_creation.handle_input(event)
        elif self.gamestate == GRID_GAME:
            #print("Input handler: dungeon crawl")
            self.gamestate = self.grid_game.handle_input(event)
        elif self.gamestate == COMBAT_SCREEN:
            #print("Input handler: combat")
            self.gamestate = self.combat_screen.handle_input(event)

    ### Global Render function, determines page visibility ###
    def gamestate_coordinator(self):
        self.screen.fill(BLACK)
        if self.gamestate == START_MENU:
            self.start_menu.draw(self.screen)
        elif self.gamestate == CHARACTER_CREATION:
            self.character_creation.run()
        elif self.gamestate == GRID_GAME:
            self.grid_game.run()
        elif self.gamestate == COMBAT_SCREEN:
            self.combat_screen.run()
        pygame.display.flip()

    ### Core run function ###
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)  # Pass event to handle_input
            self.gamestate_coordinator()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()
