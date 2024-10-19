import uuid


class BaseCard:
    def __init__(self, unit, unit_type, color, power, gold, enable_animal=False, enable_building=False):
        color2 = None
        if type(color) is not str:
            color, color2 = color
        self.uuid = uuid.uuid4()
        self.unit = unit
        self.type = unit_type
        self.color = color
        self.color2 = color2
        self.power = power
        self.gold = gold
        self.enable_animal = enable_animal
        self.enable_building = enable_building

    def __str__(self):
        return f'{self.color_str()} {self.unit} P:{self.power} G:{self.gold}'

    def __repr__(self):
        return self.__str__()

    def title(self):
        return self.__str__().title()

    def color_str(self):
        color = self.color
        if self.color2:
            color = f'{color}/{self.color2}'
        return color

    def activate_ability(self):
        print('Base Class Card!')
