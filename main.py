# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the following .py
# modules into the current file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 60
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidable = pygame.sprite.Group()
    shotable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroidable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shotable)
    
    danger_zone = AsteroidField()
    poor_soul = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        for each in drawable:    
            each.draw(screen)
        for each in updatable:    
            each.update(dt)
        for each in asteroidable:
            if poor_soul.collision_check(each):
                print("Game over!")
                return   
            for every in shotable:
                if each.collision_check(every):
                    each.split()
                    every.kill()
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
