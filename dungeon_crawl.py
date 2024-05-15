# grid_game.py
import pygame
import random
import copy

#from player import Player
#from enemy import Enemy 
from obstacle import Obstacle
from exit import Exit
from constants import *
from characters import Character, all_enemies_in_the_game

class GridGame:
    def __init__(self, grid_width, grid_height, player):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.player = player
        self.enemies = self.generate_enemies(nr_enemies=2)
        self.obstacles = [Obstacle(random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)) for _ in range(10)]
        self.exit = self.generate_valid_exit()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player_moved = False
        self.exits_reached = 0

        # Load player image
        self.player_image = pygame.transform.scale(self.player.image, (GRID_SIZE, GRID_SIZE))

    ### Generate enemies
    def generate_enemies(self, nr_enemies):
        chosen_enemies = [] # these will spawn on the current floor the player is on
        for _ in range(nr_enemies):
            chosen_enemy = copy.copy(random.choice(all_enemies_in_the_game))
            chosen_enemy.x = random.randint(0, self.grid_width - 1)
            chosen_enemy.y = random.randint(0, self.grid_height - 1)
            chosen_enemy.hitpoints = random.randint(self.player.max_hitpoints*0.3, self.player.max_hitpoints*0.5)
            chosen_enemy.max_hitpoints = random.randint(self.player.max_hitpoints*0.3, self.player.max_hitpoints*0.5)
            chosen_enemies.append(chosen_enemy)

        return chosen_enemies

        

    #### Grid game drawing function ####
    def draw_grid(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * GRID_SIZE + grid_offset_x, y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x * GRID_SIZE + grid_offset_x, obstacle.y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BROWN, obstacle_rect)
        if self.exit:
            #self.enemies = self.generate_enemies(3)
            exit_rect = pygame.Rect(self.exit.x * GRID_SIZE + grid_offset_x, self.exit.y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, exit_rect)

    def draw_player(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2

        # Update player sprite accroding to selected profession
        if self.player.profession == 'Knight':
            self.player_image = pygame.image.load("graphics/knight.png").convert_alpha()
        elif self.player.profession == 'Mage':
            self.player_image = pygame.image.load("graphics/wizard.png").convert_alpha()
        elif self.player.profession == 'Rogue':
            self.player_image = pygame.image.load("graphics/thief.png").convert_alpha()
        # scale image
        self.player_image = pygame.transform.scale(self.player_image, (GRID_SIZE, GRID_SIZE))

        # Calculate the position to blit the enemy image
        # Blit the enemy image onto the screen
        player_rect = self.player_image.get_rect(topleft=(self.player.x * GRID_SIZE + grid_offset_x, self.player.y * GRID_SIZE + grid_offset_y))
        screen.blit(self.player_image, player_rect)

    def draw_enemies(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2
        for enemy in self.enemies:
            # scale image for enemies
            enemy.image = pygame.transform.scale(enemy.image, (GRID_SIZE, GRID_SIZE))
            # Calculate the position to blit the enemy image
            enemy_rect = enemy.image.get_rect(topleft=(enemy.x * GRID_SIZE + grid_offset_x, enemy.y * GRID_SIZE + grid_offset_y))
            # Blit the enemy image onto the screen
            screen.blit(enemy.image, enemy_rect)

    def draw_health_bar(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2
        health_bar_width = self.grid_width * GRID_SIZE
        health_bar_height = 20
        health_bar_rect = pygame.Rect(grid_offset_x, grid_offset_y + self.grid_height * GRID_SIZE + 10, health_bar_width, health_bar_height)
        
        # Calculate the width of the health bar based on player's current health
        current_hp_percentage = max(self.player.hitpoints / self.player.max_hitpoints, 0)
        fill_width = int(health_bar_width * current_hp_percentage)
        
        # Draw the empty health bar
        pygame.draw.rect(screen, BLACK, health_bar_rect)
        
        # Draw the filled portion of the health bar in red
        fill_rect = pygame.Rect(grid_offset_x, grid_offset_y + self.grid_height * GRID_SIZE + 10, fill_width, health_bar_height)
        pygame.draw.rect(screen, RED, fill_rect)

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
                enemy.enemy_move(player_x, player_y)

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

            # Generate new enemies for the next level
            self.enemies = self.generate_enemies(nr_enemies=2)

            #self.enemies = [Enemy(random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1)) for _ in range(3)]
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

        # remove all colliding enemies
        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)

        return nr_colliding_enemies

    def run(self):
        self.draw_grid(self.screen)
        self.draw_enemies(self.screen)
        self.draw_player(self.screen)
        self.draw_health_bar(self.screen)