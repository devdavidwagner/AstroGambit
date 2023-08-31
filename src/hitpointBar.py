import pygame

class HitpointBar:
    def __init__(self, max_hitpoints, width, height, color):
        self.max_hitpoints = max_hitpoints
        self.hitpoints = max_hitpoints
        self.width = width
        self.height = height
        self.color = color # New attribute to store the bar color

    def draw(self, surface, x, y):
        bar_width = int((self.hitpoints / self.max_hitpoints) * self.width)
        pygame.draw.rect(surface, self.color, (x, y, bar_width, self.height))
        pygame.draw.rect(surface, (255, 0, 0), (x + bar_width, y, self.width - bar_width, self.height))  # Red part
