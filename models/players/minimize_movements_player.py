class MinimizeMovements:

    def __init__(self, color):
        from models.players.minimax import Minimax

        self.color = color
        self.minimax = Minimax(color, Minimax.MIN)

    def play(self, board):
        return self.minimax(self.color, board, 3, self.heuristic_a)[1]

    def heuristic_a(self, player, board):
        return len(board.valid_moves(player))
