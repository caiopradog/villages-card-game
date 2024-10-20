from constants import COLOR, TYPE
import uuid
from helper import choose_option
from .. import Deck
from typing import Self
from cards import BaseCard


def count_gold(cards):
    gold = 0
    for card in cards:
        gold += card.gold
    return gold


class Player:
    def __init__(self, name, table):
        self.id = uuid.uuid4()
        self.name = name
        self.villages = {
            COLOR.RED: Deck(),
            COLOR.DARK: Deck(),
            COLOR.BLUE: Deck(),
            COLOR.GREEN: Deck(),
            COLOR.YELLOW: Deck(),
            COLOR.PURPLE: Deck(),
            COLOR.ORANGE: Deck(),
        }
        self.hand = Deck()
        self.cemetery = Deck()
        self.score = 0
        self.table = table

        # Battle Data
        self.attacking_card: BaseCard | None = None
        self.attacked_player: Self | None = None
        self.attacked_village = None
        self.defending_card: BaseCard | None = None
        self.kidnapped_villager: BaseCard | None = None
        self.battle_won = None

    # GETTERS
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def title(self) -> str:
        return self.name.title()

    def get_villages_to_build(self) -> [str]:
        hand_by_colors = {}
        for card in self.hand:
            if card.color == COLOR.GRAY:
                continue

            if card.color not in hand_by_colors:
                hand_by_colors[card.color] = []
            hand_by_colors[card.color].append(card)

            if card.color2:
                if card.color2 not in hand_by_colors:
                    hand_by_colors[card.color2] = []
                hand_by_colors[card.color2].append(card)
        return [color for color in hand_by_colors if len(hand_by_colors[color]) >= 3]

    def get_built_villages(self) -> [str]:
        return [village for village in self.villages if len(self.villages[village])]

    def get_attackable_players(self) -> [Self]:
        attackable_players = []
        for player in self.get_opponents():
            if player.get_built_villages():
                attackable_players.append(player)

        return attackable_players

    def get_opponents(self) -> [Self]:
        return [player for player in self.table.players if player != self]

    def get_all_villagers(self) -> [BaseCard]:
        return [card for color in self.villages for card in self.villages[color]]

    def get_available_actions(self) -> [str]:
        actions = ['discard']
        if self.get_attackable_players():
            actions.append('attack')
        if self.get_villagers('merchant'):
            actions.append('trade')
        return actions

    def get_villagers_village(self, villager) -> Deck:
        return self.villages[villager.color]

    def get_villagers(self, unit=None, color=None) -> [BaseCard]:
        return [
            card for card in self.get_all_villagers()
            if (unit is None or (unit is not None and unit == card.unit))
            and (color is None or (color is not None and color == card.color))
        ]

    def get_colors_in_hand(self) -> [str]:
        colors = [card.color for card in self.hand]
        return list(set(colors))

    def get_animals_in_hand(self) -> [BaseCard]:
        return [card for card in self.hand if card.type == TYPE.ANIMAL]

    def get_buildings_in_hand(self) -> [BaseCard]:
        return [card for card in self.hand if card.type == TYPE.BUILDING]

    def get_villager_in_village(self, color, unit) -> [BaseCard]:
        return [card for card in self.villages[color] if card.unit == unit]

    def village_supports_animals(self, color) -> [BaseCard]:
        return [card for card in self.villages[color] if card.unit in ['farmer']]

    def village_supports_buildings(self, color) -> [BaseCard]:
        return [card for card in self.villages[color] if card.unit in ['builder']]

    def get_cards_in_hand(self, key, value):
        return [card for card in self.hand if getattr(card, key) == value]

    def get_incrementable_villages(self) -> dict:
        built_villages = self.get_built_villages()

        available_villages = {}
        for village in built_villages:
            color_cards_in_hand = self.get_cards_in_hand('color', village)
            if len(color_cards_in_hand) > 0:
                available_villages[village] = self.get_cards_in_hand('color', village)
                if self.village_supports_animals(village):
                    available_villages[village] += self.get_cards_in_hand('type', TYPE.ANIMAL)

                if self.village_supports_buildings(village):
                    available_villages[village] += self.get_cards_in_hand('type', TYPE.BUILDING)

        return available_villages

    def get_cards_to_add_to_villages(self) -> [BaseCard]:
        return [card for card in self.hand if card.color in self.get_built_villages()]

    def get_card_to_battle(self, village=None) -> BaseCard:
        options = self.hand + self.get_villagers(color=village)
        options = [card for card in options if card.type == TYPE.UNIT]
        side_battle = 'attack' if village is None else 'defend'
        return self.choose_card_to_battle(options, side_battle)

    def get_card_origin(self, card):
        origin = self.hand if card in self.hand else self.get_villagers_village(card)
        origin_type = 'hand' if card in self.hand else card.color
        return origin, origin_type

    # END GETTERS

    # CHOOSERS
    def choose_village_to_build(self) -> str | None:
        available_to_build = self.get_villages_to_build()
        if len(available_to_build) == 0:
            return None

        return choose_option(available_to_build, f'Choose a village to build: ')

    def choose_action(self, actions) -> str:
        return choose_option(actions, 'Choose an act: ', optional=False)

    def choose_card_from_hand(self, reason, optional=False) -> BaseCard:
        text = f'Choose a card to {reason}: '
        return choose_option(self.hand, text, optional=optional)

    def choose_player_to_attack(self) -> Self:
        players = self.get_attackable_players()
        return choose_option(players, 'Choose player to attack: ', optional=False)

    def choose_player_to_trade(self) -> Self:
        return choose_option(self.get_opponents(), 'Choose player to trade: ', optional=False)

    def choose_card_to_discard(self) -> BaseCard:
        return self.choose_card_from_hand('discard')

    def choose_card_to_trade(self) -> BaseCard:
        return self.choose_card_from_hand('trade')

    def choose_card_to_battle(self, options, side_battle) -> BaseCard:
        return choose_option(options, f'Choose a villager to {side_battle}: ', optional=False)

    def choose_battle_reward(self, rewards):
        return choose_option(rewards, 'Choose battle reward: ', page_count=3, optional=False)

    def choose_village_to_attack(self, attacked_player) -> str:
        return choose_option(attacked_player.get_built_villages(),
                             'Choose village to attack: ',
                             page_count=4,
                             optional=False)

    def choose_villager_from_village(self, color, player=None):
        if player is None:
            player = self
        return choose_option(player.villages[color], 'Choose villager: ', optional=False)

    def choose_cards_to_build(self, cards):
        return choose_option(cards, 'Choose cards to build: ', optional=False, min_choice=3, max_choice=-1)

    def choose_village_to_increment(self):
        return choose_option(
            list(self.get_incrementable_villages()),
            'Choose a village to increment: ',
            optional=False,
            max_choice=1
        )

    def choose_cards_to_add_to_village(self, village):
        available_cards = self.get_incrementable_villages()[village]
        return choose_option(available_cards, 'Choose cards to add to village: ', max_choice=-1)
    # END CHOOSERS

    # ACTIONS
    def draw_cards(self, qtd):
        self.hand.add_cards(self.table.deck.draw_cards(qtd))

    def destroy_card(self, deck, card):
        deck.remove_card(card)
        self.cemetery.add_card(card)

    def discard_card(self, card):
        self.hand.remove_card(card)
        self.table.discard.add_card(card)

    def show_hand(self):
        self.hand.show_deck()

    def count_score(self):
        positive = count_gold(self.get_all_villagers())
        negative = count_gold(list(self.hand) + list(self.cemetery)) * -1
        self.score += positive - negative

    def build_village(self, color):
        available_cards = [card for card in self.hand if card.color == color]
        chosen_cards = self.choose_cards_to_build(available_cards)
        self.hand.remove_cards(chosen_cards)
        self.villages[color].add_cards(chosen_cards)

    def add_card_to_village(self, village: str, card: BaseCard):
        self.villages[village].add_card(card)
        self.hand.remove_card(card)

    def add_cards_to_village(self, village: str, cards: [BaseCard]):
        for card in cards:
            self.add_card_to_village(village, card)

    def attack_player(self):
        if not self.table.is_testing:
            print(f'{self.attacking_card} vs {self.defending_card}!')
        self.battle_won = self.attacking_card.power >= self.defending_card.power

    def destroy_opponent_card(self, card):
        opponent = self.attacked_player
        (deck, deck_name) = opponent.get_card_origin(card)
        opponent.destroy_card(deck, card)

    def remove_opponent_card(self, card):
        opponent = self.attacked_player
        (deck, deck_name) = opponent.get_card_origin(card)
        deck.remove_card(card)

    def kidnap_opponent_card(self, card):
        self.remove_opponent_card(card)
        self.hand.add_card(card)

    def destroy_opponent_defender(self):
        self.destroy_opponent_card(self.defending_card)

    def resolve_battle_reward(self, reward):
        if reward == 'destroy defender':
            self.destroy_opponent_defender()
        else:
            self.kidnap_opponent_card(self.kidnapped_villager)

    def resolve_after_battle(self):
        (att_deck, att_deck_name) = self.get_card_origin(self.attacking_card)
        if not self.battle_won or att_deck_name == 'hand':
            origin_text = 'hired' if att_deck_name == 'hand' else 'defeated'
            if not self.table.is_testing:
                print(f'Attacking {origin_text} unit {self.attacking_card} discarded!')
            self.destroy_card(att_deck, self.attacking_card)

        (def_deck, def_deck_name) = self.attacked_player.get_card_origin(self.defending_card)
        if self.kidnapped_villager != self.defending_card and def_deck_name == 'hand':
            if not self.table.is_testing:
                print(f'Defending hired unit {self.defending_card} discarded!')
            self.attacked_player.destroy_card(def_deck, self.defending_card)

    def reset_battle_data(self):
        self.attacking_card = None
        self.attacked_player: Self = None
        self.attacked_village = None
        self.defending_card = None
        self.kidnapped_villager = None
        self.battle_won = None

    # END ACTIONS

    # PHASES
    def phase_draw(self):
        self.draw_cards(2)

    def phase_build(self):
        color = self.choose_village_to_build()
        if color is None:
            return
        self.build_village(color)

    def phase_act_attack(self):
        self.attacking_card = self.get_card_to_battle()
        self.attacked_player = self.choose_player_to_attack()
        self.attacked_village = self.choose_village_to_attack(self.attacked_player)
        self.defending_card = self.attacked_player.get_card_to_battle(self.attacked_village)
        self.attack_player()

        if self.battle_won:
            print('Battle Won!')
            reward = self.choose_battle_reward(['destroy defender', 'kidnap defender', 'kidnap villager'])
            if reward == 'kidnap villager':
                self.kidnapped_villager = self.choose_villager_from_village(self.attacked_village, self.attacked_player)
            elif reward == 'kidnap defender':
                self.kidnapped_villager = self.defending_card
            self.resolve_battle_reward(reward)
        else:
            print('Battle Lost!')
        self.resolve_after_battle()
        self.reset_battle_data()

    def phase_act_trade(self):
        giving_card = self.choose_card_to_trade()
        trading_player = self.choose_player_to_trade()
        receiving_card = trading_player.choose_card_to_trade()

        self.hand.remove_card(giving_card)
        trading_player.hand.add_card(giving_card)
        self.hand.add_card(receiving_card)
        trading_player.hand.remove_card(receiving_card)

    def phase_act_discard(self):
        card = self.choose_card_to_discard()
        self.discard_card(card)

    def phase_act(self):
        available_actions = self.get_available_actions()
        action = self.choose_action(available_actions)
        if action == 'attack':
            self.phase_act_attack()
        elif action == 'trade':
            self.phase_act_trade()
        else:
            self.phase_act_discard()

    def increment_village(self):
        villages_to_increment = self.get_incrementable_villages()
        if len(villages_to_increment) == 0:
            return
        chosen_village = self.choose_village_to_increment()
        chosen_cards = self.choose_cards_to_add_to_village(chosen_village)
        self.add_cards_to_village(chosen_village, chosen_cards)
    # END PHASES
