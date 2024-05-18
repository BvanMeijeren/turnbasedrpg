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


def draw_health_bar(self, screen):
    grid_offset_x = (SCREEN_WIDTH) // 20
    grid_offset_y = (SCREEN_HEIGHT) // 20
    health_bar_width = 200
    health_bar_height = 20
    health_bar_rect = pygame.Rect(grid_offset_x, grid_offset_y, health_bar_width, health_bar_height)
    
    # Calculate the width of the health bar based on player's current health
    current_hp_percentage = max(self.player.hitpoints / self.player.max_hitpoints, 0)
    fill_width = int(health_bar_width * current_hp_percentage)
    
    # Draw the empty health bar
    pygame.draw.rect(screen, BLACK, health_bar_rect)
    
    # Draw the filled portion of the health bar in red
    fill_rect = pygame.Rect(grid_offset_x, grid_offset_y, fill_width, health_bar_height)
    pygame.draw.rect(screen, RED, fill_rect)