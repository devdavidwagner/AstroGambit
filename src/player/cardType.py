from enum import Enum

class CardType(Enum):
    SHIP = "SHIP"
    ATTACK = "ATTACK"
    SHIELD = "SHIELD REGEN"
    REPAIR = "REPAIR"

# Example usage:
card_type = CardType.SHIP
print(card_type)  # Output: CardType.SHIP
