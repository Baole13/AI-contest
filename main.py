import pygame
from environment import Tetris
from agent import Agent
from video_writer import VideoWriter
from environment import WIDTH, HEIGHT, TILE_SIZE
from environment import COLORS


pygame.init()
screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
agent = Agent()
game = Tetris()
vw = VideoWriter("tetris_gameplay.mp4")

def draw_grid(screen, grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = COLORS[grid[y][x]]
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def run_game():
    done = False
    clock = pygame.time.Clock()
    state = game.get_state()

    while not done:
        screen.fill((0, 0, 0))
        draw_grid(screen, game.grid)
        action = agent.choose_action(state)
        state, score, done = game.step(action)
        vw.add(pygame.surfarray.array3d(screen))
        pygame.display.flip()
        clock.tick(50)

    vw.save()
    pygame.quit()

if __name__ == "__main__":
    run_game()
