from table import Table, Player, AiPlayer
from constants import EXPANSION

if __name__ == '__main__':
    # TODO: Program abilities (use unittests to test each card)

    table = Table([EXPANSION.BASE])
    players = [
        AiPlayer('Steve', table),
        AiPlayer('John', table),
        AiPlayer('Stanley', table),
    ]
    table.players = players
    table.start_game()

    for _ in range(5):
        table.play_round()
    table.end_game()
    print('End game!')
    for player in table.players:
        print(f'{player.name} gold: {player.score}')
