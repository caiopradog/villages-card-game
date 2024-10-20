from .basecard import BaseCard
from constants import TYPE


class Wizard(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='wizard',
            unit_type=TYPE.UNIT,
            color=color,
            power=4,
            gold=2,
        )