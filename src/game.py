import pygame
from src.player import Player
from src.enemy import Enemy
from src.backgroundStuff import BackgroundStuff as Background

class Game:
    ENEMY_CARD_CENTER = (400, 400)
    PLAYER_CARD_CENTER = (800, 400)
    VS_CENTER = (600, 400)
    VS_IMAGE_URL = "assets/VS.png"
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ASTRO GAMBIT")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self.PLAYER_CARD_CENTER, 100, 200, 20,(0, 255, 0)) 
        self.enemy = Enemy(self.ENEMY_CARD_CENTER, 100, 200, 20, (0, 255, 0)) 
        self.backgroundVS = Background(self.VS_CENTER, self.VS_IMAGE_URL)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit to 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Update game logic here

    def render(self):
        # Render game elements here

        #clear
        self.screen.fill((0, 0, 0))

        #backgrounds
        self.backgroundVS.draw(self.screen)

        #players
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
