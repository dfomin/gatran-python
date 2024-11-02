from dataclasses import dataclass

from gatran.action import Action


@dataclass
class TicTacToeAction(Action):
    pos: int

    def __str__(self) -> str:
        return f"pos={self.pos}"
