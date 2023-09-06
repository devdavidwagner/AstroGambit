import pygame
from src.player.card import Card  # Import your Card class

class Deck:
    def __init__(self):
        self.cards: list[Card] = []  # Initialize an empty list to hold the cards with type hint
        self.cardsInCommandZone: list[Card] = [] # Initialize an empty list to hold the cards with type hint

    def add_card(self, card: Card):
        self.cards.append(card)

    def addCardToCommandZone(self,card):
        self.cardsInCommandZone.append(card)

    def draw(self, surface):
        for card in self.cards:
            card.draw(surface)

    def update(self, mouse_pos):
        for card in self.cards:
            card.update(mouse_pos)
            if card.sendToCommand:
                self.addCardToCommandZone(card)
                card.inCommandZone = True
                
    def handle_event(self, events):
        for card in self.cards:
            card.handle_event(events) 