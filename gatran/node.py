from dataclasses import dataclass
from typing import Dict, List

from action import Action

from gatran.state import State


@dataclass
class Node:
    state: State
    wins: int
    total_games: int
    parents: List["Node"]
    children: Dict[Action, List["Node"]]
