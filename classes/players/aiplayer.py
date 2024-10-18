import random
from . import Player
from .. import Deck, Card


def choose_random(options, min_choice: int = 1, max_choice: int = 1):
    if max_choice == -1:
        max_choice = len(options)
    chosen = random.sample(list(options), k=random.randint(min_choice, max_choice))
    return chosen if len(chosen) > 1 else chosen[0]


class AiPlayer(Player):
    def __init__(self, name, table):
        super().__init__(name, table)

    def choose_village_to_build(self):
        colors = self.get_villages_to_build()
        if len(colors) == 0:
            return None

        return choose_random(colors)

    def choose_action(self, actions):
        action = 'attack' if 'attack' in actions else choose_random(actions)
        print(f'{self.name} has chosen {action}')
        return action

    def choose_card_from_hand(self, min_choice=1, max_choice=1):
        card = choose_random(self.hand, min_choice=min_choice, max_choice=max_choice)
        print(f'{self.name} has chosen {card} from hand')
        return card

    def choose_card_to_discard(self):
        return self.choose_card_from_hand(max_choice=1)

    def choose_card_to_battle(self, options, side_battle) -> (Card, Deck):
        card = choose_random(options)
        origin = self.hand if card in self.hand else self.get_villagers_village(card)
        origin_type = 'hand' if card in self.hand else card.color
        print(f"{self.name} has chosen {card} from {origin_type}'s village to battle!")
        return card, origin, origin_type

    def choose_card_to_trade(self):
        return self.choose_card_from_hand()

    def choose_player_to_attack(self):
        return choose_random(self.get_attackable_players())

    def choose_battle_reward(self, rewards):
        reward = choose_random(rewards)
        print(f'{self.name} has chosen {reward} as battle reward!')
        return reward

    def choose_villager_from_village(self, color, player=None):
        if player is None:
            player = self
        villager = choose_random(player.villages[color])
        print(f'{self.name} has kidnapped {villager}!')
        return villager

    def choose_village_to_attack(self, attacked_player):
        attacked_village = choose_random(attacked_player.get_built_villages())
        print(f"{self.name} will attack {attacked_player.name}'s {attacked_village} village!")
        return attacked_village

    def choose_cards_to_build(self, available_cards):
        chosen_cards = choose_random(available_cards, min_choice=3, max_choice=-1)
        print(f"{self.name} will build a village with {chosen_cards}!")
        return chosen_cards

