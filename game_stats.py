class GameStats:
    """Tracks stats for alien invasion"""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit

