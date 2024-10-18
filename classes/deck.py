from expansions import expansion_cards
from .card import Card
from constants import TYPE, COLOR
import random
import uuid
import math


class Deck:
    def __init__(self, expansions=None):
        if expansions is None:
            expansions = []
        self.cards = []
        self.expansions = expansions

    def __repr__(self):
        return ' | '.join(map(str, self.cards))

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def __setitem__(self, key, value):
        self.cards[key] = value
        return self

    def __set__(self, instance, value):
        self.cards = value
        return self

    def __len__(self):
        return len(self.cards)

    def __list__(self):
        return self.cards

    def __add__(self, other):
        if type(other) is list:
            return self.cards + other
        else:
            newList = self.cards
            newList.append(other)
            return newList

    def __sub__(self, other):
        if type(other) is list:
            self.remove_cards(other)
        else:
            self.remove_card(other)
        return self

    def pop(self, idx=0):
        popped = self.cards.pop(idx)
        return popped

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def remove_cards(self, cards):
        for card in cards:
            self.remove_card(card)

    def show_deck(self):
        page_count = 3
        for i in range(math.ceil(len(self.cards) / page_count)):
            idx = i * page_count
            cards = [str(card) for card in self.cards[idx:idx+page_count]]
            print(' | '.join(cards))

    def draw_cards(self, qtd):
        drawn_cards = self.cards[0:qtd]
        self.cards = self.cards[qtd:]
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.cards = []

    def fill_deck(self):
        card_limits = {
            COLOR.RED: 10,
            COLOR.BLUE: 10,
            COLOR.DARK: 10,
            COLOR.GREEN: 10,
            COLOR.YELLOW: 10,
            COLOR.PURPLE: 10,
            COLOR.ORANGE: 10,
            COLOR.LIGHT: 3,
            TYPE.ANIMAL: 7,
            TYPE.BUILDING: 5,
        }
        available_cards = []
        for expansion in self.expansions:
            available_cards = available_cards + expansion_cards[expansion]
        card_pool = {
            COLOR.RED: [],
            COLOR.BLUE: [],
            COLOR.GREEN: [],
            COLOR.YELLOW: [],
            COLOR.PURPLE: [],
            COLOR.ORANGE: [],
            COLOR.DARK: [],
            COLOR.LIGHT: [],
            TYPE.ANIMAL: [],
            TYPE.BUILDING: [],
        }
        for card_template in available_cards:
            for color in card_template['colors']:
                key = color if card_template['type'] in [TYPE.UNIT, TYPE.MONSTER] else card_template['type']
                card = Card(
                    uuid=uuid.uuid4(),
                    unit=card_template['unit'],
                    unit_type=card_template['type'],
                    color=color,
                    power=card_template['power'],
                    gold=card_template['gold']
                )
                card_pool[key] += [card]*card_template['count']

        final_card_list = []
        for card_type in card_pool:
            card_list = card_pool[card_type]
            random.shuffle(card_list)
            if not len(card_list):
                continue
            card_count = card_limits[card_type]
            filtered_cards = card_list[0:card_count]
            if card_type not in [COLOR.DARK, COLOR.LIGHT, TYPE.ANIMAL, TYPE.BUILDING]:
                card_list = card_list[card_count:]
                building_enabling_cards = [card for card in filtered_cards if card.enable_building]
                animal_enabling_cards = [card for card in filtered_cards if card.enable_animal]
                unneeded_cards = [card for card in filtered_cards if card not in building_enabling_cards and card not in animal_enabling_cards]
                random.shuffle(unneeded_cards)

                if not len(building_enabling_cards):
                    building_enabling_in_pool = [card for card in card_list if card.can_support_building()]
                    selected_card = building_enabling_in_pool.pop()
                    filtered_cards.append(selected_card)
                    card_list.remove(selected_card)

                if not len(animal_enabling_cards):
                    animal_enabling_in_pool = [card for card in card_list if card.can_support_animal()]
                    selected_card = animal_enabling_in_pool.pop()
                    filtered_cards.append(selected_card)
                    card_list.remove(selected_card)
            final_card_list += filtered_cards

        self.cards = final_card_list
