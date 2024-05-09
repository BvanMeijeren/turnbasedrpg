# grid_game.py
import pygame
import random

#from player import Player
from enemy import Enemy 
from obstacle import Obstacle
from exit import Exit
from constants import *
from characters import Character

class GridGame:
    def __init__(self, grid_width, grid_height, player):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.player = player
        self.enemies = [Enemy(random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)) for _ in range(3)]
        self.obstacles = [Obstacle(random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)) for _ in range(10)]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.exit = self.generate_valid_exit()
        self.player_moved = False
        self.exits_reached = 0

        # Load the enemy image
        self.enemy_image = pygame.image.load("graphics/goblin.png")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (GRID_SIZE, GRID_SIZE))

        # Load player image
        self.player_image = self.player.image
        self.player_image = pygame.transform.scale(self.player_image, (GRID_SIZE, GRID_SIZE))

    #### Grid game drawing function ####
    def draw_grid(self, screen):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x * GRID_SIZE, obstacle.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BROWN, obstacle_rect)
        if self.exit:
            exit_rect = pygame.Rect(self.exit.x * GRID_SIZE, self.exit.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, exit_rect)

    def draw_player(self, screen):
        # Calculate the position to blit the enemy image
        player_rect = self.player_image.get_rect(topleft=(self.player.x * GRID_SIZE, self.player.y * GRID_SIZE))
        # Blit the enemy image onto the screen
        screen.blit(self.player_image, player_rect)

    def draw_enemies(self, screen):
        for enemy in self.enemies:
            # Calculate the position to blit the enemy image
            enemy_rect = self.enemy_image.get_rect(topleft=(enemy.x * GRID_SIZE, enemy.y * GRID_SIZE))
            # Blit the enemy image onto the screen
            screen.blit(self.enemy_image, enemy_rect)

    ### quite to menu ###
    def return_to_menu(self):
        self.exits_reached = 0  # Reset the exits reached count

    ### input handler ###
    def handle_input(self, event):
        gamestate = GRID_GAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.try_move_player(0, -1)  # Move up
            elif event.key == pygame.K_s:
                self.try_move_player(0, 1)   # Move down
            elif event.key == pygame.K_a:
                self.try_move_player(-1, 0)  # Move left
            elif event.key == pygame.K_d:
                self.try_move_player(1, 0)   # Move right
            elif event.key == pygame.K_ESCAPE:
                print("pressed Q")
                gamestate = START_MENU       # return to menu
        
        if self.check_enemy_collision() > 0:
            gamestate = COMBAT_SCREEN
        
        return gamestate

    ### placement & movement functions ###
    def try_move_player(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy
        if not self.is_obstacle(new_x, new_y) and 0 <= new_x < self.grid_width and 0 <= new_y < self.grid_height:
            self.player.move(dx, dy)
            self.move_enemies()             # move enemies
            self.check_exit()               # check and validate exit position
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
            if not self.is_obstacle(new_x, new_y) and 0 <= new_x < self.grid_width and 0 <= new_y < self.grid_height:
                enemy.move(player_x, player_y)

    def is_obstacle(self, x, y):
        for obstacle in self.obstacles:
            if obstacle.x == x and obstacle.y == y:
                return True
        return False

    def generate_valid_exit(self):
        while True:
            exit_x = random.randint(0, self.grid_width - 1)
            exit_y = random.randint(0, self.grid_height - 1)
            if (exit_x, exit_y) != (self.player.x, self.player.y) and not any((exit_x == obj.x and exit_y == obj.y) for obj in self.enemies + self.obstacles):
                return Exit(exit_x, exit_y)

    def check_exit(self):
        if self.player.x == self.exit.x and self.player.y == self.exit.y:
            self.exits_reached += 1
            self.enemies = [Enemy(random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1)) for _ in range(3)]
            self.obstacles = [Obstacle(random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1)) for _ in range(10)]
            self.exit = self.generate_valid_exit()
            if not self.exit:
                self.exit = self.generate_valid_exit()  # Regenerate the exit if it's not valid

    def check_enemy_collision(self):
        enemies_to_remove = []
        for enemy in self.enemies:
            if enemy.x == self.player.x and enemy.y == self.player.y:
                enemies_to_remove.append(enemy)     # add colliding enemy to remove list

        # count nr of colliding enemies
        nr_colliding_enemies = len(enemies_to_remove)
        print(nr_colliding_enemies)

        # remove all colliding enemies
        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)

        return nr_colliding_enemies

    def run(self):
        self.draw_grid(self.screen)
        self.draw_enemies(self.screen)
        self.draw_player(self.screen)