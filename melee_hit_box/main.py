import pygame, sys
from setting import *

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

def main():
    run = True

    while(run):
        
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False

        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

main()