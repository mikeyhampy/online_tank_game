import sys
from game.point import Point
import raylibpy
from game.audio_service import AudioService
from game import constants
from game.connect_fb_db import firebase_python_connect

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._dx = -1
        self._space = False
        self._enter = False
        self._up = False
        self._down = False
        self._right = False
        self._left = False
        self.audio_service = AudioService()
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0
        fire = False

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            dy = 1
        
        if self.is_down_pressed():
            dy = -1

        # fire cannon once
        # if self.is_enter_up():
        #     self._enter = True
        if self.is_enter_pressed(): #and self._enter:
            fire = True
            # self._enter = False

        """
        database code change
        """
        dx2, dy2, fire2 = firebase_python_connect.set_directions(constants.YOUR_USER_NAME, dx, dy, fire, constants.OPPONENT_USER_NAME)

        direction = Point(dx, dy)
        direction2 = Point(dx2 * -1, dy2 * -1)
        return direction, fire, direction2, fire2

    def set_choice(self):
        if self.is_left_pressed() or self.is_a_pressed():
            self._dx = -1
        
        if self.is_right_pressed() or self.is_d_pressed():
            self._dx = 1

        if self.is_enter_pressed() or self.is_space_pressed():
            self.audio_service.play_sound(constants.SOUND_TOGGLE)
            self._space = False
            self._enter = False
            return True
        else:
            return False

    def choose_color1(self):
        """
        choose colors for tank 1
        """
        dx = 0
        dy = 0
        if self._enter == False:
            # choose left
            if self.is_left_up():
                self._left = True
            if self.is_left_pressed() and self._left:
                dx = -1
                self._left = False
            
            # choose right
            if self.is_right_up():
                self._right = True
            if self.is_right_pressed() and self._right:
                dx = 1
                self._right = False
            
            # choose up
            if self.is_up_up():
                self._up = True
            if self.is_up_pressed() and self._up:
                dy = -1
                self._up = False
            
            # choose down
            if self.is_down_up():
                self._down = True
            if self.is_down_pressed() and self._down:
                dy = 1
                self._down = False

            # select (enter)
            if self.is_enter_pressed():
                self._enter = True
                self.audio_service.play_sound(constants.SOUND_TOGGLE)

        firebase_python_connect.set_pointer(constants.YOUR_USER_NAME, dx, dy, self._enter)
        direction = Point(dx, dy)
        return direction, self._enter
    def  choose_color2(self):
        """
        choose colors for tank 2
        """

        dx, dy, self._space = firebase_python_connect.get_pointer(constants.OPPONENT_USER_NAME)
        direction = Point(dx, dy)
        return direction, self._space

    def window_should_close(self):
        return raylibpy.window_should_close()

    """
    Directional key inputs
    """
    # left pressed and not pressed
    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)
    def is_left_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_LEFT)

    # right pressed and not pressed
    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)
    def is_right_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_RIGHT)

    # up pressed and not pressed
    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)
    def is_up_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_UP)

    # down pressed and not pressed
    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)
    def is_down_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_DOWN)

    # a pressed and not pressed
    def is_a_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)
    def is_a_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_A)

    # d pressed and not pressed
    def is_d_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)
    def is_d_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_D)

    # w pressed and not pressed
    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)
    def is_w_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_W)

    # s pressed and not pressed
    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)
    def is_s_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_S)

    # space pressed and not pressed
    def is_space_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_SPACE)
    def is_space_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_SPACE)

    # enter pressed and not pressed
    def is_enter_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_ENTER)
    def is_enter_up(self):
        return raylibpy.is_key_up(raylibpy.KEY_ENTER)