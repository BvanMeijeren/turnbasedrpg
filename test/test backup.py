import pygame
import sys
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)

# Set up grid parameters
GRID_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Set up screen dimensions
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT + 40

# Game states
START_MENU = 0
GRID_GAME = 1
COMBAT_SCREEN = 2

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, player_x, player_y):
        if self.x < player_x:
            self.x += 1
        elif self.x > player_x:
            self.x -= 1
        if self.y < player_y:
            self.y += 1
        elif self.y > player_y:
            self.y -= 1

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Exit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class StartMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Grid Game", True, WHITE)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.start_text = self.font.render("Press Space to Start", True, WHITE)
        self.start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self, screen):
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_text, self.start_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GRID_GAME
        return START_MENU

class CombatScreen:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("You are now in combat!", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.text, self.text_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return False

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
        self.combat_screen = CombatScreen()
        self.gamestate = START_MENU

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

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.gamestate == GRID_GAME:
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
                    if event.key == pygame.K_SPACE:
                        self.gamestate = GRID_GAME

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

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        menu = StartMenu()

        while True:
            if self.gamestate == GRID_GAME:
                self.handle_input()
                self.check_enemy_collision()
                screen.fill(BLACK)
                self.draw_grid(screen)
                self.draw_enemies(screen)
                self.draw_player(screen)
                pygame.display.flip()
                clock.tick(10)
            # Combat screen state
            # elif self.gamestate == COMBAT_SCREEN:
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             pygame.quit()
            #             sys.exit()
            #     self.combat_screen.draw(screen)
            #     pygame.display.flip()
            #     if self.combat_screen.handle_input():
            #         self.gamestate = GRID_GAME


class GameManager:
    def __init__(self, width, height):
        self.gamestate = START_MENU
        self.grid_game = GRID_GAME
        self.combat_screen = COMBAT_SCREEN
        self.menu = START_MENU
        self.width = width
        self.height = height

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        menu = StartMenu()

        while True:
            # Start Menu State
            if self.gamestate == START_MENU:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                menu.draw(screen)
                pygame.display.flip()
                if menu.handle_input() == GRID_GAME:
                    self.gamestate = GRID_GAME
            # Grid State
            elif self.gamestate == GRID_GAME:
                self.grid_game()
            # Combat screen state
            elif self.gamestate == COMBAT_SCREEN:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.combat_screen.draw(screen)
                pygame.display.flip()
                if self.combat_screen.handle_input():
                    self.gamestate = GRID_GAME

if __name__ == "__main__":
    game = GameManager(GRID_WIDTH, GRID_HEIGHT)
    game.run()
