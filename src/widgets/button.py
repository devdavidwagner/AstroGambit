import pygame

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.highlighted = False
        self.color = color
        self.clicked = False

    def draw(self, surface):
        if self.highlighted:
            pygame.draw.rect(surface, (200, 200, 200), self.rect, 3)  # Highlighted border
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.highlighted = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def handle_event(self, mouse_pos, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.check_click(mouse_pos):
                    self.clicked = True                   
            elif event.type == pygame.MOUSEMOTION:               
                self.check_hover(mouse_pos)
