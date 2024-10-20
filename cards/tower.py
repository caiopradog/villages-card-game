from .basecard import BaseCard
from constants import TYPE


class Tower(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='tower',
            unit_type=TYPE.BUILDING,
            color=color,
            power=0,
            gold=3,
        )