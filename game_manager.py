# game_manager.py
import pygame
import sys

from start_menu import StartMenu
from dungeon_crawl import GridGame
from combat import CombatScreen
from constants import *

class GameManager:
    def __init__(self):
        pygame.init()
        self.start_menu = StartMenu()
        self.grid_game = GridGame(GRID_WIDTH, GRID_HEIGHT)
        self.combat_screen = CombatScreen()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gamestate= START_MENU

    ### Global Input handler function ###
    def handle_input(self, event):
        if self.gamestate == START_MENU:
            self.gamestate = self.start_menu.handle_input(event)
        elif self.gamestate == GRID_GAME:
            self.gamestate = self.grid_game.handle_input(event)
        elif self.gamestate == COMBAT_SCREEN:
            self.gamestate = self.combat_screen.handle_input(event)

    def update(self):
        if self.grid_game:
            has_colliding_enemies = self.grid_game.check_enemy_collision()
            print(str(has_colliding_enemies))
            if has_colliding_enemies:
                self.gamestate = COMBAT_SCREEN

    def render(self):
        self.screen.fill(BLACK)
        if self.gamestate == START_MENU:
            self.start_menu.draw(self.screen)
        elif self.gamestate == GRID_GAME:
            self.grid_game.run()
        elif self.gamestate == COMBAT_SCREEN:
            self.combat_screen.run()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)  # Pass event to handle_input
            self.update()
            self.render()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()
