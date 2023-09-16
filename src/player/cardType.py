from enum import Enum, auto


class CardType(Enum):
    SHIP = auto()
    ATTACK_LASER = auto()
    ATTACK_BOMB = auto()
    SHIELD = auto()
    REPAIR = auto()
    SHIELD_BOOST = auto()

    # Define AttackType as part of CardType
    class AttackType(Enum):
        LASER = auto()
        BOMB = auto()

