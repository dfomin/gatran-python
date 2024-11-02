from chess import Move

from gatran.action import Action


class ChessAction(Action):
    def __init__(self, move: Move):
        self.move = move

    def __str__(self) -> str:
        return str(self.move)
