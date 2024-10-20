from .basecard import BaseCard
from constants import TYPE


class Tavern(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='tavern',
            unit_type=TYPE.BUILDING,
            color=color,
            power=0,
            gold=3,
        )