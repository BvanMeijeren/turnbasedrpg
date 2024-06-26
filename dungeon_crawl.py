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
from obstacle import forest_obstacles
from backgrounds import choose_grid_background
from ui_widgets import player_status_menu

class GridGame:
    def __init__(self, grid_width, grid_height, player):
        self.font = font_normal
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.player = player
        self.enemies = self.generate_enemies(nr_enemies=2)
        self.player.encountered_enemies = []
        self.obstacles = self.generate_obstacles(nr_obstacles=10)
        self.biome = 'Forest' # forest by default
        self.exit = self.generate_valid_exit()
        self.screen = screen
        self.player_moved = False
        self.exits_reached = 0

        # Load player image
        #self.player_image = pygame.transform.scale(self.player.image, (GRID_SIZE, GRID_SIZE))

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
    
    def generate_obstacles(self, nr_obstacles):
        chosen_obstacles = []
        for _ in range(nr_obstacles):
            chosen_obstacle = copy.copy(random.choice(forest_obstacles))
            chosen_obstacle.x = random.randint(0, self.grid_width - 1)
            chosen_obstacle.y = random.randint(0, self.grid_height - 1)
            chosen_obstacles.append(chosen_obstacle)

        return chosen_obstacles

    # background texture
    def draw_background(self):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2

        background_texture = choose_grid_background(self.biome)
        background_texture = pygame.transform.scale(background_texture, ( (GRID_SIZE * GRID_WIDTH), (GRID_SIZE * GRID_HEIGHT) ))
        background_texture_rect = pygame.Rect( (GRID_SIZE + grid_offset_x - 50), (GRID_SIZE + grid_offset_y -50), GRID_SIZE, GRID_SIZE)
        screen.blit(background_texture, background_texture_rect)

    #### Grid game drawing function ####
    def draw_grid(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2

        # grid
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * GRID_SIZE + grid_offset_x, y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)

        # add obstacles
        for obstacle in self.obstacles:
            # scale image
            obstacle.image = pygame.transform.scale(obstacle.image, (GRID_SIZE, GRID_SIZE))
            # get rectangle
            obstacle_rect = pygame.Rect(obstacle.x * GRID_SIZE + grid_offset_x, obstacle.y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
            # Blit the enemy image onto the screen
            screen.blit(obstacle.image, obstacle_rect)

        # add exit
        if self.exit:
            exit_rect = pygame.Rect(self.exit.x * GRID_SIZE + grid_offset_x, self.exit.y * GRID_SIZE + grid_offset_y, GRID_SIZE, GRID_SIZE)
            exit_image = pygame.image.load("graphics/stairs.png").convert()
            exit_image = pygame.transform.scale(exit_image, (GRID_SIZE, GRID_SIZE))
            screen.blit(exit_image, exit_rect)

    def draw_player(self, screen):
        grid_offset_x = (SCREEN_WIDTH - self.grid_width * GRID_SIZE) // 2
        grid_offset_y = (SCREEN_HEIGHT - self.grid_height * GRID_SIZE) // 2

        # scale image
        player_image = pygame.transform.scale(self.player.image, (GRID_SIZE, GRID_SIZE))

        # Calculate the position to blit the enemy image
        # Blit the enemy image onto the screen
        player_rect = player_image.get_rect(topleft=(self.player.x * GRID_SIZE + grid_offset_x, self.player.y * GRID_SIZE + grid_offset_y))
        screen.blit(player_image, player_rect)


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
        enemies_colliding_with_player = []
        for enemy in self.enemies:
            if enemy.x == self.player.x and enemy.y == self.player.y:
                enemies_colliding_with_player.append(enemy)     # add colliding enemy to remove list

        # count encountered enemies and store 
        self.player.encountered_enemies = enemies_colliding_with_player
        nr_enemies_encountered = len(enemies_colliding_with_player)
        # print('colliding with ' + str(nr_enemies_encountered) + ' enemies' )
        # print(enemies_colliding_with_player)

        # remove all colliding enemies
        for enemy in enemies_colliding_with_player:
            self.enemies.remove(enemy)
        
        return nr_enemies_encountered

    def run(self):
        self.draw_background()
        self.draw_grid(self.screen)
        player_status_menu(self, self.screen)
        self.draw_enemies(self.screen)
        self.draw_player(self.screen)