import pygame
from src.player import Player
from src.enemy import Enemy
from src.backgroundStuff import BackgroundStuff as Background
from src.widgets.button import Button

class Game:
    ENEMY_CARD_CENTER = (400, 400)
    PLAYER_CARD_CENTER = (400, 400)
    VS_CENTER = (600, 400)
    VS_IMG_URL = "assets/VS.png"
    SHIP_IMG_URLS = ("assets/spaceShip.png", "assets/spaceShip2.png","assets/spaceShip3.png")
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ASTRO GAMBIT")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self.PLAYER_CARD_CENTER, 100, 200, 20,(0, 255, 0), self.SHIP_IMG_URLS, 100, 100) 
       # self.enemy = Enemy(self.ENEMY_CARD_CENTER, 100, 200, 20, (0, 255, 0)) 
        #self.backgroundVS = Background(self.VS_CENTER, self.VS_IMG_URL)
        self.orderButton = Button((self.screen.get_width() / 2) - 100, 500, 200, 200, "COMMAND", (100, 100, 100))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def run(self):
        while self.running:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit to 60 FPS

    def handle_events(self):
        self.orderButton.check_hover((self.mouse_x, self.mouse_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                self.orderButton.check_hover(mouse_pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.orderButton.check_click(mouse_pos):
                    self.player.ship.start_laser_animation()  # Call ship method to start laser animation

    def update(self):
        self.player.update()
        
        # Update game logic here

    def render(self):
        # Render game elements here

        #clear
        self.screen.fill((0, 0, 0))

        #backgrounds
       # self.backgroundVS.draw(self.screen)

        #players
        self.player.draw(self.screen)
       # self.enemy.draw(self.screen)
        self.orderButton.draw(self.screen)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
