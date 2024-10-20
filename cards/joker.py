from .basecard import BaseCard
from constants import TYPE


class Joker(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='joker',
            unit_type=TYPE.UNIT,
            color=color,
            power=2,
            gold=1,
        )