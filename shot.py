from circleshape import *
from constants import SHOT_RADIUS, PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * (dt)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt