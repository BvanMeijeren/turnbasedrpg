import pygame
import sys
import random

from start_menu import StartMenu
from dungeon_crawl import GridGame
#from combat import CombatScreen
from constants import *

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_page = StartMenu()
        self.grid_game = GridGame(GRID_WIDTH, GRID_HEIGHT)

    def handle_input(self, event):
        if self.grid_game.gamestate == START_MENU:
            self.grid_game.gamestate = self.current_page.handle_input(event)
        elif self.grid_game.gamestate == GRID_GAME:
            self.grid_game.handle_input(event)
        elif self.grid_game.gamestate == COMBAT_SCREEN:
            if self.grid_game.combat_screen.handle_input(event):
                self.grid_game.gamestate = GRID_GAME

    def update(self):
        self.grid_game.check_enemy_collision()

    def render(self):
        self.screen.fill(BLACK)
        if self.grid_game.gamestate == START_MENU:
            self.current_page.draw(self.screen)
        elif self.grid_game.gamestate == GRID_GAME:
            self.grid_game.draw_grid(self.screen)
            self.grid_game.draw_enemies(self.screen)
            self.grid_game.draw_player(self.screen)
        elif self.grid_game.gamestate == COMBAT_SCREEN:
            self.grid_game.combat_screen.draw(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)
            self.update()
            self.render()
            self.clock.tick(10)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    game = Main()
    game.run()
