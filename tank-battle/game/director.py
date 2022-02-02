from time import sleep

import raylibpy
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        self._start_game = True
        
    def pre_game(self):
        """Starts the pre-game actions"""
        while self._start_game and (constants.PLAYER_TANK_COLOR1 == "" or constants.PLAYER_TANK_COLOR1 == ""):
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            constants

            if raylibpy.window_should_close():
                self._start_game = False
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if raylibpy.window_should_close():
                self._keep_playing = False

            if_end_game = self._script["output"][0]._end_game
            if if_end_game:
                self._keep_playing = False
                

        over_win = self._script["output"][0]._game_message
        end_game_message = self._cast["end_game"]
        sleep(.5)
        while if_end_game:
            #make end of game message
            end_game_message[2].set_text("Play again?")
            end_game_message[3].set_text("YES")
            end_game_message[4].set_text("NO")
            if over_win == "PLAYER 1 WINS!!!":
                end_game_message[1].set_text("PLAYER 1 WINS!!!")
            else:
                end_game_message[0].set_text("PLAYER 2 WINS!!!")
                
            #contol which color is used and if user will play again
            select = self._script["input"][0].select_end_game()
            self._script["output"][1].set_color_number(select)
            self._script["output"][1].execute(self._cast)
            enter = self._script["input"][0]._enter

            #cheks if end game loop ends
            if raylibpy.window_should_close():
                if_end_game = False
            if enter and select == -1:
                if_end_game = False
                constants.KEEP_PLAYING = True
                sleep(1)
            elif enter and select == 1:
                if_end_game = False




    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)