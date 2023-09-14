from src.specialObjects.ship import Ship
from src.specialObjects.zones.fleetZone import FleetZone

class Fleet():
    FLEET_ZONE_COODS = (600, 150)
    IMG_ZONE = "assets/fleetZone.png"
    def __init__(self, fleet_name, ship_number, flag_ship, fleet_modifiers, fleet_morale, is_player):
        self.fleet_name = fleet_name
        self.ship_number = ship_number
        self.flagShip = flag_ship
        self.fleet_modifiers = fleet_modifiers
        self.fleet_morale = fleet_morale
        self.is_player = is_player
        self.ships = []
        self.fleetZone = FleetZone(self.FLEET_ZONE_COODS,self.IMG_ZONE)

    def add_ship(self, ship):
        self.ships.append(ship)
        self.ship_number +=1

    def list_ships(self):
        return [ship.info() for ship in self.ships]
    
    def order(self, orderType):
        if orderType == "ATTACK":
            for ship in self.ships:
                ship.start_laser_animation()
            self.flagShip.start_laser_animation()
    
    def update(self):        
        self.flagShip.update()
        for ship in self.ships:
            ship.update()
    
    
    def draw(self, screen):
        self.fleetZone.draw(screen)
        self.flagShip.draw(screen)
        for ship in self.ships:
            ship.draw(screen)