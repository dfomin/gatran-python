from examples.tictactoe.tictactoe_state import TicTacToeState
from gatran.agent import CLIAgent
from gatran.game import Game


def main():
    game = Game(TicTacToeState(), [CLIAgent(), CLIAgent()])
    game.play()


if __name__ == "__main__":
    main()
