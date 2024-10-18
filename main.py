from classes import Table, Player, AiPlayer
from constants import EXPANSION
from classes.players.aiplayer import choose_random as choose_option

if __name__ == '__main__':
    table = Table([EXPANSION.BASE])
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
