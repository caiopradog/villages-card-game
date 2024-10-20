from .basecard import BaseCard
from constants import TYPE


class Golem(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='golem',
            unit_type=TYPE.UNIT,
            color=color,
            power=2,
            gold=2,
        )