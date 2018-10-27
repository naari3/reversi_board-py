from random import choice

class BasePlayer(object):
    def __init__(self):
        pass

    def decide_place(self, board, turn):
        raise NotImplementedError


class RandomPlayer(BasePlayer):
    def decide_place(self, board, turn):
        return choice(board.placable_positions(turn))
