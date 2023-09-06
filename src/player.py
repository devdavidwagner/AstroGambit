import pygame
from src.hitpointBar import HitpointBar
from src.specialObjects.fleet import Fleet
from src.specialObjects.ship import Ship

class Player(HitpointBar, Fleet):
    def __init__(self, cardCenter, max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints, ship_image_paths, ship_width, ship_height):
        super().__init__(max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints)
        self.rect =  pygame.Rect(300, 200, 450, 450)
        self.rect.center = (cardCenter[0], cardCenter[1] - 200)
        self.ship = Ship(400, 200, ship_image_paths, "USS CHAD", (ship_width, ship_height))
        self.rectShip = self.ship.image.get_rect()
        self.rectShip.center = (cardCenter[0], cardCenter[1])

    def update(self):
        self.ship.update()
        

    def draw(self, screen):
        super().draw(screen, self.rect.x, self.rect.top - 100)
        #screen.blit(self.image, self.rect)
        self.ship.draw(screen)

