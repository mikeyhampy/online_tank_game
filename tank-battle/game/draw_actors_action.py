from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self._color_number = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        choice = False
        self._output_service.clear_screen()
        for key, group in cast.items():

            self._output_service.draw_actors(group, self._color_number)
        self._output_service.flush_buffer()

    def set_color_number(self, number):
        self._color_number = number