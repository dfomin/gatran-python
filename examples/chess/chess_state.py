from dataclasses import dataclass, field
from typing import List, Optional

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

    def rewards(self) -> Optional[List[float]]:
        if self.board.is_game_over():
            if self.board.is_checkmate():
                return [float(self.board.turn != chess.WHITE), float(self.board.turn != chess.BLACK)]
            else:
                return [0.5, 0.5]
        return None

    def unique_id(self) -> str:
        return str(self.board)

    def possible_actions(self) -> List[Action]:
        return [ChessAction(move) for move in self.board.legal_moves]

    def clone(self) -> 'State':
        return ChessState(self.board.copy())
