from game.actor import Actor
from game.point import Point
from game import constants
from math import cos
from math import sin
from math import radians

class Ball():
    def __init__(self):
        self._balls = []
        self.angle1 = (-180)
        self.angle2 = (-180)

    def set_ball1(self):
        ball = Actor()
        ball._scale = .5
        ball._angle = self.angle1
        x_cos = cos(radians(ball._angle))
        y_sin = sin(radians(ball._angle))
        x = constants.BALL1_POS - (constants.BARREL_WIDTH * x_cos) + ((constants.BALL_WIDTH * .75) * y_sin)
        x += constants.BALL_CHANGE_X1
        y = constants.BALL_Y1 - constants.BARREL_WIDTH * y_sin
        dx = constants.BALL_DX * x_cos
        dy = constants.BALL_DY * y_sin
        position = Point(x, y)
        velocity = Point(dx, dy)
        ball.set_position(position)
        ball.set_velocity(velocity)
        ball.set_width(constants.BALL_WIDTH)
        ball.set_height(constants.BALL_HEIGHT)
        ball.set_image("ball", constants.PLAYER_TANK_COLOR1)
        self._balls.append(ball)

    def set_ball2(self):
        ball2 = Actor()
        ball2._scale = .5
        ball2._angle = self.angle2
        x_cos = cos(radians(ball2._angle))
        y_sin = sin(radians(ball2._angle))
        x = constants.BALL2_POS - constants.BARREL_WIDTH * x_cos #+ ((constants.BALL_WIDTH * .75) * y_sin)
        x += constants.BALL_CHANGE_X2
        y = constants.BALL_Y - (constants.BARREL_WIDTH - (constants.BALL_WIDTH/6)) * y_sin# + ((constants.BALL_WIDTH * (.75/2)) * x_cos)
        dx = (constants.BALL_DX) * x_cos
        dy = constants.BALL_DY * y_sin
        position = Point(x, y)
        velocity = Point(dx, dy)
        ball2.set_position(position)
        ball2.set_velocity(velocity)
        ball2.set_width(constants.BALL_WIDTH)
        ball2.set_height(constants.BALL_HEIGHT)
        ball2.set_image("ball", constants.PLAYER_TANK_COLOR2)
        self._balls.append(ball2)

    def get_ball(self):
        return self._balls