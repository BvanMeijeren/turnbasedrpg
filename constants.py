import pygame

# Initialize pygame
pygame.init()

# Get the display size
DISPLAY_INFO = pygame.display.Info()
DISPLAY_SIZE = (DISPLAY_INFO.current_w, DISPLAY_INFO.current_h)

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
SCREEN_WIDTH = DISPLAY_SIZE[0]
SCREEN_HEIGHT = DISPLAY_SIZE[1]

# Create the screen with correct dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Game states
START_MENU = 0
CHARACTER_CREATION = 1
GRID_GAME = 2
COMBAT_SCREEN = 3
