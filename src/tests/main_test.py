import unittest
from unittest.mock import patch
from main import RPS

class TestRPS(unittest.TestCase):
    def setUp(self):
        print("setup")

    @patch('main.play', return_value='1')
    def test_pelaa_kierros_pisteet_kertyy(self, input):
        game = RPS()
        game.compare(1)
        self.assertEqual(len(game.results), 1)

    @patch('main.play', return_value='1')
    def test_tietokone_valinta(self, input):
        game = RPS()
        option = game.computer_choose()
        self.assertIn(option, [1,2,3])
