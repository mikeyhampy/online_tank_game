from game.actor import Actor
from game.point import Point
from game import constants

class EndGame():
    def __init__(self):
        self._end_games = []

    def set_end_game(self):
        youwin= Actor()
        position = Point(100, 30)
        youwin.set_position(position)
        youwin.set_text("")
        self._end_games.append(youwin)

        gameover = Actor()
        position = Point(100, 30)
        gameover.set_position(position)
        gameover.set_text("")
        self._end_games.append(gameover)

        playagain = Actor()
        position = Point(200, 30 * 2 + 72)
        playagain.set_position(position)
        playagain.set_text("")
        self._end_games.append(playagain)

        yes = Actor()
        position = Point(200, 30 * 3 + 72 * 2)
        yes.set_position(position)
        yes.set_text("")
        self._end_games.append(yes)

        no = Actor()
        position = Point(450, 30 * 3 + 72 * 2)
        no.set_position(position)
        no.set_text("")
        self._end_games.append(no)


    def get_end_game(self):
        return self._end_games
