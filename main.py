
from classes import Table, Player, AiPlayer
from constants import EXPANSION
from expansions import get_cards

if __name__ == '__main__':
    # TODO: Create all BASE cards classes

    in_game_cards = get_cards([EXPANSION.BASE])
    table = Table(in_game_cards)
    players = [
        Player('Caio', table),
        AiPlayer('John', table),
    ]
    table.players = players
    table.start_game()

    for _ in range(5):
        for player in table.players:
            print(f'Player {player.name} turn:')
            player.phase_draw()
            player.phase_act()
            player.phase_build()
            player.increment_village()
    table.end_game()
    print('End game!')
    for player in table.players:
        print(f'{player.name} gold: {player.score}')
