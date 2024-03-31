from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Tuple

from gatran.action import Action


@dataclass
class State(ABC):
    current_player_index: int = 0
    rewards: Optional[List[int]] = None

    def __eq__(self, other) -> bool:
        return self.unique_id() == other.unique_id

    def __hash__(self) -> int:
        return hash(self.unique_id())

    @property
    def is_finished(self):
        return self.rewards is not None

    def apply_action(self, action: Action) -> List[Tuple['State', float]]:
        possible_states = action.apply(self.clone())
        for possible_state in possible_states:
            possible_state[0].check_game_over()
        return possible_states

    @abstractmethod
    def unique_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def possible_actions(self) -> List[Action]:
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> 'State':
        raise NotImplementedError
