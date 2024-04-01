import math
from typing import Tuple, Optional, cast, List

from gatran.action import Action
from gatran.agent import Agent
from gatran.state import State
from gatran.tree.negamax_node import NegamaxNode


class NegamaxAgent(Agent):
    def choose_action(self, state: State, possible_actions: List[Action]) -> Action:
        node = NegamaxNode(state, [], {})
        _, action = negamax(node, 10, 0)
        return action


def negamax(node: NegamaxNode, max_depth: int, current_depth: int) -> Tuple[float, Optional[Action]]:
    if node.state.is_finished or max_depth == current_depth:
        return node.value(), None

    max_score, best_action = -math.inf, None
    for action in node.state.possible_actions():
        current_score = 0
        for next_state, prob in node.state.apply_action(action):
            if next_state.unique_id() not in node.transposition_table:
                new_node = NegamaxNode(next_state, [], {})
                node.transposition_table[next_state.unique_id()] = new_node
            next_score, next_move = negamax(
                cast(NegamaxNode, node.transposition_table[next_state.unique_id()]),
                max_depth,
                current_depth + 1)
            if next_state.current_player_index != node.state.current_player_index:
                next_score = -next_score
            current_score += next_score * prob
        if current_score > max_score:
            max_score = current_score
            best_action = action
    return max_score, best_action
