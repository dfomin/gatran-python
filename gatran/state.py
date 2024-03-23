from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Tuple

from action import Action


@dataclass
class State(ABC):
    current_player_index: int = 0
    winner: Optional[int] = 0
    
    def __eq__(self, other) -> bool:
        return self.unique_id() == other.unique_id

    def __hash__(self) -> int:
        return hash(self.unique_id)

    @abstractmethod
    def unique_id(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def possible_actions(self) -> List[Action]:
        raise NotImplementedError

    @abstractmethod
    def apply_action(self) -> List[Tuple[int, float]]:
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> "State":
        raise NotImplementedError
