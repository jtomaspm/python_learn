import pygame
import os
pygame.font.init()                                              # initialise fonts
pygame.mixer.init()                                             # initialise sounds

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")                       #define title for window

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#FONTS
HEALT_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FRAMES_PER_SECOND = 60
VELOCITY = 5
BULLET_VELOCITY = 10
MAX_BULLETS = 5
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#EVENTS
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#Assets
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('D:/jtoma/Documents/code/pyhon/first_game/Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('D:/jtoma/Documents/code/pyhon/first_game/Assets', 'spaceship_red.png'))
SPACE = pygame.image.load(os.path.join('D:/jtoma/Documents/code/pyhon/first_game/Assets', 'space.png'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('D:/jtoma/Documents/code/pyhon/first_game/Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('D:/jtoma/Documents/code/pyhon/first_game/Assets', 'Gun+Silencer.mp3'))

#recise images
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

#rotate images
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_healt, yellow_healt):
    WIN.fill(WHITE)                                             #paint background white
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_healt_text = HEALT_FONT.render("Health: " + str(red_healt), 1 , WHITE)
    WIN.blit(red_healt_text, (WIDTH - red_healt_text.get_width() - 10, 10))
    yellow_healt_text = HEALT_FONT.render("Health: " + str(yellow_healt), 1 , WHITE)
    WIN.blit(yellow_healt_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))                      #draw surfaces
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):  
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: #LEFT
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY < BORDER.x - yellow.width: #RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: #UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY < HEIGHT - yellow.height - 5: #DOWN
        yellow.y += VELOCITY
        
def red_handle_movement(keys_pressed, red):  
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width: #LEFT
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY < WIDTH - red.width: #RIGHT
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0: #UP
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY < HEIGHT - red.height - 5: #DOWN
        red.y += VELOCITY

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_healt = 10
    yellow_healt = 10

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FRAMES_PER_SECOND)
        for event in pygame.event.get():                       #get all events and run through them
            if event.type == pygame.QUIT:                      #event(pygame.QUIT) click the "x" button 
                run = False
                pygame.quit()

            #fire bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10 , 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10 , 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_healt -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_healt -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""
        if red_healt <= 0:
            winner_text = "Yellow Wins!"

        if yellow_healt <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
            

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_healt, yellow_healt)

    main()

if __name__ == "__main__":
    main()