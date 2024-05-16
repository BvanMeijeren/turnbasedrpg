import pygame

biome_dict = {
    "Forest" : pygame.image.load("graphics/terrain/forest/grass_background.png").convert()
}

def choose_background_texture(biome):
    return biome_dict[biome]