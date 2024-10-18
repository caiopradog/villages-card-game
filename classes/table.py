from .deck import Deck


class Table:
    def __init__(self, expansions):
        self.players = []
        self.deck = Deck(expansions)
        self.deck.fill_deck()
        self.deck.shuffle()
        self.discard = Deck()

    def draw_player_cards(self, player, qtd):
        deck = self.deck
        if not len(deck):
            deck = self.discard
            deck.shuffle()
        player.draw_cards(qtd)

    def start_game(self):
        for player in self.players:
            self.draw_player_cards(player, 8)

    def reset_decks(self):
        self.discard.reset()
        self.deck.reset()
        self.deck.fill_deck()

    def end_game(self):
        for player in self.players:
            player.count_score()
        self.reset_decks()
