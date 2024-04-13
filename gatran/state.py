from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from gatran.action import Action


class State(ABC):
    def __eq__(self, other) -> bool:
        return self.unique_id() == other.unique_id

    def __hash__(self) -> int:
        return hash(self.unique_id())

    def current_player_index(self) -> int:
        raise NotImplementedError

    def rewards(self) -> Optional[List[float]]:
        raise NotImplementedError

    @property
    def is_finished(self):
        return self.rewards() is not None

    def apply_action(self, action: Action) -> List[Tuple['State', float]]:
        return action.apply(self.clone())

    @abstractmethod
    def unique_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def possible_actions(self) -> List[Action]:
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> 'State':
        raise NotImplementedError
