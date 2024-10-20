from .basecard import BaseCard
from constants import TYPE


class Scout(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='scout',
            unit_type=TYPE.UNIT,
            color=color,
            power=1,
            gold=1,
        )