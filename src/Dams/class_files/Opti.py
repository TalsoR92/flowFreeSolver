from enum import Enum

class CheckReachable(Enum):
    NONE = 0
    END_PATH = 1
    NEAR_2_POINTS = 2
    NEAR_3_THINGS = 3
    EVERY_CASE = 4

class Opti:
    # met les type a coté des variables
    def __init__(self, check_reachable: CheckReachable=CheckReachable.NONE):
        # Vérifie si check_reachable est une valeur valide de l'énumération CheckReachable
        if not isinstance(check_reachable, CheckReachable):
            raise ValueError("check_reachable doit être une valeur de l'énumération CheckReachable")
        self.check_reachable = check_reachable
