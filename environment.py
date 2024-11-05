import pygame
import random

WIDTH, HEIGHT = 10, 20
TILE_SIZE = 30
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]]
]
COLORS = [(0, 0, 0), (255, 85, 85), (100, 200, 115), (120, 108, 245), (255, 140, 50), (50, 120, 52)]

class Tetris:
    def __init__(self):
        self.grid = [[0] * WIDTH for _ in range(HEIGHT)]
        self.score = 0
        self.piece = self.new_piece()
        self.next_piece = self.new_piece()

    def new_piece(self):
        return random.choice(SHAPES)

    def valid_position(self, piece, offset):
        offset_x, offset_y = offset
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    if x + offset_x < 0 or x + offset_x >= WIDTH or y + offset_y >= HEIGHT:
                        return False
                    if y + offset_y >= 0 and self.grid[y + offset_y][x + offset_x]:
                        return False
        return True

    def place_piece(self, piece, offset):
        offset_x, offset_y = offset
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell and y + offset_y < HEIGHT:
                    self.grid[y + offset_y][x + offset_x] = cell
        self.clear_lines()

    def clear_lines(self):
        cleared = 0
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared = HEIGHT - len(new_grid)
        self.grid = [[0] * WIDTH for _ in range(cleared)] + new_grid
        self.score += cleared ** 2

    def get_state(self):
        return self.grid, self.piece, self.next_piece

    def reset(self):
        self.__init__()

    def step(self, action):
        x, rotation = action
        piece = self.piece
        for _ in range(rotation):
            piece = list(zip(*piece[::-1]))
        if self.valid_position(piece, (x, 0)):
            self.place_piece(piece, (x, 0))
            self.piece = self.next_piece
            self.next_piece = self.new_piece()
            return self.get_state(), self.score, False
        return self.get_state(), self.score, True  # End if invalid action
