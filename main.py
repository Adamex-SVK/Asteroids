import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_SPEED
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
import sys 

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield_object = AsteroidField()



    while 1 == 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for draws in drawable:
            draws.draw(screen)
        
        updatable.update(dt)

        for asteorid in asteroids:
            if CircleShape.collides_with(player_object, asteorid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collides_with(asteroid, shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        clock_object.tick(60)
        dt = (clock_object.tick(60)/1000)
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
