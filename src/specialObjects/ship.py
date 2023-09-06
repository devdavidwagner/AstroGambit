import pygame
import random

class Ship:
    PADDING = 20
    def __init__(self, x, y, image_paths, name, size):
        self.x = x
        self.y = y
        self.name = name
        self.size = size
        self.image_paths = image_paths  # List of image file paths
        self.images = [pygame.image.load(path) for path in image_paths]
        self.image_index = 0  # Index to track the current image
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.origX = self.rect.x
        self.origY = self.rect.y
        self.left_boundary = self.origX - self.PADDING  # Adjust for your specific range
        self.right_boundary = self.origX + self.PADDING
        self.top_boundary = self.origY - self.PADDING  # Adjust for your specific range
        self.bottom_boundary = self.origY + self.PADDING
        self.animation_speed = 4  
        self.animation_counter = 0
        self.movingRight = False
        self.movingDown = True
        # Probability of changing direction
        self.change_direction_probability = 0.1  # Adjust as needed

        # Laser animation properties
        self.laser_images = [pygame.image.load(f"assets/laser{i}.png") for i in range(1, 4)]  # Load laser images 1, 2, and 3
        self.laser_rect = None  # Rectangle to position the laser image
        self.laser_animation_index = 0  # Index to track the current laser image
        self.is_shooting = False  # Flag to indicate if the ship is shooting

        self.frame_counter = 0
        

    def info(self):
        return f"Ship name: {self.name}, Size: {self.size}"

    def update(self):
        # Update the animation frame
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_counter = 0

        # Moving the ship horizontally
        if self.movingRight:
            self.rect.x += 1 
        else:
            self.rect.x -= 1 

       
        if self.rect.x >= self.right_boundary:
            self.movingRight = False
        elif self.rect.x <= self.left_boundary:
            self.movingRight = True

        # Moving the ship vertically
        if self.movingDown:
            self.rect.y += 1  # Move down
        else:
            self.rect.y -= 1  # Move up

        # Check boundaries and change direction
        if self.rect.y >= self.bottom_boundary or self.rect.y <= self.top_boundary:
        # Introduce randomness to change direction
            if random.random() < self.change_direction_probability:
                self.movingDown = not self.movingDown

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
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # Draw the laser image if shooting
        if self.is_shooting and self.laser_rect:
            surface.blit(self.laser_images[self.laser_animation_index], self.laser_rect)
