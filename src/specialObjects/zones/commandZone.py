import pygame

class CommandZone:
    def __init__(self , zoneCenter, imageURL):
        self.cardsInZone = []  # Initialize an empty list to hold cards in the zone
        self.commandSent = False  # Initialize the command state as False
        self.image = pygame.image.load(imageURL)
        self.rect = self.image.get_rect()
        self.rect.center = zoneCenter

    def addCardToZone(self, card):
        self.cardsInZone.append(card)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        # Implement any logic to update the command zone here
        pass

    def send_command(self):
        # Implement the functionality to send a command (e.g., set commandSent to True)
        self.commandSent = True

    def reset(self):
        # Implement the functionality to reset the command zone (e.g., clear cards and reset state)
        self.cardsInZone = []
        self.commandSent = False
