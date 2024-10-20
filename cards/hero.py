from .basecard import BaseCard
from constants import TYPE


class Hero(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='hero',
            unit_type=TYPE.UNIT,
            color=color,
            power=3,
            gold=2,
        )