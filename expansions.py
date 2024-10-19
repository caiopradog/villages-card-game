from constants import COLOR, EXPANSION
import cards
from cards import BaseCard


expansion_cards = {
    EXPANSION.BASE: [{
        "class": 'Ace',
        "colors": [COLOR.YELLOW, COLOR.PURPLE, COLOR.GREEN, COLOR.BLUE],
        "count": 1,
    }, {
        "class": 'Archer',
        "colors": [COLOR.ORANGE, COLOR.GREEN],
        "count": 1,
    }, {
        "class": 'Assassin',
        "colors": [COLOR.PURPLE, COLOR.RED],
        "count": 1,
    }, {
        "class": 'Builder',
        "colors": [COLOR.PURPLE, COLOR.BLUE, COLOR.ORANGE, COLOR.RED, COLOR.YELLOW, COLOR.GREEN],
        "count": 1,
    }, {
        "class": 'Dragon',
        "colors": [COLOR.RED, COLOR.ORANGE],
        "count": 1,
    }, {
        "class": 'Farmer',
        "colors": [COLOR.RED, COLOR.YELLOW, COLOR.GREEN, COLOR.PURPLE, COLOR.BLUE, COLOR.ORANGE],
        "count": 1,
    }, {
        "class": 'Goblin',
        "colors": [COLOR.BLUE, COLOR.YELLOW, COLOR.RED],
        "count": 1,
    }, {
        "class": 'Golem',
        "colors": [COLOR.GREEN, COLOR.YELLOW],
        "count": 1,
    }, {
        "class": 'Hero',
        "colors": [COLOR.BLUE, COLOR.GREEN],
        "count": 1,
    }, {
        "class": 'Joker',
        "colors": [COLOR.GREEN, COLOR.PURPLE],
        "count": 1,
    }, {
        "class": 'King',
        "colors": [COLOR.GREEN, COLOR.YELLOW],
        "count": 1,
    }, {
        "class": 'Knight',
        "colors": [COLOR.YELLOW, COLOR.GREEN, COLOR.BLUE, COLOR.PURPLE],
        "count": 1,
    }, {
        "class": 'Merchant',
        "colors": [COLOR.ORANGE, COLOR.YELLOW],
        "count": 1,
    }, {
        "class": 'Orc',
        "colors": [COLOR.RED, COLOR.ORANGE],
        "count": 1,
    }, {
        "class": 'Priest',
        "colors": [COLOR.ORANGE, COLOR.RED],
        "count": 1,
    }, {
        "class": 'Princess',
        "colors": [COLOR.GREEN, COLOR.BLUE, COLOR.YELLOW, COLOR.PURPLE],
        "count": 1,
    }, {
        "class": 'Scout',
        "colors": [COLOR.RED, COLOR.PURPLE, COLOR.ORANGE],
        "count": 1,
    }, {
        "class": 'Thief',
        "colors": [COLOR.YELLOW, COLOR.BLUE, COLOR.PURPLE],
        "count": 1,
    }, {
        "class": 'Warrior',
        "colors": [COLOR.ORANGE, COLOR.BLUE, COLOR.RED],
        "count": 1,
    }, {
        "class": 'Wizard',
        "colors": [COLOR.RED, COLOR.PURPLE, COLOR.ORANGE, COLOR.BLUE],
        "count": 1,
    }, {
        "class": 'Bunny',
        "colors": [COLOR.GRAY],
        "count": 2,
    }, {
        "class": 'Chicken',
        "colors": [COLOR.GRAY],
        "count": 2,
    }, {
        "class": 'Pig',
        "colors": [COLOR.GRAY],
        "count": 2,
    }, {
        "class": 'Sheep',
        "colors": [COLOR.GRAY],
        "count": 1,
    }, {
        "class": 'Castle',
        "colors": [COLOR.GRAY],
        "count": 1,
    }, {
        "class": 'Inn',
        "colors": [COLOR.GRAY],
        "count": 2,
    }, {
        "class": 'Tavern',
        "colors": [COLOR.GRAY],
        "count": 1,
    }, {
        "class": 'Tower',
        "colors": [COLOR.GRAY],
        "count": 1,
    }]
}


def get_cards(expansions: list) -> ["BaseCard"]:
    available_cards = []

    for expansion in expansions:
        templates = expansion_cards[expansion]
        for template in templates:
            for color in template['colors']:
                card_class = getattr(cards, template['class'])
                card = card_class(color)
                available_cards += [card]*template['count']

    return available_cards
