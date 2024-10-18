class EXPANSION(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    BASE = 'blank'
    BONE = 'bone'
    CARDSMITH = 'cp'
    CRYSTAL_QUEST = 'cq'
    DISTANT_LANDS = 'dl'
    GHOST_TOWN = 'gt'
    HOLIDAY_PACK = 'hp'
    ROYALTY_PACK = 'rp'
    SALT = 'salt'
    SUPER = 'sv'


class TYPE(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    ANIMAL = 'animal'
    UNIT = 'unit'
    MONSTER = 'monster'
    TREASURE = 'treasure'
    BUILDING = 'building'
    SCORE = 'score'


class COLOR(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    PURPLE = 'purple'
    ORANGE = 'orange'
    LIGHT = 'light'
    DARK = 'dark'
    GRAY = 'gray'