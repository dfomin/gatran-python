import math

from gatran.action import Action
from gatran.agent import Agent
from gatran.state import State
from gatran.tree.node import Node, Evaluator


class NegascoutAgent(Agent):
    def __init__(self, evaluator: Evaluator, max_depth: int):
        self.evaluator = evaluator
        self.max_depth = max_depth

    def choose_action(self, state: State) -> Action:
        node = Node(state, [], {})
        value, action = self.negascout(node, 0, -math.inf, math.inf)
        print(value)
        return action

    def negascout(self, node: Node, current_depth: int, alpha: float, beta: float) -> tuple[float, Action | None]:
        if node.state.is_finished or self.max_depth == current_depth:
            return self.evaluator.value(node), None

        max_score, best_action = -math.inf, None
        for i, action in enumerate(node.state.possible_actions()):
            if i == 0:
                score = self.get_score(node, action, current_depth, alpha, beta)
            else:
                score = self.get_score(node, action, current_depth, alpha, alpha + 1)

                if alpha < score < beta:
                    score = self.get_score(node, action, current_depth, alpha, beta)

            if score > max_score:
                max_score = score
                best_action = action

            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return max_score, best_action

    def get_score(
        self,
        node: Node,
        action: Action,
        current_depth: int,
        alpha: float,
        beta: float,
    ) -> float:
        current_score = 0
        for next_state, prob in node.state.apply_action(action):
            if next_state.unique_id() not in Node.transposition_table:
                new_node = Node(next_state, [], {})
                Node.transposition_table[next_state.unique_id()] = new_node
            next_score, next_move = self.negascout(
                Node.transposition_table[next_state.unique_id()],
                current_depth + 1,
                -beta,
                -alpha,
            )
            current_player = node.state.current_player_index()
            next_player = next_state.current_player_index()
            if current_player != next_player:
                next_score = -next_score

            current_score += next_score * prob
        return current_score
