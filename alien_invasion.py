import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """An Alien Invasion game"""

    def __init__(self):
        """Initialize game, settings, and create screen object"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.player_ship = Ship(self.settings, self.screen)
        pygame.display.set_caption("Alien Invasion")
        self.bullets = Group()

    def run_game(self):
        """Control game loop for Alien Invasion"""
        while True:
            self.check_events()
            self.player_ship.update()
            self.update_bullets()
            self.draw_screen()

    def update_bullets(self):
        """Update position of bullets and remove old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.set_moving_right(False)
        if event.key == pygame.K_LEFT:
            self.player_ship.set_moving_left(False)

    def check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.set_moving_right(True)
        if event.key == pygame.K_LEFT:
            self.player_ship.set_moving_left(True)
        if event.key == pygame.K_SPACE:
            self.fire_bullet()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.player_ship)
            self.bullets.add(new_bullet)

    def draw_screen(self):
        """Draw screen and blend images"""
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player_ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
