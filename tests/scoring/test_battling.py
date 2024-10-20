import unittest
import cards
from tests import helpers
from table import Player


class TestBattling(unittest.TestCase):
    def setUp(self):
        self.table = helpers.setup_table(2)
        self.att_player: Player = self.table.players[0]
        self.def_player: Player = self.table.players[1]
        self.att_player.attacked_player = self.def_player

    def set_battle_data(self, att_card, def_village, def_card):
        self.att_player.attacking_card = att_card
        self.att_player.attacked_village = def_village
        self.att_player.defending_card = def_card

    def test_win_from_village(self):
        att_village = 'red'
        def_village = 'blue'

        att_card = cards.Dragon(att_village)
        def_card = cards.Princess(def_village)

        helpers.add_card_to_player_village(self.att_player, att_village, att_card)
        helpers.add_card_to_player_village(self.def_player, def_village, def_card)

        self.set_battle_data(att_card, def_village, def_card)
        self.att_player.attack_player()

        self.assertTrue(self.att_player.battle_won)
        self.att_player.resolve_after_battle()
        self.assertIn(att_card, self.att_player.villages[att_village])

    def test_win_from_hand(self):
        att_village = 'red'
        def_village = 'blue'

        att_card = cards.Dragon(att_village)
        def_card = cards.Princess(def_village)

        self.att_player.hand.add_card(att_card)
        self.def_player.hand.add_card(def_card)

        self.set_battle_data(att_card, def_village, def_card)
        self.att_player.attack_player()

        self.assertTrue(self.att_player.battle_won)
        self.att_player.resolve_after_battle()
        self.assertNotIn(att_card, self.att_player.hand)
        self.assertNotIn(def_card, self.def_player.hand)

    def test_lose_from_village(self):
        att_village = 'red'
        def_village = 'blue'

        att_card = cards.Princess(att_village)
        def_card = cards.Dragon(def_village)

        helpers.add_card_to_player_village(self.att_player, att_village, att_card)
        helpers.add_card_to_player_village(self.def_player, def_village, def_card)

        self.set_battle_data(att_card, def_village, def_card)
        self.att_player.attack_player()

        self.assertFalse(self.att_player.battle_won)
        self.att_player.resolve_after_battle()
        self.assertNotIn(att_card, self.att_player.villages[att_village])

    def test_lose_from_hand(self):
        att_village = 'red'
        def_village = 'blue'

        att_card = cards.Princess(att_village)
        def_card = cards.Dragon(def_village)

        self.att_player.hand.add_card(att_card)
        self.def_player.hand.add_card(def_card)

        self.set_battle_data(att_card, def_village, def_card)
        self.att_player.attack_player()

        self.assertFalse(self.att_player.battle_won)
        self.att_player.resolve_after_battle()
        self.assertNotIn(att_card, self.att_player.hand)
        self.assertNotIn(def_card, self.def_player.hand)
