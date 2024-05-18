from constants import *

def selection_menu(self, attribute, title, options):
    select_text = self.font.render(title, True, WHITE)
    select_rect = select_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(select_text, select_rect)

    for i, class_name in enumerate(options):
        text_color = RED if attribute == i else WHITE
        class_option_text = self.font.render(class_name, True, text_color)
        class_option_rect = class_option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 * (i + 1)))
        screen.blit(class_option_text, class_option_rect)