from abc import ABC, abstractmethod
from typing import List, Tuple


class Action(ABC):
    @abstractmethod
    def apply(self, state: 'State') -> List[Tuple['State', float]]:
        raise NotImplementedError
