from examples.tictactoe.evaluator import TicTacToeEvaluator
from examples.tictactoe.tictactoe_state import TicTacToeState
from gatran.agent import CLIAgent
from gatran.algorithms.negascout import NegascoutAgent
from gatran.game import Game


def main():
    game = Game(TicTacToeState(), [CLIAgent(), NegascoutAgent(TicTacToeEvaluator(), 10)])
    game.play()


if __name__ == "__main__":
    main()
