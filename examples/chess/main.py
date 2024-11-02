from examples.chess.chess_state import ChessState
from examples.chess.evaluator import ChessEvaluator
from gatran.agent import CLIAgentInputAction
from gatran.algorithms.negascout import NegascoutAgent
from gatran.game import Game


def main():
    game = Game(ChessState(), [CLIAgentInputAction(), NegascoutAgent(ChessEvaluator(), 4)])
    game.play()


if __name__ == "__main__":
    main()
