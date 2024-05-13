def calculate_knight_moves(positions, piece):
    if not positions or piece not in positions:
        return []

    col, row = positions[piece]
    col = ord(col.upper()) - ord('A')
    row = int(row) - 1

    possible_moves = [
        (col + 1, row + 2), (col + 1, row - 2),
        (col - 1, row + 2), (col - 1, row - 2),
        (col + 2, row + 1), (col + 2, row - 1),
        (col - 2, row + 1), (col - 2, row - 1),
    ]

    opponent_positions = {key.lower(): value for key, value in positions.items() if key.lower() != piece.lower()}
    moves = []

    for c, r in possible_moves:
        if 0 <= c < 8 and 0 <= r < 8:
            move = f"{chr(c + ord('A'))}{r + 1}"
            # Simulate the move and check if any opponent's piece can capture the piece in the new position
            simulated_positions = positions.copy()
            simulated_positions[piece] = move
            can_capture = False
            for opponent_piece, opponent_position in opponent_positions.items():
                if opponent_piece == 'knight':
                    continue  # Knights don't capture in this scenario
                if piece_can_capture(simulated_positions, opponent_piece, opponent_position, move):
                    can_capture = True
                    break
            if not can_capture:
                moves.append(move)

    return moves

def calculate_rook_moves(positions, piece):
    if not positions or piece not in positions:
        return []

    col, row = positions[piece]
    col = ord(col.upper()) - ord('A')
    row = int(row) - 1

    moves = []

    for c in range(8):
        if c != col:
            move = f"{chr(c + ord('A'))}{row + 1}"
            if move not in positions.values() and not is_capture(positions, piece, move):
                moves.append(move)

    for r in range(8):
        if r != row:
            move = f"{chr(col + ord('A'))}{r + 1}"
            if move not in positions.values() and not is_capture(positions, piece, move):
                moves.append(move)

    return moves

def calculate_bishop_moves(positions, piece):
    if not positions or piece not in positions:
        return []

    col, row = positions[piece]
    col = ord(col.upper()) - ord('A')
    row = int(row) - 1

    moves = []

    for c in range(8):
        for r in range(8):
            if abs(c - col) == abs(r - row) and (c != col or r != row):
                move = f"{chr(c + ord('A'))}{r + 1}"
                if move not in positions.values() and not is_capture(positions, piece, move):
                    moves.append(move)

    return moves

def calculate_queen_moves(positions, piece):
    if not positions or piece not in positions:
        return []

    rook_moves = calculate_rook_moves(positions, piece)
    bishop_moves = calculate_bishop_moves(positions, piece)

    return rook_moves + bishop_moves

def is_capture(positions, piece, target_position):
    for opponent_piece, opponent_position in positions.items():
        if opponent_piece.lower() != piece.lower() and piece_can_capture(positions, opponent_piece, opponent_position, target_position):
            return True
    return False

def piece_can_capture(positions, capturing_piece, capturing_piece_position, target_position):
    col, row = target_position
    col = ord(col.upper()) - ord('A')
    row = int(row) - 1

    capturing_col = ord(capturing_piece_position[0].upper()) - ord('A')
    capturing_row = int(capturing_piece_position[1]) - 1

    if capturing_piece == 'queen':
        return capturing_col == col or capturing_row == row or \
               abs(capturing_col - col) == abs(capturing_row - row)
    elif capturing_piece == 'rook':
        return capturing_col == col or capturing_row == row
    elif capturing_piece == 'bishop':
        return abs(capturing_col - col) == abs(capturing_row - row)
    elif capturing_piece == 'pawn':
        return ord(capturing_piece_position[0].upper()) == ord(col) + 1 and \
               (int(capturing_piece_position[1]) == row + 1 or int(capturing_piece_position[1]) == row - 1)
    elif capturing_piece == 'knight':
        return abs(capturing_col - col) == 2 and \
               abs(capturing_row - row) == 1 or \
               abs(capturing_col - col) == 1 and \
               abs(capturing_row - row) == 2
    return False

