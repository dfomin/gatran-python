from dataclasses import dataclass, field

import chess
from chess import Board

from examples.chess.chess_action import ChessAction
from gatran.action import Action
from gatran.state import State


@dataclass
class ChessState(State):
    board: Board = field(default_factory=chess.Board)

    def __str__(self):
        return str(self.board)

    def current_player_index(self) -> int:
        return int(self.board.turn == chess.BLACK)

    def rewards(self) -> list[float] | None:
        if self.board.outcome():
            if self.board.outcome().winner is None:
                return [0.5, 0.5]
            elif self.board.outcome().winner:
                return [1.0, 0.0]
            else:
                return [0.0, 1.0]
        return None

    def unique_id(self) -> str:
        return self.board.fen()

    def possible_actions(self) -> list[Action]:
        return [ChessAction(move) for move in self.board.legal_moves]

    def apply_action(self, action: ChessAction) -> list[tuple['State', float]]:
        state = self.clone()
        state.board.push(action.move)
        return [(state, 1.0)]

    def clone(self) -> 'State':
        return ChessState(self.board.copy())
