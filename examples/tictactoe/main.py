from examples.tictactoe.evaluator import TicTacToeEvaluator
from examples.tictactoe.tictactoe_state import TicTacToeState
from gatran.agent import CLIAgent
from gatran.algorithms.negamax import NegamaxAgent
from gatran.game import Game


def main():
    game = Game(TicTacToeState(), [CLIAgent(), NegamaxAgent(TicTacToeEvaluator())])
    game.play()


if __name__ == "__main__":
    main()
