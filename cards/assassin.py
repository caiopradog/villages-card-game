from .basecard import BaseCard
from constants import TYPE


class Assassin(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='assassin',
            unit_type=TYPE.UNIT,
            color=color,
            power=1,
            gold=3,
        )