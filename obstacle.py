import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # for rendering
        super().__init__()
        self.image = pygame.image.load("graphics/terrain/forest/rocks.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Forest biome
forest_obstacles = []

rock = Obstacle(
    x = 0,
    y = 0
)

forest_obstacles.append(rock)

tree = Obstacle(
    x = 0,
    y = 0
)
tree.image = pygame.image.load("graphics/terrain/forest/tree.png").convert()
forest_obstacles.append(tree)