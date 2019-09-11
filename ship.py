import pygame


class Ship:
    """Represents the player ship for Alien Invasion game"""

    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('resources/images/Player_Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
