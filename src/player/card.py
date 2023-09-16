import pygame,math
from src.player.cardType import CardType

class Card:
    COMMAND_ZONE_COODS = (1000,450)
    CARD_ZONE_COODS = (10,600)
    USED_CARD_ZONE_COODS = (1000,140)
    INCOMING_ZONE_COODS = (150,150)  
    def __init__(self, x, y, image_path, cardType, cardCount):
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.cardCount = cardCount
        self.rect.topleft = (0 + (30 * self.cardCount), 900)
        self.is_hovered = False
        self.is_clicked = False
        self.hover_angle = -15  # Tilt angle when hovered
        self.original_scale = 1.0
        self.hover_scale = 1.1
        self.sendToCommand = False
        self.inCommandZone = False
        self.cardType = cardType
        self.inUsedCommandZone = False
        self.inIncomingCommandZone = False
        self.inMainZone = False
        self.cardBackImg = pygame.image.load("assets/cardBack.png")
       
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.2), int(self.image.get_height() * 0.2)))
        self.z = 1
        x = x  + (40 * self.cardCount)
        print(self.cardCount)
        self.small_rect = pygame.Rect(
            self.rect.centerx,
            self.rect.centery,
            140,
            500
        )

    def __lt__(self, other):
        return self.z < other.z

    def draw(self, surface, count=1, commandZone=""):
        angle = math.radians(10)  # Angle in degrees (adjust as needed)

        if commandZone == "COMMAND":              
            self.rect.x = self.COMMAND_ZONE_COODS[0] - 100
            self.rect.y = self.COMMAND_ZONE_COODS[1] - 100
            surface.blit(self.image, self.rect.topleft)  
        elif commandZone == "USED":
            self.rect.x = self.USED_CARD_ZONE_COODS[0] - (30 * count)
            self.rect.y = self.USED_CARD_ZONE_COODS[1] - 60
            surface.blit(self.image, (self.rect.topleft[0], self.rect.topleft[1] + 30))
        elif commandZone == "INCOMING":
            self.rect.x = self.INCOMING_ZONE_COODS[0] - (30 * count)
            self.rect.y = self.INCOMING_ZONE_COODS[1] - 60
            surface.blit(self.image, (self.rect.topleft[0], self.rect.topleft[1] + 30))
        elif commandZone == "MAIN":
            print("MAIN " + str(count))
            x = 0 + (100 * count)
            y = self.USED_CARD_ZONE_COODS[1] + 200 + (30 * count * math.sin(angle))
            self.rect.x = x
            self.rect.y = y
            surface.blit(self.image, (x, y))  
        else:
            x = 0 + (100 * self.cardCount)
            y = self.USED_CARD_ZONE_COODS[1] + 200 + (30 * self.cardCount * math.sin(angle))
            self.rect.x = x
            self.rect.y = y
            surface.blit(self.image, (x, y))  

    

    def update(self, mouse_pos, alreadyHoveredCard):
        self.small_rect.x = self.rect.x
        self.small_rect.y = self.rect.y
        if self.small_rect.collidepoint(mouse_pos):
            if not self.is_hovered and not alreadyHoveredCard and not self.inCommandZone and not self.inUsedCommandZone and not self.inIncomingCommandZone:
                self.is_hovered = True
                # Straighten the card and zoom it
                self.image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * self.hover_scale), int(self.original_image.get_height() * self.hover_scale)))
                self.rect = self.image.get_rect()
        elif self.inCommandZone:
                self.image = pygame.transform.rotate(self.original_image, 0)
                self.rect = self.image.get_rect()
        elif self.inIncomingCommandZone:
                self.image = pygame.transform.scale(self.cardBackImg, (int(self.cardBackImg.get_width() * 0.5), int(self.cardBackImg.get_height() * 0.5)))
                self.rect = self.image.get_rect()           
        elif self.inUsedCommandZone:
                self.image = pygame.transform.scale(self.cardBackImg, (int(self.cardBackImg.get_width() * 0.5), int(self.cardBackImg.get_height() * 0.5)))
                self.rect = self.image.get_rect()
        else:
            if self.is_hovered:
                self.z = 0
                self.is_hovered = False
                # Rotate the image back to 0 degrees (no rotation) and restore the original size           
                self.image = pygame.transform.rotate(self.original_image, 0)
                self.image = pygame.transform.scale(self.image, (int(self.original_image.get_width()), int(self.original_image.get_height())))
                self.rect = self.image.get_rect()
            else:
                self.image = pygame.transform.rotate(self.original_image, self.hover_angle)
                self.image = pygame.transform.scale(self.image, (int(self.original_image.get_width()), int(self.original_image.get_height())))
                self.rect = self.image.get_rect()
        
                


    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos) and self.is_hovered:
                    print("click")
                    self.is_clicked = True
                    self.sendToCommand = True
                    self.inCommandZone = True
          
