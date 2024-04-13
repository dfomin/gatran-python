from examples.chess.chess_state import ChessState
from examples.chess.evaluator import ChessEvaluator
from gatran.agent import CLIAgent
from gatran.algorithms.negamax import NegamaxAgent
from gatran.game import Game


def main():
    game = Game(ChessState(), [CLIAgent(), NegamaxAgent(ChessEvaluator(), 3)])
    game.play()


if __name__ == "__main__":
    main()
