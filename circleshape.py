import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        return distance <= self.radius + other_circle.radius