import pygame

class BackgroundStuff():
    def __init__(self, cardCenter, imageURL):
        self.image = pygame.image.load(imageURL)
        self.rect = self.image.get_rect()
        self.rect.center = cardCenter

    def draw(self, screen):
        screen.blit(self.image, self.rect)

