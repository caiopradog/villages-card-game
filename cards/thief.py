from .basecard import BaseCard
from constants import TYPE


class Thief(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='thief',
            unit_type=TYPE.UNIT,
            color=color,
            power=1,
            gold=1,
        )