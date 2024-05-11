import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from weapon_generator import *

class Character:
    #stats
    def __init__(self, x, y, name, id, level, xp, hitpoints, max_hitpoints, critical_chance, critical_multiplier, species, 
                 fire_def, ice_def, electricity_def, skills, items, equipped_weapon, profession):
        self.x = x
        self.y = y
        self.name = name 
        self.id = id
        self.level = 1
        self.xp = 0 # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.max_hitpoints = max_hitpoints
        self.critical_chance = 0.05 # as a proportion
        self.critical_multiplier = 1.5 # decimal
        self.species = species
        self.fire_def = fire_def # from -1 to 1
        self.ice_def = ice_def # from -1 to 1
        self.electricity_def = electricity_def # from -1 to 1
        self.skills = None
        self.items = None
        self.equipped_weapon = None
        self.profession = profession

        # for rendering
        super().__init__()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image = pygame.image.load("graphics/knight.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # move function
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

