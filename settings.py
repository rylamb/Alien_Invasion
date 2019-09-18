class Settings:
    """Stores the settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (5, 5, 5)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 240, 240, 240
        self.bullets_allowed = 3
