import pygame
from src.hitpointBar import HitpointBar
from src.specialObjects.fleet import Fleet
from src.specialObjects.fleet import Ship
from src.specialObjects.zones.cardZone import CardZone 
from src.specialObjects.zones.commandZone import CommandZone
from src.player.card import Card
from src.player.deck import Deck
from src.player.cardType import CardType
from src.widgets.button import Button



class Player(HitpointBar, Fleet):
    COMMAND_ZONE_COODS = (1000,500)
    USED_CARD_ZONE_COODS = (1000,140)
    CARD_ZONE_COODS = (300,500)  
    INCOMING_ZONE_COODS = (150,150)  
    SHIP_COORDS = (600,200)
    SHIP_IMAGE_PATHS = ("assets/spaceShipScout.png","assets/spaceShipScout2.png" ,"assets/spaceShipScout3.png")

    def __init__(self, cardCenter, max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints, ship_image_paths, ship_width, ship_height):
        super().__init__(max_hitpoints, width_hitpoints, height_hitpoints, color_hitpoints)
        self.rect =  pygame.Rect(300, 200, 450, 450)
        self.rect.center = (cardCenter[0], cardCenter[1] - 200)
        self.flagShip = Ship(self.SHIP_COORDS[0],self.SHIP_COORDS[1], ship_image_paths, "USS CHAD", (ship_width, ship_height), False)
        self.fleet = Fleet("PLAYER", 1, self.flagShip, None, None, True)
        self.rectShip = self.flagShip.image.get_rect()
        self.rectShip.center = (cardCenter[0], cardCenter[1])
        self.deck = Deck()
        self.deckCount = 0
        # Create a card with an image and add it to the deck
        with open("src/player/decks/starterDeck.txt", 'r') as file:
            for line in file:
                path = "assets/card" + line.split("|")[0] + ".png"
                type = Player.stringToType(line.split("|")[1])
                card = Card(self.CARD_ZONE_COODS[0]  + (self.deckCount * 150), self.CARD_ZONE_COODS[1] - 100, path, type)
                self.deckCount += 1
                self.deck.add_card(card)

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.commandZone = CommandZone(self.COMMAND_ZONE_COODS, "assets/commandZone.png")
        self.cardZone = CardZone(self.CARD_ZONE_COODS, "assets/cardZone.png")
        self.usedCommandZone = CardZone(self.USED_CARD_ZONE_COODS, "assets/usedCommandsZone.png")
        self.incomingCommandZone = CardZone(self.INCOMING_ZONE_COODS, "assets/incomingCommandZone.png")
        self.zones = (self.cardZone, self.usedCommandZone, self.incomingCommandZone)
        self.ship_width = ship_width
        self.ship_height = ship_height
        self.orderButton = Button(0, 200, 300, 100, "COMMAND", (100, 100, 100))

    def stringToType(type):
        type = type.strip()
        if type == "SHIP":
            return CardType.SHIP
        if type == "ATTACK":
            return CardType.ATTACK
         

    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()       
        self.deck.update((self.mouse_x, self.mouse_y))
        for card in self.deck.cards:
            if card.sendToCommand:
                self.commandZone.addCardToZone(card)
        if self.orderButton.clicked:
            self.orderButton.clicked = False
            self.commit_command()
        
        self.fleet.update()

        

    def draw(self, screen):
        #super().draw(screen, self.rect.x, self.rect.top - 100)       
        for zone in self.zones:
            zone.draw(screen)

        self.commandZone.draw(screen)

        self.deck.draw(screen)
        self.fleet.draw(screen)
        self.orderButton.draw(screen)
        

    def handle_event(self, event):
        self.deck.handle_event(event)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.orderButton.handle_event((self.mouse_x, self.mouse_y),event)

    def commit_command(self):
        for card in self.deck.cards:
            if card.inCommandZone:
                card.inCommandZone = False
                card.sendToCommand = False
                            
                card.inUsedCommandZone = True
                self.deck.addCardToUsedCommandZone(card)
                card.cardCount = self.deck.cardsInUsedCommandZone.__len__()
                if card.cardType == CardType.SHIP:
                    newShip = Ship(self.SHIP_COORDS[0], self.SHIP_COORDS[1] + (50 * self.fleet.ship_number), self.SHIP_IMAGE_PATHS, "USS SCOUT", (self.ship_width / 1.5, self.ship_height / 1.5), True)
                    self.fleet.add_ship(newShip)
                if card.cardType == CardType.ATTACK:
                    self.fleet.order("ATTACK")
                
                    



