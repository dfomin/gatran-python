from dataclasses import dataclass, field
from typing import List

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

    def unique_id(self) -> str:
        return str(self.board)

    def possible_actions(self) -> List[Action]:
        return [ChessAction(move) for move in self.board.legal_moves]

    def clone(self) -> 'State':
        return ChessState(self.current_player_index, self.rewards, self.board.copy())
