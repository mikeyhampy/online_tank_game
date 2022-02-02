import os
os.environ['RAYLIB_BIN_PATH'] = r'../online_tank_game/tank-battle'

import random
import raylibpy
from game import constants
from game.director import Director
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.colors import Colors
from game.selector_box import Selectorbox
from game.wall import Wall
from game.lives import Lives
from game.tank import Tank
from game.barrel import Barrel
from game.choose_color import Choosecolor
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.check_end import CheckEnd
from game.end_game import EndGame

def main():
    # Create the script {key: tag, value: list}

    open_window_loop = 0
    while(constants.KEEP_PLAYING):
        constants.KEEP_PLAYING = False
        constants.TANK_ANGLE = 180
        constants.TANK_ANGLE2 = 360
        constants.BALL_CHANGE_X1 = 0
        constants.BALL_CHANGE_X2 = 0
        constants.PLAYER_TANK_COLOR1 = ""
        constants.PLAYER_TANK_COLOR2 = ""
        # create the cast {key: tag, value: list}
        cast = {}
        cast["colors"] = []
        # TODO: color options for the tanks
        colors = Colors()
        colors.set_colors()
        cast["colors"] = colors.get_colors()

        cast["selector"] = []
        selector = Selectorbox()
        selector.set_selector_boxes()
        cast["selector"] = selector.get_selector_boxes()

        # Create the script {key: tag, value: list}

        script = {}

        input_service = InputService()
        output_service = OutputService()
        physics_service = PhysicsService()
        audio_service = AudioService()

        choose_colors = Choosecolor(audio_service)
        move_actors_action = MoveActorsAction()
        control_actors_action = ControlActorsAction(input_service, audio_service)
        draw_actors_action = DrawActorsAction(output_service)
        handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
        handle_off_screen_action = HandleOffScreenAction(audio_service)
        check_end = CheckEnd(audio_service)

        # TODO: Create additional actions here and add them to the script

        script["input"] = [control_actors_action]
        script["update"] = [choose_colors, handle_collisions_action]
        script["output"] = [draw_actors_action]

        # Start the game run once
        if open_window_loop == 0:
            output_service.open_window("Tank Battle")
            audio_service.start_audio()
            open_window_loop = 1
        audio_service.play_sound(constants.SOUND_TOGGLE)
        audio_service.play_sound(constants.SOUND_TOGGLE)

        """
        Set up game
        """
        director = Director(cast, script)
        director.pre_game()

        
        # create the cast {key: tag, value: list}
        cast = {}

        cast["walls"] = []
        # TODO: Create walls here and add them to the list
        wall = Wall()
        wall.set_walls()
        cast["walls"] = wall.get_walls()
        
        cast["lives1"] = []
        cast["lives2"] = []
        lives = Lives()
        lives.set_lives()
        cast["lives1"] = lives.get_lives1()
        cast["lives2"] = lives.get_lives2()  

        cast["balls"] = []

        cast["barrel"] = []
        # barrel actor
        barrel = Barrel()
        barrel.set_barrel()
        cast["barrel"] = barrel.get_barrel()

        cast["tank"] = []
        # TODO: Create a tank here and add it to the list
        tank = Tank()
        tank.set_tank()
        cast["tank"] = tank.get_tank()

        cast["end_game"] = []
        end_game = EndGame()
        end_game.set_end_game()
        cast["end_game"] = end_game.get_end_game()

        # Create the script {key: tag, value: list}
        script = {}

        # TODO: Create additional actions here and add them to the script
        script["input"] = [control_actors_action]
        script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
        script["output"] = [check_end, draw_actors_action]
   
        """
        Play game
        """
        audio_service.play_sound(constants.SOUND_START)
        director = Director(cast, script)
        director.start_game()

        output_service.flush_buffer()

    raylibpy.close_window()

if __name__ == "__main__":
    main()
