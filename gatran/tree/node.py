from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Tuple, ClassVar, Protocol

from gatran.action import Action
from gatran.state import State


@dataclass
class Node(ABC):
    state: State
    parents: List['Node']
    children: Dict[Action, Tuple[str, float]]

    transposition_table: ClassVar[Dict[str, 'Node']] = {}


class Evaluator(Protocol):
    @abstractmethod
    def value(self, node: Node) -> float:
        raise NotImplementedError
