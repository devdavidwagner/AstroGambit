import pygame
from src.player.card import Card  # Import your Card class

class Deck:
    def __init__(self):
        self.cards: list[Card] = [] 
        self.cardsInIncomingZone: list[Card] = []
        self.cardsInCommandZone: list[Card] = [] 
        self.cardsInUsedCommandZone: list[Card] = [] 
        self.cardsInMainZone: list[Card] = [] 
        self.alreadyHoveredCard = False

    def add_card(self, card: Card):
        self.cards.append(card)

    def addCardToCommandZone(self,card):
        self.cardsInCommandZone.append(card)

    def addCardToUsedCommandZone(self,card):
        self.cardsInUsedCommandZone.append(card)

    def addCardToIncomingZone(self,card):
        self.cardsInIncomingZone.append(card)
    
    def addCardToMainZone(self,card):
        self.cardsInMainZone.append(card)

    def draw(self, surface):
        for card in self.cards:
            if card.inCommandZone:
                card.draw(surface,1, "COMMAND")
            elif card.inUsedCommandZone:
                card.draw(surface, card.cardCount, "USED")
            elif card.inIncomingCommandZone:
                card.draw(surface, card.cardCount, "INCOMING")
            else:
                card.draw(surface, self.cardsInMainZone.index(card), "MAIN")

            if card.is_hovered:
                pygame.draw.rect(surface, (255, 255, 0), card.rect, 3)  # Adjust the color and line width as needed
    
    def sort(self):
        self.cards.sort(key=lambda card: card.z)

    def newCard(self):
        if self.cardsInIncomingZone.__len__() > 0:
            drawCard = self.cardsInIncomingZone[0]
            self.cardsInIncomingZone = [drawCard] + self.cardsInIncomingZone[1:]  
            self.cardsInMainZone.append(drawCard)
            self.cardsInIncomingZone.remove(drawCard)
            drawCard.inMainZone = True
            drawCard.inIncomingCommandZone = False

    def update(self, mouse_pos):            
        foundHovered = False
        for card in self.cards:
            if card.is_hovered:    
                foundHovered = True
        
        for card in self.cards:
            card.update(mouse_pos, foundHovered)      
            if card.sendToCommand:
                self.addCardToCommandZone(card)
                card.inMainZone = False
                card.inCommandZone = True
                card.is_hovered = False

            
      
                
    def handle_event(self, events):       
        for card in self.cards:
            if card.is_hovered:                
                card.z = 1     
                self.cards.sort()       
            card.handle_event(events) 
       

    
        
        