"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    health = 3
    total_aliens_created  = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate 
        self.health = Alien.health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y 

    def collision_detection(self, other):
        pass

#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates

def new_aliens_collection(start_positions):

    aliens = []
    
    for coordinate in start_positions:
        x_coor, y_coor = coordinate
        new_alien = Alien(x_coor, y_coor)
        aliens.append(new_alien)

    return aliens
    