from .basecard import BaseCard
from constants import TYPE


class Priest(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='priest',
            unit_type=TYPE.UNIT,
            color=color,
            power=0,
            gold=0,
        )