import pygame

class Card:
    def __init__(self, x, y, image_path):
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.is_hovered = False
        self.is_clicked = False
        self.hover_angle = -15  # Tilt angle when hovered
        self.original_scale = 1.0
        self.hover_scale = 1.5

        self.sendToCommand = False
        self.inCommandZone = False

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.is_hovered:
                self.is_hovered = True
                self.image = pygame.transform.rotozoom(self.original_image, self.hover_angle, self.hover_scale)
                self.rect = self.image.get_rect(center=self.rect.center)
        else:
            if self.is_hovered:
                self.is_hovered = False
                self.image = self.original_image.copy()
                self.rect = self.image.get_rect(center=self.rect.center)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    # Left mouse button clicked on the card
                    self.is_clicked = True
                    self.sendToCommand = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.is_clicked:
                    # Left mouse button released after clicking on the card
                    self.is_clicked = False
                    # Implement the card movement and "To Command Zone" action here
                    self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - 100)
