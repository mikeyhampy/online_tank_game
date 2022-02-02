from game import constants
from game.action import Action
from game.point import Point

class Choosecolor(Action):
    """A code template for changing selector position and choose a color
    
    Stereotype:
    Controller

    Attributes:
    _input_service (InputService): An instance of InputService.
    """
    def __init__(self, audio_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._color_index = [[0, 1, 2], [3, 4, 5]]
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
        cast (dict): The game actors {key: tag, value: list}.
        """
        selector_p1 = cast["selector"][0]
        selector_p2 = cast["selector"][1]
        tank_color = cast["colors"]

        # get position and velocity of the selectors
        velocity1 = selector_p1.get_velocity()
        velocity2 = selector_p2.get_velocity()
        dx1 = velocity1.get_x()
        dy1 = velocity1.get_y()
        dx2 = velocity2.get_x()
        dy2 = velocity2.get_y()

        # get selectors current index in reference to self._color_index
        selector_index_x1 = selector_p1._color_index_x
        selector_index_x2 = selector_p2._color_index_x
        selector_index_y1 = selector_p1._color_index_y
        selector_index_y2 = selector_p2._color_index_y

        # get new ingex 2D index
        selector_index_x1 = ((selector_index_x1 + dx1) % 3)
        selector_index_x2 = ((selector_index_x2 + dx2) % 3)
        selector_index_y1 = ((selector_index_y1 + dy1) % 2)
        selector_index_y2 = ((selector_index_y2 + dy2) % 2)

        # get 1D index to call colors actor
        selected_tank_index1 = self._color_index[selector_index_y1][selector_index_x1]
        selected_tank_index2 = self._color_index[selector_index_y2][selector_index_x2]

        # get colors actor to call referent for position
        selected_color_position1 = tank_color[selected_tank_index1]
        selected_color_position2 = tank_color[selected_tank_index2]

        selected_color_position1
        selected_color_position2
        color_position1 = selected_color_position1.get_position()
        color_position2 = selected_color_position2.get_position()

        color_x1 = color_position1.get_x()
        color_y1 = color_position1.get_y()
        color_x2 = color_position2.get_x()
        color_y2 = color_position2.get_y()

        #move boxes
        selector_p1._color_index_x = selector_index_x1
        selector_p2._color_index_x = selector_index_x2
        selector_p1._color_index_y = selector_index_y1
        selector_p2._color_index_y = selector_index_y2

        position1 = Point(color_x1 - (constants.SELECTOR_LINE_WIDTH * 4), color_y1  - (constants.SELECTOR_LINE_WIDTH * 4))
        selector_p1.set_position(position1)

        position2 = Point(color_x2 - (constants.SELECTOR_LINE_WIDTH * 2), color_y2 - (constants.SELECTOR_LINE_WIDTH * 2))
        selector_p2.set_position(position2)

        """
        PLAY SOUND
        """
        if dx1 != 0 or dy1 != 0 or dx2 != 0 or dy2 !=0:
            self._audio_service.play_sound(constants.SOUND_TOGGLE)