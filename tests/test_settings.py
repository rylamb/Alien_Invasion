import unittest
import sys
sys.path.append("../")

from settings import Settings


class SettingsTestCase(unittest.TestCase):

    def setUp(self):
        self.settings = Settings()

    def test_get_screen_width(self):
        self.assertEqual(self.settings.get_screen_width(), 1200)

    def test_get_screen_height(self):
        self.assertEqual(self.settings.get_screen_height(), 800)

    def test_get_background_color(self):
        self.assertEqual(self.settings.get_background_color(), (5, 5, 5))


if __name__ == '__main__':
    unittest.main()
