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
        if state.board.outcome():
            if state.board.outcome().winner is None:
                state._rewards = [0.5, 0.5]
            elif state.board.outcome().winner:
                state._rewards = [1, 0]
            else:
                state._rewards = [0, 1]
        return [(state, 1.0)]
