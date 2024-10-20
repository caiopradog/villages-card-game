from .basecard import BaseCard
from constants import TYPE


class Sheep(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='sheep',
            unit_type=TYPE.ANIMAL,
            color=color,
            power=0,
            gold=1,
        )