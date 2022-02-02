import sys
from game import constants
import raylibpy

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        None
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._textures = {}
        self._color_number = 0

    def open_window(self, title):
        """
        Opens a new window with the provided title.
        """
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, title)
        raylibpy.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.begin_drawing()
        raylibpy.clear_background(raylibpy.BLACK)
        #vector = raylibpy.Vector2(0, 0)
        #raylibpy.draw_texture(constants.IMAGE_BACKGROUND, 0, 0, raylibpy.WHITE)
        #raylibpy.draw_texture_ex(constants.IMAGE_BACKGROUND, vector, 0, 1, raylibpy.WHITE)

    def draw_box_ex(self, rectangle, width_of_line, color):
        """
        Draws at rectangular box with the provided specifications.
        """
        if color == None:
            color = raylibpy.BLACK
        raylibpy.draw_rectangle_lines_ex(rectangle, width_of_line, color)

    def draw_text(self, x, y, text, text_color):
        """
        Outputs the provided text at the desired location.
        """
        color = raylibpy.LIGHTGRAY

        if text == "YES" and text_color == -1:
            color = raylibpy.GREEN
        elif text == "NO" and text_color == 1:
            color = raylibpy.RED

        raylibpy.draw_text(text, x + 5, y + 5, constants.DEFAULT_FONT_SIZE, color)

    def draw_image_ex(self, x, y, angle, scale, image):
        """
        Outputs the provided image on the screen.
        """
        if image not in self._textures.keys():

            loaded = raylibpy.load_texture(image)
            self._textures[image] = loaded
        vector = raylibpy.Vector2(x, y)
        texture = self._textures[image]
        raylibpy.draw_texture_ex(texture, vector, angle, scale, raylibpy.WHITE)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        position = actor.get_position()
        angle = actor._angle
        color_of_line = actor._colors_of_lines
        width_of_line = actor._box_line_width
        scale = actor._scale
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        vc = raylibpy.Vector2(width / 2, 0)
        rectangle = raylibpy.Rectangle(x, y, width, height)

        if actor.has_image():
            image = actor.get_image()
            self.draw_image_ex(x, y, angle, scale, image)
            #self.draw_image(x - width / 2, y - height / 2, image)
        elif actor.has_text():
            text = actor.get_text()
            self.draw_text(x, y, text, self._color_number)
        elif width > 0 and height > 0:
            self.draw_box_ex(rectangle, width_of_line, color_of_line)
        
    def draw_actors(self, actors, color_number):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        self._color_number = color_number
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.end_drawing()
