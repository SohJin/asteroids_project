# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# database.py into the current file
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
