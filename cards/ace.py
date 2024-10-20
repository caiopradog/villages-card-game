from .basecard import BaseCard
from constants import TYPE


class Ace(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='ace',
            unit_type=TYPE.UNIT,
            color=color,
            power=2,
            gold=1,
        )