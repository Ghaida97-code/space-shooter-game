import pygame
from constants import *
from player import Player
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from game_objects import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids, updatable_group)
    Shot.containers = (updatable_group, drawable_group, shots_group)
    AsteroidField.containers = (updatable_group,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    try:
        while True:
            dt = clock.tick(60) / 1000 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            for asteroid in asteroids:
                for shot in shots_group:
                    if asteroid.collisions(shot):
                        asteroid.split()
                        shot.kill()
            
            updatable_group.update(dt)   
            screen.fill("black")
            drawable_group.draw(screen)
            
            for sprite in updatable_group:
                if hasattr(sprite, "draw"):  
                    sprite.draw(screen)

            for asteroid in asteroids:
                if player.collisions(asteroid):
                    print("Game over!")
                    sys.exit()
            
            pygame.display.flip()
    except Exception as e:
         print(f"Error occurred: {e}")
         import traceback
         traceback.print_exc()     


if __name__ == "__main__":
    main()