class TableWeights:
    def __init__(self, color):
        from models.players.minimax import Minimax

        self.color = color
        self.minimax = Minimax(color)

        m = {'H':10,'P':-3,'I':5,'C':3,'M':3,'N':-1,'E':1,'A':0}

        self.WEIGHTS = [
            [m['H'], m['P'], m['I'], m['M'], m['M'], m['I'], m['P'], m['H']],
            [m['P'], m['P'], m['C'], m['N'], m['N'], m['C'], m['P'], m['P']],
            [m['I'], m['C'], m['I'], m['E'], m['E'], m['I'], m['C'], m['I']],
            [m['M'], m['N'], m['E'], m['A'], m['A'], m['E'], m['N'], m['M']],
            [m['M'], m['N'], m['E'], m['A'], m['A'], m['E'], m['N'], m['M']],
            [m['I'], m['C'], m['I'], m['E'], m['E'], m['I'], m['C'], m['I']],
            [m['P'], m['P'], m['C'], m['N'], m['N'], m['C'], m['P'], m['P']],
            [m['H'], m['P'], m['I'], m['M'], m['M'], m['I'], m['P'], m['H']]
        ]

    def play(self, board):
        return self.minimax(self.color, board, 3, self.heuristic_a)[1]

    def heuristic_a(self, player, board):
        opponent = board._opponent(self.color)
        total = 0
        for xy in board._squares():
            pos = map(int,str(xy))
            if board.get_square_color(pos[0], pos[1]) == self.color:
                total += self.WEIGHTS[pos[0]-1][pos[1]-1]
            elif board.get_square_color(pos[0], pos[1]) == opponent:
                total -= self.WEIGHTS[pos[0]-1][pos[1]-1]
        return total
