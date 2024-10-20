import unittest
from tests import helpers


class TestScoring(unittest.TestCase):
    def setUp(self):
        self.table = helpers.setup_table(3)

    def test_lowscorer(self):
        self.table.players[0].score = 10
        self.table.players[1].score = 20
        self.table.players[2].score = 30
        lowscorer = self.table.get_lowscore_player()
        self.assertIs(lowscorer, self.table.players[0])

    def test_lowscore_draw(self):
        self.table.players[0].score = 10
        self.table.players[1].score = 10
        self.table.players[2].score = 20
        lowscorer = self.table.get_lowscore_player()
        self.assertIs(lowscorer, None)

    def test_highscorer(self):
        self.table.players[0].score = 10
        self.table.players[1].score = 20
        self.table.players[2].score = 30
        highscorer = self.table.get_highscore_player()
        self.assertIs(highscorer, self.table.players[2])

    def test_highscore_draw(self):
        self.table.players[0].score = 10
        self.table.players[1].score = 20
        self.table.players[2].score = 20
        highscorer = self.table.get_highscore_player()
        self.assertIs(highscorer, None)
