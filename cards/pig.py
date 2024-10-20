from .basecard import BaseCard
from constants import TYPE


class Pig(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='pig',
            unit_type=TYPE.ANIMAL,
            color=color,
            power=0,
            gold=1,
        )