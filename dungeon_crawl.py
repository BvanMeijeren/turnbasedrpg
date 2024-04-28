import pygame
#import sys
import random

from player import Player
from enemy import Enemy 
from obstacle import Obstacle
from exit import Exit
#from start_menu import StartMenu
from combat import CombatScreen
from constants import *

class GridGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(0, 0)
        self.enemies = [Enemy(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(3)]
        self.obstacles = [Obstacle(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(10)]
        self.exit = self.generate_valid_exit()
        self.player_moved = False
        self.exits_reached = 0
        self.gamestate = START_MENU
        self.combat_screen = CombatScreen()

    def draw_grid(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x * GRID_SIZE, obstacle.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BROWN, obstacle_rect)
        if self.exit:
            exit_rect = pygame.Rect(self.exit.x * GRID_SIZE, self.exit.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, exit_rect)

    def draw_player(self, screen):
        player_rect = pygame.Rect(self.player.x * GRID_SIZE, self.player.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, player_rect)

    def draw_enemies(self, screen):
        for enemy in self.enemies:
            enemy_rect = pygame.Rect(enemy.x * GRID_SIZE, enemy.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLUE, enemy_rect)

    def return_to_menu(self):
        self.exits_reached = 0  # Reset the exits reached count
        self.gamestate = START_MENU

    def handle_input(self, event):
        if self.gamestate == GRID_GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.try_move_player(0, -1)  # Move up
                elif event.key == pygame.K_s:
                    self.try_move_player(0, 1)   # Move down
                elif event.key == pygame.K_a:
                    self.try_move_player(-1, 0)  # Move left
                elif event.key == pygame.K_d:
                    self.try_move_player(1, 0)   # Move right
                elif event.key == pygame.K_q:
                    self.return_to_menu()        # return to menu
        elif self.gamestate == COMBAT_SCREEN:
            self.combat_screen.handle_input(event)

    def try_move_player(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy
        if not self.is_obstacle(new_x, new_y) and 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.player.move(dx, dy)
            self.move_enemies()
            self.check_exit()
            self.player_moved = True

    def move_enemies(self):
        for enemy in self.enemies:
            enemy_x = enemy.x
            enemy_y = enemy.y
            player_x = self.player.x
            player_y = self.player.y

            dx = 0 if enemy_x == player_x else (1 if enemy_x < player_x else -1)
            dy = 0 if enemy_y == player_y else (1 if enemy_y < player_y else -1)

            new_x = enemy_x + dx
            new_y = enemy_y + dy
            if not self.is_obstacle(new_x, new_y) and 0 <= new_x < self.width and 0 <= new_y < self.height:
                enemy.move(player_x, player_y)

    def is_obstacle(self, x, y):
        for obstacle in self.obstacles:
            if obstacle.x == x and obstacle.y == y:
                return True
        return False

    def generate_valid_exit(self):
        while True:
            exit_x = random.randint(0, self.width - 1)
            exit_y = random.randint(0, self.height - 1)
            if (exit_x, exit_y) != (self.player.x, self.player.y) and not any((exit_x == obj.x and exit_y == obj.y) for obj in self.enemies + self.obstacles):
                return Exit(exit_x, exit_y)

    def check_exit(self):
        if self.player.x == self.exit.x and self.player.y == self.exit.y:
            self.exits_reached += 1
            self.player = Player(0, 0)
            self.enemies = [Enemy(random.randint(0, self.width - 1), random.randint(0, self.height - 1)) for _ in range(3)]
            self.obstacles = [Obstacle(random.randint(0, self.width - 1), random.randint(0, self.height - 1)) for _ in range(10)]
            self.exit = self.generate_valid_exit()
            if not self.exit:
                self.exit = self.generate_valid_exit()  # Regenerate the exit if it's not valid

    def check_enemy_collision(self):
        enemies_to_remove = []
        for enemy in self.enemies:
            if enemy.x == self.player.x and enemy.y == self.player.y:
                enemies_to_remove.append(enemy)
        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)
            self.gamestate = COMBAT_SCREEN
            break  # Exit loop after finding the first enemy
