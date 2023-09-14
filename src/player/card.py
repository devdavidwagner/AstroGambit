import pygame
from src.player.cardType import CardType

class Card:
    COMMAND_ZONE_COODS = (1000,450)
    CARD_ZONE_COODS = (300,600)
    USED_CARD_ZONE_COODS = (1000,140)
    def __init__(self, x, y, image_path, cardType):
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.is_hovered = False
        self.is_clicked = False
        self.hover_angle = -15  # Tilt angle when hovered
        self.original_scale = 1.0
        self.hover_scale = 1.1

        self.sendToCommand = False
        self.inCommandZone = False
        self.cardType = cardType
        self.inUsedCommandZone = False
        self.cardBackImg = pygame.image.load("assets/cardBack.png")
        self.cardCount = 1
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.5), int(self.image.get_height() * 0.5)))
        
        

    def draw(self, surface, count = 1, commandZone = ""):
        if commandZone == "COMMAND":
            surface.blit(self.image, (self.rect.topleft[0] + 30, self.rect.topleft[1] + 100))
        elif commandZone == "USED":
            self.rect.x = self.USED_CARD_ZONE_COODS[0] - (30 * count)
            self.rect.y = self.USED_CARD_ZONE_COODS[1] - 100
            surface.blit(self.image, (self.rect.topleft[0], self.rect.topleft[1] + 30))
        else:
            surface.blit(self.image, self.rect.topleft)  


    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.is_hovered:
                self.is_hovered = True
                # Straighten the card and zoom it
                self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * self.hover_scale), int(self.original_image.get_height() * self.hover_scale)))
                self.rect = self.image.get_rect(center=self.rect.center)
        elif self.inCommandZone:
                self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.inUsedCommandZone:
                self.image = pygame.transform.scale(self.cardBackImg, (int(self.cardBackImg.get_width() * 0.5), int(self.cardBackImg.get_height() * 0.5)))
        else:
            if self.is_hovered:
                self.is_hovered = False
                # Rotate the image back to 0 degrees (no rotation) and restore the original size
                self.image = pygame.transform.rotate(self.original_image, 0)
                self.image = pygame.transform.scale(self.image, (int(self.original_image.get_width()), int(self.original_image.get_height())))
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.image = pygame.transform.rotate(self.original_image, self.hover_angle)
                self.image = pygame.transform.scale(self.image, (int(self.original_image.get_width()), int(self.original_image.get_height())))
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
                    self.rect.center = (self.COMMAND_ZONE_COODS)
