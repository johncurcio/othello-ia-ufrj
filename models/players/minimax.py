class Minimax:
    MIN = -1
    MAX = +1
    def __init__(self, color, start_with=MAX):
        self.color = color
        self.start_with = start_with

    # finge que tu vai mover e pega o tabuleiro que resulta desse movimento
    def simulate_movement(self, move, board, player):
        copy_board = board.get_clone()
        copy_board.play(move, player)
        return copy_board

    def is_max(self, player):
        if self.start_with == Minimax.MAX:
            return self.color == player
        else:
            return self.color != player


    def __call__(self, player, board, depth, heuristic_fn):
        return self.minimax(player, board, depth, heuristic_fn)

    def minimax(self, player, board, depth, heuristic_fn, cut=None):
        (best_score, best_move) = (None, None)
        if depth == 0:
            (best_score, best_move) = (heuristic_fn(player, board), None)
            return (best_score, best_move)

        opponent = board._opponent(player)
        valid_moves_max = board.valid_moves(player)
        if len(valid_moves_max) == 0 :
            if len(board.valid_moves(opponent)) == 0:
                (best_score, best_move) = (heuristic_fn(opponent, board), None)
                return (best_score, best_move)
            else:
                return self.minimax(opponent, board, depth-1, heuristic_fn)[0], None

        # cria uma lista com todos os movimentos possiveis a partir do estado atual do jogo e retorna o de maior heuristica
        best_score = None
        best_move = None
        for possible_move in valid_moves_max:
            modified_board = self.simulate_movement(possible_move, board, player)
            if best_score is None:
                b_score = self.minimax(opponent, modified_board, depth-1, heuristic_fn)[0]
            else:
                b_score = self.minimax(opponent, modified_board, depth-1, heuristic_fn, best_score)[0]
            if b_score is None:
                continue

            if self.is_max(player):
                if best_score is None or best_score < b_score:
                    best_score = b_score
                    best_move = possible_move
                    if cut is not None and best_score >= cut:
                        return (None, None)
            else:
                if best_score is None or best_score > b_score:
                    best_score = b_score
                    best_move = possible_move
                    if cut is not None and best_score <= cut:
                        return (None, None)

        # pega a jogada de valor maximo e retorna isso
        return (best_score, best_move)
