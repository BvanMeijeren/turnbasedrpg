import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
FONT = pygame.font.SysFont(None, 36)

class CharacterCreationPage:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Character Creation")

        self.selected_class = 0
        self.selected_race = 0

        self.classes = ["Warrior", "Mage", "Rogue"]
        self.races = ["Human", "Elf", "Dwarf"]

        self.selecting_class = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.selecting_class and self.selected_class > 0:
                        self.selected_class -= 1
                    elif not self.selecting_class and self.selected_race > 0:
                        self.selected_race -= 1
                elif event.key == pygame.K_s:
                    if self.selecting_class and self.selected_class < len(self.classes) - 1:
                        self.selected_class += 1
                    elif not self.selecting_class and self.selected_race < len(self.races) - 1:
                        self.selected_race += 1
                elif event.key == pygame.K_SPACE:
                    if self.selecting_class:
                        self.selecting_class = False
                    else:
                        return True
        return False

    def render(self):
        self.screen.fill(BLACK)

        if self.selecting_class:
            select_text = FONT.render("Select Class:", True, WHITE)
            select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(select_text, select_rect)

            for i, class_name in enumerate(self.classes):
                text_color = RED if self.selected_class == i else WHITE
                class_option_text = FONT.render(class_name, True, text_color)
                class_option_rect = class_option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 * (i + 1)))
                self.screen.blit(class_option_text, class_option_rect)
        else:
            select_text = FONT.render("Select Race:", True, WHITE)
            select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(select_text, select_rect)

            for i, race_name in enumerate(self.races):
                text_color = RED if self.selected_race == i else WHITE
                race_option_text = FONT.render(race_name, True, text_color)
                race_option_rect = race_option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 * (i + 1)))
                self.screen.blit(race_option_text, race_option_rect)

        pygame.display.flip()

    def run(self):
        while True:
            if self.handle_input():
                break
            self.render()

        if self.selecting_class:
            self.selecting_class = False
            self.run()

        selected_class = self.classes[self.selected_class]
        selected_race = self.races[self.selected_race]
        print("Class:", selected_class)
        print("Race:", selected_race)

if __name__ == "__main__":
    character_creation_page = CharacterCreationPage()
    character_creation_page.run()
