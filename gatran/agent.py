from abc import ABC, abstractmethod
from typing import List

from examples.tictactoe.tictactoe_action import TicTacToeAction
from gatran.action import Action
from gatran.state import State


class Agent(ABC):
    @abstractmethod
    def choose_action(self, state: State, possible_actions: List[Action]) -> Action:
        raise NotImplementedError

    def on_action_applied(self, action: Action, new_state: State):
        pass


class CLIAgent(Agent):
    def choose_action(self, state: State, possible_actions: List[Action]) -> Action:
        print(f"{state}")
        print(f"Player {state.current_player_index} plays")
        print("Actions:")
        for i, action in enumerate(possible_actions):
            print(f"{i}. {action}")
        index = int(input())
        return possible_actions[index]