import pygame

class HitpointBar:
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)  # New color for the shield overlay
    
    def __init__(self, max_hitpoints, width, height, color):
        self.max_hitpoints = max_hitpoints
        self.hitpoints = max_hitpoints
        self.width = width
        self.height = height
        self.color = color  # Bar color
        self.shield = 50  # Shield hitpoints
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(str(self.hitpoints) + "/" + str(max_hitpoints), True, self.BLACK)
        self.text_rect = self.text_surface.get_rect()

    def draw(self, surface, x, y):
        # Calculate the width of the hitpoint bar
        bar_width = int((self.hitpoints / self.max_hitpoints) * self.width)
        
        # Calculate the width of the shield overlay
        shield_width = int((self.shield / self.max_hitpoints) * self.width)
        
        # Draw the hitpoint bar in the specified color
        pygame.draw.rect(surface, self.color, (x, y, bar_width, self.height))
        
        # Draw the shield overlay in blue (overlapping the hitpoint bar)
        pygame.draw.rect(surface, self.BLUE, (x + bar_width, y, shield_width, self.height))
        
        # Draw the text
        self.text_rect = pygame.Rect(x, y, self.width, self.height)
        surface.blit(self.text_surface, self.text_rect)
