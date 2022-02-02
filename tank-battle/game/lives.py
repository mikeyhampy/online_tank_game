from game.actor import Actor
from game.point import Point
from game import constants

class Lives():
    def __init__(self):
        self._lives1 = []
        self._lives2 = []

    def set_lives(self):
        #right tank
        i = 0
        difference = 41
        x1 = constants.MAX_X - 20 - 36
        x2 = 20
        while(i < 3):
            lives1 = Actor()
            lives1._scale = .25
            position1 = Point(x1, 20)
            lives1.set_position(position1)
            lives1.set_image("full1", constants.PLAYER_TANK_COLOR1)
            self._lives1.append(lives1)

            #left tank
            lives2 = Actor()
            lives2._scale = .25
            position2 = Point(x2, 20)
            lives2.set_position(position2)
            lives2.set_image("full2", constants.PLAYER_TANK_COLOR2)
            self._lives2.append(lives2)
            x1 -= difference
            x2 += difference
            i += 1

    def get_lives1(self):
        return self._lives1

    def get_lives2(self):
        return self._lives2