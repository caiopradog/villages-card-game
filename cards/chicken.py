from .basecard import BaseCard
from constants import TYPE


class Chicken(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='chicken',
            unit_type=TYPE.ANIMAL,
            color=color,
            power=0,
            gold=1,
        )