import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from weapon_generator import *

class Character:
    #stats
    def __init__(self, x, y, name, level, xp, hitpoints, max_hitpoints, critical_chance, critical_multiplier, species, 
                 fire_def, ice_def, electricity_def, skills, items, equipped_weapon, profession):
        self.x = x
        self.y = y
        self.name = name 
        self.level = level
        self.xp = xp # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.max_hitpoints = max_hitpoints
        self.critical_chance = critical_chance # as a proportion
        self.critical_multiplier = critical_multiplier # decimal
        self.species = species
        self.fire_def = fire_def # from -1 to 1
        self.ice_def = ice_def # from -1 to 1
        self.electricity_def = electricity_def # from -1 to 1
        self.skills = skills
        self.items = items
        self.equipped_weapon = equipped_weapon
        self.profession = profession

        # for rendering
        super().__init__()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image = pygame.image.load("graphics/goblin.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # move function
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def enemy_move(self, player_x, player_y):
        if self.x < player_x:
            self.x += 1
        elif self.x > player_x:
            self.x -= 1
        if self.y < player_y:
            self.y += 1
        elif self.y > player_y:
            self.y -= 1


# enemies

all_enemies_in_the_game = []

Goblin = Character(
    x = 0, # overwritten later
    y = 0, # overwritten later
    name="Goblin Niffler", 
    level=1, #
    xp=0,
    hitpoints=50, # overwritten based on player level
    max_hitpoints=50, # overwritten based on player level
    critical_chance=0.05, 
    critical_multiplier=1.5,
    species="Monster", 
    fire_def=100,
    ice_def=100,
    electricity_def=100,
    skills=None, 
    items=None,
    equipped_weapon=None,
    profession="Knight"
) 
Goblin.image = pygame.image.load("graphics/goblin.png").convert()
all_enemies_in_the_game.append(Goblin)

Skeleton = Character(
    x = 0, # overwritten later
    y = 0, # overwritten later
    name="Wonky Skeleton", 
    level=1, #
    xp=0,
    hitpoints=30, # overwritten based on player level
    max_hitpoints=50, # overwritten based on player level
    critical_chance=0.05, 
    critical_multiplier=1.5,
    species="Undead", 
    fire_def=100,
    ice_def=100,
    electricity_def=100,
    skills=None, 
    items=None,
    equipped_weapon=None,
    profession="Knight"
) 
Skeleton.image = pygame.image.load("graphics/skeleton.png").convert()
all_enemies_in_the_game.append(Skeleton)