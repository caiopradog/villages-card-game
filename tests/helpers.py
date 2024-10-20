from table import Table, AiPlayer
from constants import EXPANSION


def add_card_to_player_village(player, village, card):
    player.hand.add_card(card)
    player.add_card_to_village(village, card)


def setup_table(qtd_players: int) -> Table:
    table = Table([EXPANSION.BASE], is_testing=True)
    players = [
        AiPlayer('Red', table),
        AiPlayer('Blue', table),
        AiPlayer('Green', table),
        AiPlayer('Yellow', table),
        AiPlayer('Purple', table),
    ]
    table.players = players[0:qtd_players]

    return table


def simulate_game(rounds, qtd_players: int):
    table = setup_table(qtd_players)
    table.start_game()
    for i in range(rounds):
        table.play_round()
