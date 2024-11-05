from environment import WIDTH, HEIGHT, TILE_SIZE

class Agent:
    def __init__(self):
        pass

    def choose_action(self, state):
        grid, piece, next_piece = state
        best_action = (0, 0)
        best_score = -float('inf')
        
        for rotation in range(4):
            rotated_piece = piece
            for _ in range(rotation):
                rotated_piece = list(zip(*rotated_piece[::-1]))
            for x_position in range(-2, WIDTH):
                score = self.evaluate_position(grid, rotated_piece, (x_position, 0))
                if score > best_score:
                    best_score = score
                    best_action = (x_position, rotation)
        
        return best_action

    def evaluate_position(self, grid, piece, position):
        # Simple scoring function to favor lower placements with fewer holes
        return -sum(sum(row) for row in grid)  # Placeholder scoring
