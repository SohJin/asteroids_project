from circleshape import *
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * (dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        first_position = self.velocity.rotate(random_angle)
        second_position = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_asteroid_first.velocity = first_position * 1.2
        spawn_asteroid_second.velocity = second_position * 1.2