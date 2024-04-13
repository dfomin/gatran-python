from typing import Tuple, Dict

import chess

from examples.chess.chess_state import ChessState
from gatran.tree.node import Evaluator, Node


PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
}


def calculate_material(board: chess.Board) -> Tuple[float, float]:
    white_score = 0
    black_score = 0

    for piece_type, value in PIECE_VALUES.items():
        white_score += len(board.pieces(piece_type, chess.WHITE)) * value
        black_score += len(board.pieces(piece_type, chess.BLACK)) * value

    return white_score, black_score


class ChessEvaluator(Evaluator):
    def value(self, node: Node) -> float:
        if isinstance(node.state, ChessState):
            rewards = node.state.rewards()
            if rewards is not None:
                player = node.state.current_player_index()
                opponent = 1 - node.state.current_player_index()
                return rewards[player] * 1000 - rewards[opponent] * 1000

            white, black = calculate_material(node.state.board)
            if node.state.current_player_index() == 0:
                return white - black
            else:
                return black - white
