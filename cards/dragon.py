from .basecard import BaseCard
from constants import TYPE


class Dragon(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='dragon',
            unit_type=TYPE.UNIT,
            color=color,
            power=5,
            gold=2
        )
