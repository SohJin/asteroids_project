# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the following .py
# modules into the current file
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 60
    poor_soul = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        poor_soul.draw(screen)
        poor_soul.update(dt)
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
