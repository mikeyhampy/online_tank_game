from game.actor import Actor
from game.point import Point
from game import constants

class Tank():
    def __init__(self):
        self._tanks = []

    def set_tank(self):
        #right tank
        tank1 = Actor()
        tank_x1 = constants.TANK_X1
        position = Point(tank_x1, constants.TANK_Y)
        tank1.set_position(position)
        tank1.set_width(constants.TANK_WIDTH)
        tank1.set_height(constants.TANK_HEIGHT)
        tank1.set_image("tank1", constants.PLAYER_TANK_COLOR1)
        self._tanks.append(tank1)

        #left tank
        tank2 = Actor()
        tank_x2 = constants.TANK_X2
        position = Point(tank_x2, constants.TANK_Y)
        tank2.set_position(position)
        tank2.set_width(constants.TANK_WIDTH)
        tank2.set_height(constants.TANK_HEIGHT)
        tank2.set_image("tank2", constants.PLAYER_TANK_COLOR2)
        self._tanks.append(tank2)

    def get_tank(self):
        return self._tanks