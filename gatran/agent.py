from abc import ABC, abstractmethod
from typing import List

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
        print(f"Player {state.current_player_index()} plays")
        print("Actions:")
        for i, action in enumerate(possible_actions):
            print(f"{i}. {action}")
        index = int(input())
        return possible_actions[index]


class CLIAgentInputAction(Agent):
    def choose_action(self, state: State, possible_actions: List[Action]) -> Action:
        print(f"{state}")
        print(f"Player {state.current_player_index()} plays")
        while True:
            print("Input action:")
            value = input()
            for action in possible_actions:
                if str(action) == value:
                    return action
            print("Incorrect action")
