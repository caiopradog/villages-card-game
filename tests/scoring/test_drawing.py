import unittest
from tests import helpers


class TestDrawing(unittest.TestCase):
    def setUp(self):
        self.table = helpers.setup_table(3)

    def test_single_player_draw(self):
        player = self.table.players[0]
        qtd_draw = 2
        self.table.draw_player_cards(player, qtd_draw)
        cards_drawn = player.hand
        self.assertEqual(len(cards_drawn), qtd_draw)
        self.assertNotIn(cards_drawn, self.table.deck)

    def test_no_repeating_cards(self):
        self.table.start_game()
        starting_hand = 8
        for player in self.table.players:
            self.assertEqual(len(player.hand), starting_hand)
            hand = set(player.hand)
            for opponent in player.get_opponents():
                opponent_hand = set(opponent.hand)
                self.assertFalse(any(hand.intersection(opponent_hand)))
