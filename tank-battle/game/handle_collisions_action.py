from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service
        self.num_tank_col = 0
        self.num_wall_col = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if len(cast) == 2:
        #beginning of the game
            selector_p1 = cast["selector"][0]
            selector_p2 = cast["selector"][1]
            tank_colors = cast["colors"]
            if selector_p1._color_selected and selector_p2._color_selected:
                for tank_color in tank_colors:
                    if self._physics_service.is_collision(tank_color, selector_p1):
                        selector_p1._color_tank = tank_color._color_actor
                        constants.PLAYER_TANK_COLOR1 = tank_color._color_actor

                    if self._physics_service.is_collision(tank_color, selector_p2):
                        selector_p2._color_tank = tank_color._color_actor
                        constants.PLAYER_TANK_COLOR2 = tank_color._color_actor
        else:
                
            # set variables to check collisions in game
            balls = cast["balls"]
        
            tank_right = cast["tank"][0]
            tank_left = cast["tank"][1]
            wall = cast["walls"][0]
            lives1 = cast["lives1"]
            lives2 = cast["lives2"]

            for ball in balls:
                if self._physics_service.is_collision(ball, wall):
                    self._audio_service.play_sound(constants.SOUND_THUD)
                    balls.remove(ball)

                    # check ball and tank right collisions
            for ball in balls:
                if self._physics_service.is_collision(ball, tank_right):
                    self._audio_service.play_sound(constants.SOUND_EXPLOSION)
                    balls.remove(ball)
                    length1 = len(lives1)
                    i1 = 0
                    for live1 in lives1:
                        if i1 == (length1 - 1):
                            lives1.remove(live1)
                        i1 += 1


            # check ball and tank left collisions
            for ball in balls:
                if self._physics_service.is_collision(ball, tank_left):
                    self._audio_service.play_sound(constants.SOUND_EXPLOSION)
                    balls.remove(ball)
                    length2 = len(lives2)
                    i2 = 0
                    for live2 in lives2:
                        if i2 == (length2 - 1):
                            lives2.remove(live2)
                        i2 += 1