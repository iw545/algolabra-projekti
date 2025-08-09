import unittest
from main import RPS, MarkovChain

markov1 = MarkovChain([0,1,1,0,-1])
markov2 = MarkovChain([-1,-1,0,1,0])
markov3 = MarkovChain([1,-1,1,1,0])
markov_models = [markov1, markov2, markov3]

class TestRPS(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.game = RPS(markov_models)

    def test_compare_result_valid(self):
        value = self.game.compare(1)
        self.assertIn(value, [1,2,3])

    def test_computer_choose_result_valid(self):
        value = self.game.computer_choose(1)
        self.assertIn(value, [1,2,3])

    def test_search_and_update_result_valid(self):
        value = self.game.search_and_update("RPS", 1)
        self.assertIn(value, ["R", "P", "S"])

    def test_history_accumulates_characters(self):
        value = self.game.compare(1)
        self.assertEqual(len(self.game.history), 1)

    def test_dict_keys_update(self):
        value = self.game.search_and_update("RPS", 1)
        self.assertEqual(len(self.game.current_markov.matrix), 1)


