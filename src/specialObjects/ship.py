import pygame
import random
from src.player.cardType import CardType

class Ship:
    PADDING = 200
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    FLEET_ZONE_COODS = (600, 200)
    SHIP_HEIGHT = 100
    SHIP_WIDTH = 100
    FLEET_X = 600
    FLEET_Y = 200

    def __init__(self, x, y, image_paths, name, size, arrival):
        self.x = x
        self.y = y
        self.name = name
        self.size = size
        self.fleet_x = self.FLEET_X
        self.fleet_y = self.FLEET_Y
        self.image_paths = image_paths  # List of image file paths
        self.images = [pygame.image.load(path) for path in image_paths]
        self.image_index = 0  # Index to track the current image
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.origX = self.rect.x
        self.origY = self.rect.y
        self.left_boundary = self.FLEET_ZONE_COODS[0] - 50
        self.right_boundary = self.FLEET_ZONE_COODS[0] + 200
        self.top_boundary = self.FLEET_ZONE_COODS[1] - 100
        self.bottom_boundary = self.FLEET_ZONE_COODS[1] 
        self.animation_speed = 6  
        self.animation_counter = 0
        self.movingRight = False
        self.movingDown = True
        # Probability of changing direction
        self.change_direction_probability = 0.001 # Adjust as needed

        self.shipArrivalImages_Paths = ["assets/arrrivalPortal.png","assets/arrrivalPortal2.png","assets/arrrivalPortal3.png"]
        self.shipArrivalImages = [pygame.image.load(path) for path in self.shipArrivalImages_Paths]       
        self.arrivalRect = self.shipArrivalImages[0].get_rect()
        self.arrivalRect.center = (50, 50)

        # Laser animation properties
        self.laser_images = [pygame.image.load(f"assets/laser{i}.png") for i in range(1, 4)]  # Load laser images 1, 2, and 3
        self.laser_rect = None  # Rectangle to position the laser image
        self.laser_animation_index = 0  # Index to track the current laser image
        self.is_shooting = False  # Flag to indicate if the ship is shooting

        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.name, True, self.BLACK)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height)

        self.frame_counter = 0
        self.arrival = arrival
        self.arrivalDraw = False

        if arrival:
            self.rect.x = -10
            self.rect.y = 0
            self.arrival = True
            self.arrivalDraw = True
            self.target_x = 600  # Set the target x-coordinate
            self.target_y = 200  # Set the target y-coordinate
        

    def info(self):
        return f"Ship name: {self.name}, Size: {self.size}"
    

    def update(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_counter = 0

        if self.arrival:
                # Calculate horizontal and vertical movement directions
            # Calculate horizontal and vertical movement directions
            if self.rect.x > self.target_x or self.rect.y > self.target_y:
                self.arrival = False  # Set arrival to True when both conditions are met
            else:
                self.rect.x += 4
                self.rect.y += 1          
        else:                       


            if self.movingRight:
                self.rect.x += 1
            else:
                self.rect.x -= 1

            # Calculate vertical movement direction
            if self.movingDown:
                self.rect.y += 1
            else:
                self.rect.y -= 1

            # Check and handle horizontal boundaries
            # Check and handle horizontal boundaries
            if self.rect.x >= self.right_boundary:
                self.movingRight = False
            elif self.rect.x <= self.left_boundary:
                self.movingRight = True

            # Check and handle vertical boundaries
            if self.rect.y >= self.bottom_boundary:
                self.movingDown = False
            elif self.rect.y <= self.top_boundary:
                self.movingDown = True


            if random.random() < self.change_direction_probability:
                horizontal_change = random.choice([True, False])  # Randomly set the horizontal direction
                vertical_change = random.choice([True, False])   # Randomly set the vertical direction

                if horizontal_change:
                    self.movingRight = random.choice([True, False])
                if vertical_change:
                    self.movingDown = random.choice([True, False])



        # Update the laser animation
            # Update the laser animation if shooting
        if self.is_shooting:
            # Control the animation speed with a frame counter
            self.frame_counter += 1

            # Update the animation every, for example, 5 frames (adjust this value)
            if self.frame_counter % 5 == 0:
                # Position the laser image at the ship's top
                self.laser_rect.centerx = self.rect.centerx
                self.laser_rect.x = self.rect.right 
                self.laser_rect.y -= 10  # Adjust this value for the laser's vertical speed

                # Advance to the next laser image
                self.laser_animation_index += 1
                if self.laser_animation_index >= len(self.laser_images):
                    self.is_shooting = False  # End the animation when all frames are displayed

                # Reset the frame counter
                self.frame_counter = 0



    def start_laser_animation(self):
        # Start the laser animation
        self.is_shooting = True
        self.laser_animation_index = 0
        self.laser_rect = self.rect.copy()
        self.laser_rect.x += 300 
        
    arrivalDrawTime = 1
    imageInd = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.arrivalDraw:
            if self.arrivalDrawTime == 10:
                self.imageInd  += 1
            elif self.arrivalDrawTime == 20:
                self.imageInd  += 1
            
            if self.arrivalDrawTime < 30:
                self.arrivalDrawTime += 1
                surface.blit(self.shipArrivalImages[self.imageInd], self.arrivalRect)
            else:
                self.arrivalDrawTime = 0
                self.imageInd = 0
                self.arrivalDraw = False

        #Draw the laser image if shooting
        if self.is_shooting and self.laser_rect:
            surface.blit(self.laser_images[self.laser_animation_index], self.laser_rect)
