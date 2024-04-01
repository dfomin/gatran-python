from gatran.tree.node import Node


class NegamaxNode(Node):
    def value(self) -> float:
        if self.state.is_finished:
            index = self.state.current_player_index
            opponent = 1 - index
            return self.state.rewards[index] - self.state.rewards[opponent]
        else:
            return 0
