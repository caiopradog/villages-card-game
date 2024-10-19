from .basecard import BaseCard
from constants import TYPE


class Princess(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='princess',
            unit_type=TYPE.UNIT,
            color=color,
            power=2,
            gold=5
        )
