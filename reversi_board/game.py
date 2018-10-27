from .board import ReversiBoard
from .consts import (
    REVERSI_BLANK, REVERSI_BLACK, REVERSI_WHITE,
    REVERSI_STATUS_PROGRESS, REVERSI_STATUS_FINISH
)


class ReversiGame(object):
    """docstring"""

    def __init__(self, player1, player2, board=None, turn=None):
        self.players = {
            REVERSI_BLACK: player1,
            REVERSI_WHITE: player2,
        }
        self.status = REVERSI_STATUS_PROGRESS
        if board is list:
            self.board = ReversiBoard(board)
        elif board is ReversiBoard:
            self.board = board
        else:
            self.board = ReversiBoard()
        if turn:
            self.turn = turn
        else:
            self.turn = REVERSI_BLACK

    def process(self):
        place = self.players[self.turn].decide_place(self.board, self.turn)
        self.board.put_piece(place, self.turn)
        next_turn = REVERSI_BLACK if self.turn == REVERSI_WHITE else REVERSI_WHITE
        if self.board.placable_positions(next_turn):
            self.turn = next_turn
        elif not self.board.placable_positions(self.turn):  # どちらも置けなかったら終わり
            self.status = REVERSI_STATUS_FINISH
            return
        return self.turn

    def result(self):
        blacks = (self.board.board == REVERSI_BLACK).sum()
        whites = (self.board.board == REVERSI_WHITE).sum()
        return [blacks, whites]
