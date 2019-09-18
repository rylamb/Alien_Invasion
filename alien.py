import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents a alien ship that is part of a fleet"""

    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load image and set rectangle
        self.image = pygame.image.load('resources/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Set starting location at top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
        return False
