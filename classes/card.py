class Card:
    def __init__(self, uuid, unit, unit_type, color, power, gold):
        color2 = None
        if type(color) is not str:
            color, color2 = color
        self.uuid = uuid
        self.unit = unit
        self.type = unit_type
        self.color = color
        self.color2 = color2
        self.power = power
        self.gold = gold
        self.enable_animal = self.unit in ['farmer']
        self.enable_building = self.unit in ['builder']

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

    def can_support_building(self):
        return self.unit in ['builder']

    def can_support_animal(self):
        return self.unit in ['farmer']
