import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rounded Transparent Square Example")

# Define colors
transparent_color = (0, 0, 0, 128)  # Black color with 50% transparency (128/255)

# Create a transparent surface
square_size = (200, 200)
transparent_square = pygame.Surface(square_size, pygame.SRCALPHA)

# Fill the surface with a transparent color with rounded corners
rounded_rect = pygame.Rect(0, 0, *square_size)
border_radius = 20  # Adjust the radius as needed
pygame.draw.rect(transparent_square, transparent_color, rounded_rect, border_radius=border_radius)

# Calculate the position to center the square
screen_width, screen_height = window_size
square_width, square_height = square_size
square_position = (
    (screen_width - square_width) // 2,
    (screen_height - square_height) // 2
)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Blit the transparent square with rounded corners onto the screen at the calculated position
    screen.blit(transparent_square, square_position)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
