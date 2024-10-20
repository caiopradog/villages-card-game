from .basecard import BaseCard
from constants import TYPE


class Inn(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='inn',
            unit_type=TYPE.BUILDING,
            color=color,
            power=0,
            gold=3,
        )