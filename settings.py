class Settings:
    """Stores the settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (5, 5, 5)

    def get_screen_width(self):
        return self.screen_width

    def get_screen_height(self):
        return self.screen_height

    def get_background_color(self):
        return self.background_color
