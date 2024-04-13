from typing import List, Tuple

from chess import Move

from gatran.action import Action


class ChessAction(Action):
    def __init__(self, move: Move):
        self.move = move

    def __str__(self) -> str:
        return str(self.move)

    def apply(self, state: 'ChessState') -> List[Tuple['ChessState', float]]:
        state.board.push(self.move)
        return [(state, 1.0)]
