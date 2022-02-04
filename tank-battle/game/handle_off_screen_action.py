from game import constants
from game.action import Action

class HandleOffScreenAction(Action):
    """
    Bounces the ball off the walls
    """
    def __init__(self, audio_service):
        """The class constructor."""
        self._audio_service = audio_service

    def execute(self, cast):

        #get ball data
        balls = cast["balls"]
        tank1 = cast["tank"][0]
        tank2 = cast["tank"][1]
        barrel1 = cast["barrel"][0]
        barrel2 = cast["barrel"][1]
        for ball in balls:
            x = ball._position.get_x()
            y = ball._position.get_y()

            #hit horizontal
            if( x <= 0 - constants.BALL_WIDTH or x >= constants.MAX_X):
                balls.remove(ball)
            
            # hit ground
            elif y > constants.MAX_Y + constants.BALL_WIDTH:
                balls.remove(ball)
                self._audio_service.play_sound(constants.SOUND_THUD)

        #get tank data
        tank_x1 = tank1._position.get_x()

        tank_x2 = tank2._position.get_x()

        # tank won't go off screen
        if(tank_x2 < 0):
            tank2._position._x = 0
            barrel2._position._x += 1 * constants.TANK_SPEED
            constants.BALL_CHANGE_X2 -= tank2._velocity._x
        if(tank_x1 > constants.MAX_X - constants.TANK_WIDTH):
            tank1._position._x = constants.MAX_X - constants.TANK_WIDTH
            barrel1._position._x += -1 * constants.TANK_SPEED
            constants.BALL_CHANGE_X1 -= tank1._velocity._x

        # tank stays on its own side
        if(tank_x2 > ((constants.MAX_X / 2) - constants.FULL_TANK_WIDTH - constants.WALL_WIDTH)):
            tank2._position._x += -1 * constants.TANK_SPEED
            barrel2._position._x += -1 * constants.TANK_SPEED
            constants.BALL_CHANGE_X2 -= tank2._velocity._x
        if(tank_x1 < ((constants.MAX_X / 2) + constants.BARREL_WIDTH + constants.WALL_WIDTH)):
            tank1._position._x += 1 * constants.TANK_SPEED
            barrel1._position._x += 1 * constants.TANK_SPEED
            constants.BALL_CHANGE_X1 -= tank1._velocity._x
