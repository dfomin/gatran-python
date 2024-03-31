from dataclasses import dataclass, replace
from typing import List

from examples.tictactoe.tictactoe_action import TicTacToeAction
from gatran.action import Action
from gatran.state import State


LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


@dataclass
class TicTacToeState(State):
    field: int = 0

    def __str__(self) -> str:
        result = ""
        for row in range(3):
            for col in range(3):
                index = row * 3 + col
                if 0b1 << (2 * index) & self.field != 0:
                    ch = "X"
                elif 0b10 << (2 * index) & self.field != 0:
                    ch = "O"
                else:
                    ch = " "
                result += ch
                if col != 2:
                    result += "|"
            if row != 2:
                result += "\n-+-+-"
                result += "\n"
        return result

    def unique_id(self) -> str:
        return str(self.field)

    def possible_actions(self) -> List[Action]:
        if self.is_finished:
            return []
        return [TicTacToeAction(i) for i in range(9) if self.field & (0b11 << (2 * i)) == 0]

    def check_game_over(self):
        for line in LINES:
            if all([0b11 & self.field >> (2 * i) == 1 for i in line]):
                self.rewards = [1, 0]
                return
            elif all([0b11 & self.field >> (2 * i) == 2 for i in line]):
                self.rewards = [0, 1]
                return
            elif all([0b11 & self.field >> (2 * i) != 0 for i in range(9)]):
                self.rewards = [0, 0]
                return

    def clone(self) -> 'State':
        return replace(self)
