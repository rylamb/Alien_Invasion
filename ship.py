import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Represents the player ship for Alien Invasion game"""

    def __init__(self, settings, screen):
        """Initialize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('resources/images/Player_Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def set_moving_right(self, value):
        self.moving_right = value

    def set_moving_left(self, value):
        self.moving_left = value

    def update(self):
        """Update ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
        # Update ship rectangle center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
