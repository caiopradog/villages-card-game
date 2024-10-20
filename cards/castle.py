from .basecard import BaseCard
from constants import TYPE


class Castle(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='castle',
            unit_type=TYPE.BUILDING,
            color=color,
            power=0,
            gold=4,
        )