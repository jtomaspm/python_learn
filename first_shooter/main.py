import pygame, sys
from settings import *
from sprites import *


    

#General Settings
pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))


def main():
    current_level = 1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                player.shoot(mx, my)
        keys_pressed = pygame.key.get_pressed()
        player.hadle_movement(keys_pressed)
        draw_sprites(SCREEN)
        end_game = check_colisions()
        current_level = generate_level(current_level)
        
        if end_game:
            pygame.time.delay(5000)
            run = False
        
        pygame.display.flip()
        clock.tick(FPS)



    pygame.quit()
    sys.exit()

main()