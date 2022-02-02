from game.actor import Actor
from game.point import Point
from game import constants
import raylibpy

class Selectorbox():
    def __init__(self):
        self._selectors = []

    def set_selector_boxes(self):
        # selector box 1
        xy_dif_width = constants.SELECTOR_LINE_WIDTH * 2
        line_width = constants.SELECTOR_LINE_WIDTH * 4
        x1 = constants.SELECTOR_X - (xy_dif_width * 2)
        y1 = constants.SELECTOR_Y - (xy_dif_width * 2)
        width1 = constants.FULL_TANK_WIDTH + (line_width * 2)
        height1 = constants.FULL_TANK_HEIGHT + (line_width * 2)
        selector1 = Actor()
        selector1._box_line_width = constants.SELECTOR_LINE_WIDTH
        selector1._colors_of_lines = raylibpy.RED
        position1 = Point(x1, y1)
        selector1.set_position(position1)
        selector1.set_width(width1)
        selector1.set_height(height1)
        self._selectors.append(selector1)

        #selector box 2
        x2 = constants.SELECTOR_X - xy_dif_width
        y2 = constants.SELECTOR_Y - xy_dif_width
        width2 = constants.FULL_TANK_WIDTH + line_width
        height2 = constants.FULL_TANK_HEIGHT + line_width
        selector2 = Actor()
        selector2._box_line_width = constants.SELECTOR_LINE_WIDTH
        selector2._colors_of_lines = raylibpy.BLUE
        position2 = Point(x2, y2)
        selector2.set_position(position2)
        selector2.set_width(width2)
        selector2.set_height(height2)
        self._selectors.append(selector2)

        title = Actor()

        position = Point(0, 50)
        title.set_position(position)
        title.set_image("pick", "color")
        self._selectors.append(title)

    def get_selector_boxes(self):
        return self._selectors