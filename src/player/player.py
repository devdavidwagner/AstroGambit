import pygame
from src.hitpointBar import HitpointBar
from src.specialObjects.fleet import Fleet
from src.specialObjects.ship import Ship
from src.player.card import Card
from src.player.deck import Deck

class Player(HitpointBar, Fleet):
    def __init__(self, cardCenter, max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints, ship_image_paths, ship_width, ship_height):
        super().__init__(max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints)
        self.rect =  pygame.Rect(300, 200, 450, 450)
        self.rect.center = (cardCenter[0], cardCenter[1] - 200)
        self.ship = Ship(400, 200, ship_image_paths, "USS CHAD", (ship_width, ship_height))
        self.rectShip = self.ship.image.get_rect()
        self.rectShip.center = (cardCenter[0], cardCenter[1])
        self.deck = Deck()
        # Create a card with an image and add it to the deck
        card_image_path = "assets/cardShipNebula.png"  # Replace with the actual image path
        card = Card(800, 300,card_image_path)
        self.deck.add_card(card)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.ship.update()
        self.deck.update((self.mouse_x, self.mouse_y))
        

    def draw(self, screen):
        super().draw(screen, self.rect.x, self.rect.top - 100)
        self.deck.draw(screen)
        #screen.blit(self.image, self.rect)
        self.ship.draw(screen)

    def handle_event(self, event):
        self.deck.handle_event(event)

