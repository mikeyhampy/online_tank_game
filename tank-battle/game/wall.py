from game.actor import Actor
from game.point import Point
from game import constants
import random

class Wall():
    def __init__(self):
        self._walls = []

    def set_walls(self):
        """
        Method will set all the wall actors and will save them in a list
        """

        wall_x = (constants.MAX_X - constants.WALL_WIDTH) / 2
        wall_y = constants.MAX_Y - constants.WALL_HEIGHT
        wall_y2 = constants.MAX_Y - 150
        wall_y = random.randint(wall_y, wall_y2)
        wall = Actor()
        position = Point(wall_x, wall_y)
        wall.set_position(position)
        wall.set_width(constants.WALL_WIDTH)
        wall.set_height(constants.WALL_HEIGHT)
        wall.set_image("wall", "red")
        self._walls.append(wall)

    def get_walls(self):
        """
        Method will get all the wall actors and return them as a string
        """

        return self._walls