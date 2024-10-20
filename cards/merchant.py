from .basecard import BaseCard
from constants import TYPE


class Merchant(BaseCard):
    def __init__(self, color):
        super().__init__(
            unit='merchant',
            unit_type=TYPE.UNIT,
            color=color,
            power=0,
            gold=3,
        )