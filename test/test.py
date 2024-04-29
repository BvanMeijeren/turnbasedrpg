import pygame
import sys

# Initialize pygame
pygame.init()

# Get the display size
DISPLAY_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)


# Set up screen dimensions
SCREEN_WIDTH = DISPLAY_SIZE[0]
SCREEN_HEIGHT = DISPLAY_SIZE[1]
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set up fonts
FONT = pygame.font.SysFont(None, 32)
TITLE_FONT = pygame.font.SysFont(None, 48)

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class HPBar(pygame.sprite.Sprite):
    def __init__(self, max_hp, x, y):
        super().__init__()
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.width = 200
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.fill_color = (0, 255, 0)
        self.empty_color = (255, 0, 0)

    def update(self, current_hp):
        self.current_hp = current_hp
        fill_width = int((self.current_hp / self.max_hp) * self.width)
        fill_rect = pygame.Rect(0, 0, fill_width, self.height)
        pygame.draw.rect(self.image, self.fill_color, fill_rect)
        empty_rect = pygame.Rect(fill_width, 0, self.width - fill_width, self.height)
        pygame.draw.rect(self.image, self.empty_color, empty_rect)

def main():
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pokémon-like RPG Page")

    # Load background image
    background_image = pygame.image.load("graphics/forest.jpg").convert()

    # Load character and Pokémon images
    character_image = pygame.image.load("graphics/character.png").convert_alpha()
    pokemon_image = pygame.image.load("graphics/goblin.png").convert_alpha()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    characters = pygame.sprite.Group()
    pokemons = pygame.sprite.Group()

    # Create character and Pokémon sprites
    character = Character(character_image, 100, 450)
    pokemon = Pokemon(pokemon_image, 600, 450)

    # Create HP bars
    character_hp_bar = HPBar(100, 50, 50)
    pokemon_hp_bar = HPBar(200, 550, 50)

    # Add sprites to sprite groups
    characters.add(character)
    pokemons.add(pokemon)
    all_sprites.add(character, pokemon, character_hp_bar, pokemon_hp_bar)

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Blit background image
        screen.blit(background_image, (0, 0))

        # Draw the title
        title_text = TITLE_FONT.render("Pokémon-like RPG", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_rect)

        # Draw the sprites
        all_sprites.draw(screen)

        # Update the HP bars (for demonstration purposes)
        character_hp_bar.update(80)  # Update character HP (80 out of 100)
        pokemon_hp_bar.update(150)   # Update Pokémon HP (150 out of 200)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
