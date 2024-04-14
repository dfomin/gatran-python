import random
from typing import List

from gatran.agent import Agent
from gatran.state import State


class Game:
    def __init__(self, state: State, agents: List[Agent]):
        self.state = state
        self.agents = agents

    def play(self):
        while not self.state.is_finished:
            agent = self.agents[self.state.current_player_index()]
            action = agent.choose_action(self.state)
            possible_states = self.state.apply_action(action)
            next_state = random.choices([ps[0] for ps in possible_states], weights=[ps[1] for ps in possible_states])[0]
            self.state = next_state
            for opponent in self.agents:
                if opponent != agent:
                    opponent.on_action_applied(action, self.state)
        print(self.state)
        print(self.state.rewards())
