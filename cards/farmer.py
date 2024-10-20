from .basecard import BaseCard
from constants import TYPE


class Farmer(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='farmer',
            unit_type=TYPE.UNIT,
            color=color,
            power=1,
            gold=3,
            enable_animal=True
        )