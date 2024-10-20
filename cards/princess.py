from .basecard import BaseCard
from constants import TYPE


class Princess(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='princess',
            unit_type=TYPE.UNIT,
            color=color,
            power=0,
            gold=5
        )
