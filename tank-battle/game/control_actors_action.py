from game import constants
from game.action import Action
from game.ball import Ball

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service, audio_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._audio_service = audio_service
        self._enter = False
        self.fire_timer = 0
        self.fire_timer2 = 0
        self._choice = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        if len(cast) == 2:
            #beginning of the game
            selector_p1 = cast["selector"][0]
            selector_p2 = cast["selector"][1]
            select_direction1, enter_color1 = self._input_service.choose_color1()
            select_direction2, enter_color2 = self._input_service.choose_color2()
            selector_p1.set_velocity(select_direction1)
            selector_p2.set_velocity(select_direction2)
            selector_p1._color_selected = enter_color1
            selector_p2._color_selected = enter_color2

        else:
            # Barrel 1 and tank 1
            fire = False
            direction1, fire = self._input_service.get_direction()
            barrel1 = cast["barrel"][0]
            tank1 = cast["tank"][0]
            tank1.set_velocity(direction1.scale(constants.TANK_SPEED))
            barrel1.set_velocity(direction1.scale(constants.TANK_SPEED))

            #fire ball 1 
            self.fire_timer += 1
            if self.fire_timer == 20:
                self._audio_service.play_sound(constants.SOUND_RELOAD)
                #self._audio_service.stop_audio(constants.SOUND_RELOAD)
                
            if fire and self.fire_timer > 35:
                ball = Ball()
                ball.angle1 += constants.TANK_ANGLE
                ball.set_ball1()
                cast["balls"].append(ball._balls[0])
                self.fire_timer = 0
                self._audio_service.play_sound(constants.SOUND_FIRE)
            # Barrel 2 and tank 2
            fire2 = False
            direction2, fire2 = self._input_service.get_direction2()
            barrel2 = cast["barrel"][1]
            tank2 = cast["tank"][1]
            tank2.set_velocity(direction2.scale(constants.TANK_SPEED))
            barrel2.set_velocity(direction2.scale(constants.TANK_SPEED))

            # fire the ball 2
            self.fire_timer2 += 1
            if self.fire_timer2 == 20:
                self._audio_service.play_sound(constants.SOUND_RELOAD)
            if fire2 and self.fire_timer2 > 35:
                ball = Ball()
                ball.angle2 += constants.TANK_ANGLE2
                self._audio_service.play_sound(constants.SOUND_FIRE)

                ball.set_ball2()
                # ball2._angle = ball2.angle
                cast["balls"].append(ball._balls[0])
                self.fire_timer2 = 0

    def select_end_game(self):
        self._enter = self._input_service.set_choice()
        choice = self._input_service._dx
        if choice != self._choice:
            self._audio_service.play_sound(constants.SOUND_TOGGLE)
        self._choice = choice
        if choice == 0:
            return 0
        elif choice == -1:
            return -1
        elif choice == 1:
            return 1