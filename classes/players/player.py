from constants import COLOR, TYPE
import uuid
from helper import choose_option
from .. import Deck
from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    from cards import BaseCard


def count_gold(cards):
    gold = 0
    for card in cards:
        gold += card.gold
    return gold


def attack_card(attacker, defender):
    return attacker.power >= defender.power


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

    # GETTERS
    def title(self) -> str:
        return self.name.title()

    def destroy_card(self, deck, card):
        deck.remove_card(card)
        self.cemetery.add_card(card)

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
        for player in self.get_other_players():
            if player.get_built_villages():
                attackable_players.append(player)

        return attackable_players

    def get_other_players(self) -> [Self]:
        return [player for player in self.table.players if player != self]

    def get_all_villagers(self) -> ["BaseCard"]:
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

    def get_villagers(self, unit=None, color=None) -> ["BaseCard"]:
        return [
            card for card in self.get_all_villagers()
            if (unit is None or (unit is not None and unit == card.unit))
            and (color is None or (color is not None and color == card.color))
        ]

    def get_colors_in_hand(self) -> [str]:
        colors = [card.color for card in self.hand]
        return list(set(colors))

    def get_animals_in_hand(self) -> ["BaseCard"]:
        return [card for card in self.hand if card.type == TYPE.ANIMAL]

    def get_buildings_in_hand(self) -> ["BaseCard"]:
        return [card for card in self.hand if card.type == TYPE.BUILDING]

    def get_villager_in_village(self, color, unit) -> ["BaseCard"]:
        return [card for card in self.villages[color] if card.unit == unit]

    def village_supports_animals(self, color) -> ["BaseCard"]:
        return [card for card in self.villages[color] if card.unit in ['farmer']]

    def village_supports_buildings(self, color) -> ["BaseCard"]:
        return [card for card in self.villages[color] if card.unit in ['builder']]

    def get_cards_in_hand(self, filter, value):
        return [card for card in self.hand if getattr(card, filter) == value]

    def get_incrementable_villages(self) -> dict:
        built_villages = self.get_built_villages()

        available_villages = {}
        for village in built_villages:
            available_villages[village] = self.get_cards_in_hand('color', village)
            if self.village_supports_animals(village):
                available_villages[village] += self.get_cards_in_hand('type', TYPE.ANIMAL)

            if self.village_supports_buildings(village):
                available_villages[village] += self.get_cards_in_hand('type', TYPE.BUILDING)

        return available_villages

    def get_cards_to_add_to_villages(self) -> ["BaseCard"]:
        return [card for card in self.hand if card.color in self.get_built_villages()]

    def get_card_to_battle(self, village=None) -> ("BaseCard", Deck):
        options = self.hand + self.get_villagers(color=village)
        options = [card for card in options if card.type == TYPE.UNIT]
        side_battle = 'attack' if village is None else 'defend'
        return self.choose_card_to_battle(options, side_battle)

    # END GETTERS

    # CHOOSERS
    def choose_village_to_build(self) -> str|None:
        available_to_build = self.get_villages_to_build()
        if len(available_to_build) == 0:
            return None

        return choose_option(available_to_build, f'Choose a village to build: ')

    def choose_action(self, actions) -> str:
        return choose_option(actions, 'Choose an act: ', optional=False)

    def choose_card_from_hand(self, reason, optional=False) -> "BaseCard":
        text = f'Choose a card to {reason}: '
        return choose_option(self.hand, text, optional=optional)

    def choose_player_to_attack(self) -> Self:
        players = self.get_attackable_players()
        return choose_option(players, 'Choose player to attack: ', optional=False)

    def choose_player_to_trade(self) -> Self:
        return choose_option(self.get_other_players(), 'Choose player to trade: ', optional=False)

    def choose_card_to_discard(self) -> "BaseCard":
        return self.choose_card_from_hand('discard')

    def choose_card_to_trade(self) -> "BaseCard":
        return self.choose_card_from_hand('trade')

    def choose_card_to_battle(self, options, side_battle) -> ("BaseCard", Deck):
        card = choose_option(options, f'Choose a villager to {side_battle}: ', optional=False)
        origin = self.hand if card in self.hand else self.get_villagers_village(card)
        origin_type = 'hand' if card in self.hand else card.color
        return card, origin, origin_type

    def choose_battle_reward(self, rewards):
        return choose_option(rewards, 'Choose battle reward: ', page_count=3, optional=False)

    def choose_village_to_attack(self, attacked_player):
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
        if self.name == 'Caio' and qtd == 8:
            animal = [card for card in self.table.deck if card.type == TYPE.ANIMAL][0:1]
            building = [card for card in self.table.deck if card.type == TYPE.BUILDING][0:1]
            self.table.deck.remove_cards(animal)
            self.table.deck.remove_cards(building)
            farmer_builder = [card for card in self.table.deck if card.color == COLOR.RED and (card.unit == 'farmer' or card.unit == 'builder')][0:2]
            self.table.deck.remove_cards(farmer_builder)
            red_cards = [card for card in self.table.deck if card.color == COLOR.RED][0:4]
            stacked_hand = animal + building + farmer_builder + red_cards
            self.table.deck.remove_cards(red_cards)
            self.hand.add_cards(stacked_hand)
        else:
            self.hand.add_cards(self.table.deck.draw_cards(qtd))

    def show_hand(self):
        self.hand.show_deck()

    def count_score(self):
        positive = count_gold(self.get_all_villagers())
        negative = count_gold(self.hand + self.cemetery) * -1
        self.score += positive - negative

    def build_village(self, color):
        available_cards = [card for card in self.hand if card.color == color]
        chosen_cards = self.choose_cards_to_build(available_cards)
        self.hand.remove_cards(chosen_cards)
        self.villages[color].add_cards(chosen_cards)

    def add_card_to_village(self, village: str, card: "BaseCard"):
        self.villages[village].add_card(card)
        self.hand.remove_card(card)

    def add_cards_to_village(self, village: str, cards: ["BaseCard"]):
        for card in cards:
            self.add_card_to_village(village, card)

    def discard_card(self, card):
        self.hand.remove_card(card)
        self.table.discard.add_card(card)

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
        (attacking_card, att_card_origin, att_card_origin_type) = self.get_card_to_battle()
        attacked_player = self.choose_player_to_attack()
        attacked_village = self.choose_village_to_attack(attacked_player)
        (defender_card, def_card_origin, def_card_origin_type) = attacked_player.get_card_to_battle(attacked_village)
        battle_result = attack_card(attacking_card, defender_card)
        print(f'{attacking_card} vs {defender_card}!')
        if battle_result:
            print('Battle Won!')
            reward = self.choose_battle_reward(['destroy defender', 'kidnap defender', 'kidnap villager'])
            if reward == 'destroy defender':
                self.destroy_card(def_card_origin, defender_card)
            elif reward == 'kidnap defender':
                def_card_origin.remove_card(defender_card)
                if reward == 'kidnap defender':
                    self.hand.add_card(defender_card)
            else:
                kidnapped_villager = self.choose_villager_from_village(attacked_village, attacked_player)
                kidnapped_village = attacked_player.get_villagers_village(kidnapped_villager)
                kidnapped_village.remove_card(kidnapped_villager)
                self.hand.add_card(kidnapped_villager)
                if kidnapped_villager != defender_card and def_card_origin_type == 'hand':
                    print(f'Defending hired unit {defender_card} discarded!')
                    attacked_player.destroy_card(def_card_origin, defender_card)
            if att_card_origin_type == 'hand':
                print(f'Attacking hired unit {attacking_card} discarded!')
                self.destroy_card(att_card_origin, attacking_card)
        else:
            print('Battle Lost!')
            self.destroy_card(att_card_origin, attacking_card)

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
