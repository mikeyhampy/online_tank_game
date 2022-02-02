from game import constants
from game.action import Action
from game.point import Point
from math import cos
from math import sin
from math import radians

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        choice = True
        right_barrel = None
        left_barrel = None
        for key, group in cast.items():
            if key == "tank" or key == "barrel":
                choice = False
            else:
                choice = True
            for actor in group:
                if not actor.get_velocity().is_zero():
                    if key == "barrel":
                        right_barrel = group[0]
                        left_barrel = group[1]
                    self._move_actor(actor, choice, right_barrel, left_barrel)

    def _move_actor(self, actor, choice, right_barrel, left_barrel):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()


        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()
        
        #checks if we are not in the tank director 
        #if not then run if, then else
        if choice:
            change_size = .05
            change_scale = .005
            if actor._scale >= (1):
                actor._scale = 1
                actor._width = (2 * constants.BALL_WIDTH)
                actor._height = (2 * constants.BALL_HEIGHT)
                change_size = 0
            else:
                actor._width += change_size
                actor._height += change_size
                actor._scale += change_scale
            actor._velocity._y = dy + .1
            x = (x + dx) + (change_size / 2)
            y = (y + dy) + (change_size / 2)
        else:  
            if right_barrel == actor:

                actor._angle += dy
                constants.TANK_ANGLE += dy
                if actor._angle <= 180:
                    y = constants.BARREL_Y1
                    actor._angle = 180
                    constants.TANK_ANGLE = 180
                    dy = 0

                if actor._angle >= 270:
                    y = constants.MAX_Y - constants.TANK_HEIGHT
                    actor._angle = 270
                    constants.TANK_ANGLE = 270
                    dy = 0
                    
                adder = constants.TANK_ANGLE_CHANGE * dy * sin(radians(constants.TANK_ANGLE))
                y += adder
                constants.BALL_CHANGE_X1 += dx

            elif left_barrel == actor:
                actor._angle += dy
                constants.TANK_ANGLE2 += dy
                if actor._angle <= 270:
                    actor._angle = 270
                    constants.TANK_ANGLE2 = 270
                    dy = 0

                if actor._angle >= 360:
                    actor._angle = 360
                    constants.TANK_ANGLE2 = 360
                    dy = 0
                    
                adder2 = constants.TANK_ANGLE_CHANGE * (dy) * cos(radians(constants.TANK_ANGLE2))
                x += adder2
                constants.BALL_CHANGE_X2 += dx

            # all tank actors (tank and barrels)
            x = (x + dx)
        
        position = Point(x, y)
        actor.set_position(position)