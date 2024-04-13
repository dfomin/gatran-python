import math
from typing import Tuple, Optional, List

from gatran.action import Action
from gatran.agent import Agent
from gatran.state import State
from gatran.tree.node import Node, Evaluator


class NegamaxAgent(Agent):
    def __init__(self, evaluator: Evaluator, max_depth: int):
        self.evaluator = evaluator
        self.max_depth = max_depth

    def choose_action(self, state: State, possible_actions: List[Action]) -> Action:
        node = Node(state, [], {})
        _, action = self.negamax(node, self.max_depth, 0)
        return action

    def negamax(self, node: Node, max_depth: int, current_depth: int) -> Tuple[float, Optional[Action]]:
        if node.state.is_finished or max_depth == current_depth:
            return self.evaluator.value(node), None

        max_score, best_action = -math.inf, None
        for action in node.state.possible_actions():
            current_score = 0
            for next_state, prob in node.state.apply_action(action):
                if next_state.unique_id() not in node.transposition_table:
                    new_node = Node(next_state, [], {})
                    node.transposition_table[next_state.unique_id()] = new_node
                next_score, next_move = self.negamax(
                    node.transposition_table[next_state.unique_id()],
                    max_depth,
                    current_depth + 1)
                if next_state.current_player_index() != node.state.current_player_index():
                    next_score = -next_score
                current_score += next_score * prob
            if current_score > max_score:
                max_score = current_score
                best_action = action
        return max_score, best_action
