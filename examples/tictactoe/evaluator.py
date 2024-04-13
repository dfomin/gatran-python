from gatran.tree.node import Evaluator, Node


class TicTacToeEvaluator(Evaluator):
    def value(self, node: Node) -> float:
        if node.state.is_finished:
            index = node.state.current_player_index()
            opponent = 1 - index
            return node.state.rewards()[index] - node.state.rewards()[opponent]
        else:
            return 0
