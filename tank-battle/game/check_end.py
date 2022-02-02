import raylibpy
from game import constants
from game.action import Action

class CheckEnd(Action):
    """
    Check if the game ends
    """

    def __init__(self, audio_service):
        super().__init__()
        self._audio_service = audio_service
        self._end_game = False
        self._game_message = ""
        self._sound = raylibpy

    def execute(self, cast):
        player1 = cast["lives1"]
        player2 =cast["lives2"]

        if len(player1) == 0:
            self._end_game = True
            self._game_message = "PLAYER 2 WINS!!!"

        if len(player2) == 0:
            self._end_game = True
            self._game_message = "PLAYER 1 WINS!!!"