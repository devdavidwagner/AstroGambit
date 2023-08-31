import pygame
from src.hitpointBar import HitpointBar

class Player(HitpointBar):
    def __init__(self, cardCenter,  max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints):
        super().__init__( max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints)
        self.image = pygame.image.load("assets/TestCard1.png")
        self.rect = self.image.get_rect()
        self.rect.center = cardCenter

    def draw(self, screen):
        super().draw(screen, self.rect.x, self.rect.top - 100)
        screen.blit(self.image, self.rect)
