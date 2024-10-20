from .deck import Deck
from expansions import get_cards


class Table:
    def __init__(self, expansions, is_testing=False):
        self.players = []
        in_game_cards = get_cards(expansions)
        self.deck = Deck(in_game_cards)
        self.deck.fill_deck()
        self.deck.shuffle()
        self.discard = Deck()
        self.is_testing = is_testing

    def get_highscore_player(self):
        highscore = (0, None)
        draw = False
        for player in self.players:
            if player.score > highscore[0]:
                highscore = (player.score, player)
                draw = False
            elif player.score == highscore[0]:
                draw = True
        return None if draw else highscore[1]

    def get_lowscore_player(self):
        lowscore = (999, None)
        draw = False
        for player in self.players:
            if player.score < lowscore[0]:
                lowscore = (player.score, player)
                draw = False
            elif player.score == lowscore[0]:
                draw = True
        return None if draw else lowscore[1]

    def draw_player_cards(self, player, qtd):
        deck = self.deck
        if not len(deck):
            deck = self.discard
            deck.shuffle()
        player.draw_cards(qtd)

    def start_game(self):
        for player in self.players:
            self.draw_player_cards(player, 8)

    def play_round(self):
        for player in self.players:
            print(f'Player {player.name} turn:')
            player.phase_draw()
            player.phase_act()
            player.phase_build()
            player.increment_village()

    def reset_decks(self):
        self.discard.reset()
        self.deck.reset()
        self.deck.fill_deck()

    def end_game(self):
        for player in self.players:
            player.count_score()
        self.reset_decks()
