class Settings:
    """Stores the settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (5, 5, 5)

        # Ship settings
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 240, 240, 240
        self.bullets_allowed = 3

        # How quickly game speeds up
        self.speedup_scale = 1.1

        # How quickly point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
