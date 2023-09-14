import pygame

class FleetZone:
    def __init__(self , zoneCenter, imageURL):
        self.shipsInZone = []  # Initialize an empty list to hold cards in the zone
        self.image = pygame.image.load(imageURL)
        self.rect = self.image.get_rect()
        self.rect.center = zoneCenter

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        # Implement any logic to update the command zone here
        pass

