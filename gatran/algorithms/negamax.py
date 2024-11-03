import math

from gatran.action import Action
from gatran.agent import Agent
from gatran.state import State
from gatran.tree.node import Evaluator, Node


class NegamaxAgent(Agent):
    def __init__(self, evaluator: Evaluator, max_depth: int):
        self.evaluator = evaluator
        self.max_depth = max_depth

    def choose_action(self, state: State) -> Action:
        node = Node(state, [], {})
        value, action = self.negamax(node, 0)
        return action

    def negamax(self, node: Node, current_depth: int) -> tuple[float, Action | None]:
        if node.state.is_finished or self.max_depth == current_depth:
            return self.evaluator.value(node), None

        max_score, best_action = -math.inf, None
        for action in node.state.possible_actions():
            score = self.get_score(node, action, current_depth)
            if score > max_score:
                max_score = score
                best_action = action
        return max_score, best_action

    def get_score(self, node: Node, action: Action, current_depth: int) -> float:
        current_score = 0
        for next_state, prob in node.state.apply_action(action):
            if next_state.unique_id() not in Node.transposition_table:
                new_node = Node(next_state, [], {})
                Node.transposition_table[next_state.unique_id()] = new_node
            next_score, next_move = self.negamax(Node.transposition_table[next_state.unique_id()], current_depth + 1)
            if next_state.current_player_index() != node.state.current_player_index():
                next_score = -next_score
            current_score += next_score * prob
        return current_score
