import unittest
from main import RPS

class TestRPS(unittest.TestCase):
    def setUp(self):
        print("setup")

    def test_pelaa_kierros_pisteet_kertyy(self):
        game = RPS()
        game.compare(1)
        self.assertEqual(game.points, 1)