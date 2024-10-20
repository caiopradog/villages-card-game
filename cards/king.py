from .basecard import BaseCard
from constants import TYPE


class King(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='king',
            unit_type=TYPE.UNIT,
            color=color,
            power=0,
            gold=0,
        )