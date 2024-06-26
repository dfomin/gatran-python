from dataclasses import dataclass
from typing import List, Tuple

from gatran.action import Action


@dataclass
class TicTacToeAction(Action):
    pos: int

    def __str__(self) -> str:
        return f"pos={self.pos}"

    def apply(self, state: 'TicTacToeState') -> List[Tuple['TicTacToeState', float]]:
        state.field |= 1 << (self.pos * 2 + state.current_player_index())
        state.check_game_over()
        if not state.is_finished:
            state._current_player_index = 1 - state.current_player_index()
        return [(state, 1)]
