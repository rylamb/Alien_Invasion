import sys
from time import sleep

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
        self.aliens = Group()
        self.create_fleet()
        self.stats = GameStats(self.settings)
        self.play_button = Button(self.settings, self.screen, "Play")
        self.sb = Scoreboard(self.settings, self.screen, self.stats)

    def run_game(self):
        """Control game loop for Alien Invasion"""
        while True:
            self.check_events()

            if self.stats.game_active:
                self.player_ship.update()
                self.update_bullets()
                self.update_aliens()

            self.update_screen()

    def update_aliens(self):
        """Check if fleet is at edge, then update aliens"""
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.player_ship, self.aliens):
            self.ship_hit()
        self.check_aliens_bottom()

    def update_bullets(self):
        """Update position of bullets and remove old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
            self.check_high_score()
        if len(self.aliens) == 0:
            self.bullets.empty()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self.create_fleet()

    def check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x, mouse_y)
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
        elif event.key == pygame.K_LEFT:
            self.player_ship.set_moving_left(True)
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.player_ship)
            self.bullets.add(new_bullet)

    def update_screen(self):
        """Draw screen and blend images"""
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player_ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def create_fleet(self):
        """Create fleet of aliens"""
        # Calculate amount of aliens per row
        alien = Alien(self.settings, self.screen)
        number_aliens_x = self.get_number_aliens_x(alien.rect.width)
        number_rows = self.get_number_rows(self.player_ship.rect.height, alien.rect.height)

        # Create first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self.settings, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def get_number_aliens_x(self, alien_width):
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, ship_height, alien_height):
        """Determine number of rows of aliens that fits on the screen"""
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows

    def check_fleet_edges(self):
        """Respond appropriately if aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop entire fleet by one row"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.player_ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def check_aliens_bottom(self):
        """Check if any aliens reach the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def check_play_button(self, mouse_x, mouse_y):
        """Start new game when player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.sb.prep_score()
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.player_ship.center_ship()

    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.prep_high_score()


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
