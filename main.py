import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock() 
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update in updatable:
            update.update(dt)

        screen.fill((0,0,0))

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000

        
        

if __name__ == "__main__":
    main()
