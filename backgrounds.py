import pygame


# gridwide background with textures such as grass
grid_biome_dict = {
    "Forest" : pygame.image.load("graphics/terrain/forest/grass_background.png").convert()
}

def choose_grid_background(biome):
    return grid_biome_dict[biome]


# screenwide backgrounds for during combat and start menu
combat_biome_dict = {
    "Forest": pygame.image.load("graphics/forest.jpg").convert()
}

def choose_combat_background(biome):
    return combat_biome_dict[biome]