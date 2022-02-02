from game.actor import Actor
from game.point import Point
from game import constants

class Colors():
    def __init__(self):
        self._tank_colors = []
        self._color_choice = ""
        self._tank_full_color = ""

    def set_colors(self):
        color_of_tank = ""

        # size and position and gap
        width = constants.FULL_TANK_WIDTH
        height = constants.FULL_TANK_HEIGHT
        color_y = constants.SELECTOR_Y
        gap_in_x = constants.SELECTOR_X
        line_width = constants.SELECTOR_LINE_WIDTH
        gap_in_y = 74

        # loops through and make oal the tank color actors
        j = 0
        while(j < 2):
            color_x = gap_in_x
            i = 0
            while(i < 3):
                # set position and size
                colors = Actor()
                colors._box_line_width = line_width
                position = Point(color_x, color_y)
                colors.set_position(position)
                colors.set_width(width)
                colors.set_height(height)

                # make the tanks difforent colors and set image
                if j == 0:
                    if i == 0:
                        #color_of_tank = constants.IMAGE_FULL1_RED
                        colors._color_actor = constants.RED
                    elif i == 1:
                        #color_of_tank = constants.IMAGE_FULL1_GRAY
                        colors._color_actor = constants.GRAY
                    elif i == 2:
                        #color_of_tank = constants.IMAGE_FULL1_BLUE
                        colors._color_actor = constants.BLUE
                if j == 1:
                    if i == 0:
                        #color_of_tank = constants.IMAGE_FULL1_ORANGE
                        colors._color_actor = constants.ORANGE
                    elif i == 1:
                        #color_of_tank = constants.IMAGE_FULL1_YELLOW
                        colors._color_actor = constants.YELLOW
                    elif i == 2:
                        #color_of_tank = constants.IMAGE_FULL1_GREEN
                        colors._color_actor = constants.GREEN
                        
                colors.set_image("full1", colors._color_actor)
                self._tank_colors.append(colors)

                # update position and i (x_pos) looper
        #92 144 92 144 92 144 92
        #116.25 45 "92" 45 "92" 45 "92"  73.75 74
                i += 1
                color_x += gap_in_x + width
            color_y += gap_in_y + height
            j += 1

    def get_colors(self):
        return self._tank_colors