from src.specialObjects.ship import Ship

class Fleet(Ship):
    def __init__(self, fleet_name, ship_number, flag_ship, fleet_modifiers, fleet_morale, is_player):
        super().__init__("Default Ship Name", 1)  # Call the constructor of the Ship class with default values
        self.fleet_name = fleet_name
        self.ship_number = ship_number
        self.flag_ship = flag_ship
        self.fleet_modifiers = fleet_modifiers
        self.fleet_morale = fleet_morale
        self.is_player = is_player
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def list_ships(self):
        return [ship.info() for ship in self.ships]