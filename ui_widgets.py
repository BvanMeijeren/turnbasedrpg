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


def popup(r,g,b,transparency,width,height,x,y):
    # Create a transparent surface
    background_color = (r, g, b, transparency)  # Black color with 50% transparency (128/255)
    border_color = (0,0,0, 180)      # Solid brown color for the border

    square_size = (width, height)
    transparent_square = pygame.Surface(square_size, pygame.SRCALPHA)

    # Fill the surface with a transparent color with rounded corners
    rounded_rect = pygame.Rect(0, 0, *square_size)
    border_radius = 20  # Adjust the radius as needed
    pygame.draw.rect(transparent_square, background_color, rounded_rect, border_radius=border_radius)

    # Draw the border with rounded corners
    border_thickness = 5  # Adjust the thickness of the border as needed
    pygame.draw.rect(transparent_square, border_color, rounded_rect, border_radius=border_radius, width=border_thickness)

    square_position = (x, y)  # Position on the main screen
    screen.blit(transparent_square, square_position)

def centered_popup(r,g,b,transparency,width,height):
    # examples for parameters
    # color_tuple = (139, 69, 19, 128) for brown or (0, 0, 0, 128) for grey
    # size_tuple = (800,500) for width and height respectively

    square_size = (width, height)

    popup(
        r = r,
        g = g,
        b = b,
        transparency = transparency,
        width = width,
        height = height,
        x = ( SCREEN_WIDTH - square_size[0]) //2,
        y = ( SCREEN_HEIGHT - square_size[1]) //2
    )

# player menu
def draw_status_bar(self, x, y, attribute, max_attribute):

        status_bar_width = SCREEN_WIDTH * 0.15
        status_bar_height = 30
        status_bar_rect = pygame.Rect(x, y, status_bar_width, status_bar_height)
        
        # Calculate the width of the health bar based on player's current health
        attribute_percentage = max(attribute / max_attribute, 0)
        fill_width = int(status_bar_width * attribute_percentage)
        
        status_bar_rects = []

        # Draw the empty health bar
        empty_rect = pygame.draw.rect(screen, BLACK, status_bar_rect)
        status_bar_rects.append(empty_rect)
        
        # Draw the filled portion of the health bar in red
        #fill_rect = pygame.Rect(x, y, fill_width, status_bar_height)
        fill_rect = pygame.Rect(x, y, fill_width, status_bar_height)
        #filled_rect = pygame.draw.rect(screen, color, fill_rect)
        status_bar_rects.append(fill_rect)

        return status_bar_rects


def player_status_menu(self):

    square_size = (SCREEN_WIDTH, SCREEN_HEIGHT / 6)
    x = (SCREEN_WIDTH - square_size[0]) // 2
    y = (SCREEN_HEIGHT - square_size[1]) - 100

    popup(
        r = 139,
        g = 69,
        b = 19,
        transparency = 90,
        width = square_size[0],
        height = square_size[1],
        x = x,
        y = y
    )

    # health status bar
    health_bar_rects = draw_status_bar(
         self, 
         x= x + SCREEN_WIDTH *0.1,
         y=y + 50,
         attribute = self.player.hitpoints,
         max_attribute = self.player.max_hitpoints
         )
    # draw empty bar
    #pygame.draw.rect(screen, BLACK, health_bar_rects[0])
    #draw filled bar
    pygame.draw.rect(screen, RED, health_bar_rects[1])

    
    # stamina status bar
    stamina_bar_rects = draw_status_bar(
         self, 
         x= x + SCREEN_WIDTH *0.1,
         y=y + 100,
         attribute = self.player.stamina,
         max_attribute = self.player.max_stamina
         )
    pygame.draw.rect(screen, BLUE, stamina_bar_rects[1])


# speech popup for NPCs
#def speech_popup(self,screen):