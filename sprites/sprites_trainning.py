import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25,25])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("D:/jtoma/Documents/code/pyhon/sprites/Grenade+1.mp3")
    
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 1080
screen_height = 720
FPS = 60
screen = pygame.display.set_mode((screen_width,screen_height))

#get rid of mouse
pygame.mouse.set_visible(False)

#Crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range (20):
    new_target = Target(random.randrange(0, screen_width),random.randrange(0, screen_height))
    target_group.add(new_target)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    
    pygame.display.flip()
    screen.fill((0,0,0))

    target_group.draw(screen)

    crosshair_group.draw(screen)
    crosshair_group.update()
    
    clock.tick(FPS)

pygame.quit()
sys.exit()