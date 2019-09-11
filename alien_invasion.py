import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """An Alien Invasion game"""

    def __init__(self):
        """Initialize game, settings, and create screen object"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.get_screen_width(), self.settings.get_screen_height()))
        self.player_ship = Ship(self.settings, self.screen)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Control game loop for Alien Invasion"""
        while True:
            self.check_events()
            self.player_ship.update()
            self.draw_screen()

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
        if event.key == pygame.K_RIGHT:
            self.player_ship.set_moving_right(False)
        if event.key == pygame.K_LEFT:
            self.player_ship.set_moving_left(False)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player_ship.set_moving_right(True)
        if event.key == pygame.K_LEFT:
            self.player_ship.set_moving_left(True)

    def draw_screen(self):
        """Draw screen and blend images"""
        self.screen.fill(self.settings.get_background_color())
        self.player_ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
