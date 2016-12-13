class GreedyMinimizer:
    BLACK, WHITE = '@', 'o'
    def __init__(self, color):
        self.color = color
        self.WEIGHTS = [
            0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
            0,  10,  -3,   5,   3,   3,   5,  -3,  10,   0,
            0,  -3,  -3,   3,  -1,  -1,   3,  -3,  -3,   0,
            0,   5,   3,   5,   1,   1,   5,   3,   5,   0,
            0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
            0,   3,  -1,   1,   0,   0,   1,  -1,   3,   0,
            0,   5,   3,   5,   1,   1,   5,   3,   5,   0,
            0,  -3,  -3,   3,  -1,  -1,   3,  -3,  -3,   0,
            0,  10, -10,   5,   3,   3,   5,  -3,  10,   0,
            0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
        ]

    def play(self, board):
        return self.greedy_minimizer(self.color, board, 7, self.heuristic_a)[1]

    def last_score(self, board):
        score = board.score()[0] if self.color == GreedyMinimizer.WHITE else board.score()[1]
        return score if score == 0 else -(score/abs(score))*sum(map(abs, self.WEIGHTS))

    def heuristic_a(self, MAX, board):
        MIN = board._opponent(MAX)
        total = 0
        for xy in board._squares():
            pos = map(int,str(xy))
            if board.get_square_color(pos[0], pos[1]) == MAX:
                total += self.WEIGHTS[xy]
            elif board.get_square_color(pos[0], pos[1]) == MIN:
                total -= self.WEIGHTS[xy]
        return total

    # retorna a posicao que deve ser jogada para seu oponente ter o menor numero de movimentos possiveis
    def minimize_opponents_movement(self, MAX, board):
        valid_moves_max = board.valid_moves(MAX)
        MIN = board._opponent(MAX)
        minimize_movement_list = []
        for possible_move in valid_moves_max:
            copy_board = board
            new_state = self.simulate_movement(possible_move, copy_board, MAX)
            score = len(new_state.valid_moves(MIN))
            minimize_movement_list.append( (score, possible_move) )
        min_move = min(minimize_movement_list)
        return min_move

    # finge que tu vai mover e pega o tabuleiro que resulta desse movimento
    def simulate_movement(self, move, board, player):
        board.play(move, player)
        board._reverse(move, player)
        return board

    def greedy_minimizer(self, MAX, board, depth, heuristic_fn):
        (best_score, best_move) = (None, None)
        if depth == 0:
            (best_score, best_move) = (heuristic_fn(MAX, board), None)
            return (best_score, best_move)

        MIN = board._opponent(MAX)
        valid_moves_max = board.valid_moves(MAX)

        if not valid_moves_max:
            if not board.valid_moves(MIN):
                return self.last_score(board), None
            else:
                return self.greedy_minimizer(MIN, board, depth-1, heuristic_fn)[0], None
        return self.minimize_opponents_movement(MAX, board)
