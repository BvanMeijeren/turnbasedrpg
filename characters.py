import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, screen
from weapons import *

class Character:
    #stats
    def __init__(self, x, y, name, level, xp, hitpoints, max_hitpoints, stamina, max_stamina, critical_chance, 
                 critical_multiplier, species, physical_def, fire_def, ice_def, electricity_def, 
                 skills, items, equipped_weapon, profession, encountered_enemies):
        self.x = x
        self.y = y
        self.name = name 
        self.level = level
        self.xp = xp # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.max_hitpoints = max_hitpoints
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.critical_chance = critical_chance # as a proportion
        self.critical_multiplier = critical_multiplier # decimal
        self.species = species
        self.physical_def = physical_def
        self.fire_def = fire_def # from -1 to 1
        self.ice_def = ice_def # from -1 to 1
        self.electricity_def = electricity_def # from -1 to 1
        self.skills = skills
        self.items = items
        self.equipped_weapon = equipped_weapon
        self.profession = profession
        self.encountered_enemies = encountered_enemies

        # for rendering
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
    stamina=20,
    max_stamina=20,
    critical_chance=0.05, 
    critical_multiplier=1.5,
    species="Monster", 
    physical_def=100, 
    fire_def=100,
    ice_def=100,
    electricity_def=100,
    skills=None, 
    items=None,
    equipped_weapon=create_starterweapon(),
    profession="Knight",
    encountered_enemies=[]
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
    stamina=20,
    max_stamina=20,
    critical_chance=0.05, 
    critical_multiplier=1.5,
    species="Undead", 
    physical_def=100,
    fire_def=100,
    ice_def=100,
    electricity_def=100,
    skills=None, 
    items=None,
    equipped_weapon=create_starterweapon(),
    profession="Knight",
    encountered_enemies=[]
) 
Skeleton.image = pygame.image.load("graphics/skeleton.png").convert()
all_enemies_in_the_game.append(Skeleton)