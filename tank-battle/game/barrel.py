from game.actor import Actor
from game.point import Point
from game import constants

class Barrel():
    def __init__(self):
        self._barrels = []

    def set_barrel(self):
        #right barrel p1
        barrel1 = Actor()
        barrel1._angle = constants.TANK_ANGLE
        position = Point(constants.BARREL_X1, constants.BARREL_Y1)
        barrel1.set_position(position)
        barrel1.set_width(constants.TANK_WIDTH)
        barrel1.set_height(constants.TANK_HEIGHT)
        barrel1.set_image("barrel", constants.PLAYER_TANK_COLOR1)
        self._barrels.append(barrel1)

        #left barrel p2
        barrel2 = Actor()
        barrel2._angle = constants.TANK_ANGLE2
        position = Point(constants.BARREL_X2, constants.BARREL_Y2)
        barrel2.set_position(position)
        barrel2.set_width(constants.TANK_WIDTH)
        barrel2.set_height(constants.TANK_HEIGHT)
        barrel2.set_image("barrel", constants.PLAYER_TANK_COLOR2)
        self._barrels.append(barrel2)

    def get_barrel(self):
        return self._barrels