import unittest
from main import RPS, MarkovChain
from ai import AI

markov1 = MarkovChain([0,1,1,0,-1])
markov2 = MarkovChain([-1,-1,0,1,0])
markov3 = MarkovChain([1,-1,1,1,0])
markov_models = [markov1, markov2, markov3]

class TestRPS(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.game = RPS(markov_models)
        self.ai = AI()

    def test_compare_result_valid(self):
        result, computer = self.ai.compare(self.game.history, self.game.current_markov, 1)
        self.assertIn(result, [1,2,3])
        self.assertIn(computer, [1,2,3])

    def test_compare_result_two_values(self):
        result, computer = self.ai.compare(self.game.history, self.game.current_markov, 1)
        self.assertEqual(len((result, computer)), 2)

    def test_computer_choose_result_valid(self):
        value = self.ai.computer_choose(self.game.history, self.game.current_markov, 1)
        self.assertIn(value, [1,2,3])

    def test_search_and_update_result_valid(self):
        value = self.ai.search_and_update("RPS", 1, self.game.current_markov)
        self.assertIn(value, ["R", "P", "S"])

    def test_dict_keys_update(self):
        value = self.ai.search_and_update("RPS", 1, self.game.current_markov)
        self.assertEqual(len(self.game.current_markov.matrix), 1)

    def test_markov_points_correct_values(self):
        for i in markov_models:
            for j in i.results:
                self.assertIn(j, [0,1,-1])

'''
    def test_history_accumulates_characters(self):
        value = self.ai.compare(self.game.history, self.game.current_markov, 1)
        self.assertEqual(len(self.game.history), 1)
'''