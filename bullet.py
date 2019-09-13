import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Represents a bullet fired by a ship"""

    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Create bullet and place at correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Update the position of the bullet"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
