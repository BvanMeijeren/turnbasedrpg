import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Character:
    #stats
    def __init__(self, x, y, name, id, level, xp, hitpoints, critical_chance, critical_multiplier, species, 
                 fire_def, ice_def, electricity_def, skills, items, equipped_weapon, profession):
        self.x = x
        self.y = y
        self.name = name 
        self.id = id
        self.level = level
        self.xp = xp # for enemies, this is how much you gain upon slaying them
        self.hitpoints = hitpoints
        self.critical_chance = critical_chance # as a proportion
        self.critical_multiplier = critical_multiplier # decimal
        self.species = species
        self.fire_def = fire_def # from -100 to 100 percent
        self.ice_def = ice_def # from -100 to 100 percent
        self.electricity_def = electricity_def # from -100 to 100 percent
        self.skills = skills
        self.items = items
        self.equipped_weapon = equipped_weapon
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

