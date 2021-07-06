import pygame, math, random
from settings import *

pygame.mixer.init()

background = pygame.image.load("grass.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
shoot_sound = pygame.mixer.Sound("Grenade+1.mp3")
hurt_sound = pygame.mixer.Sound("classic_hurt.mp3")        
hurt_player_sound = pygame.mixer.Sound("gg.wav")        
 

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    hit_list = collision_test(rect, tiles)
    collisio_tolerance = 10
    for tile in hit_list:
        if movement[0] > 0 and abs(rect.right - tile.rect.left) < collisio_tolerance:
            rect.right = tile.rect.left
            collision_types['right'] = True
        elif movement[0] < 0 and abs(rect.left - tile.rect.right) < collisio_tolerance:
            rect.left = tile.rect.right
            collision_types['left'] = True
    
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0 and abs(rect.bottom - tile.rect.top) < collisio_tolerance:
            rect.bottom = tile.rect.top
            collision_types['top'] = True
        elif movement[1] < 0 and abs(rect.top - tile.rect.bottom) < collisio_tolerance:
            rect.top = tile.rect.bottom
            collision_types['bottom'] = True
    print(collision_types)



#Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, des_x, des_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0001.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0002.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0003.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0004.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0005.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0006.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0007.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0008.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0009.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0010.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0011.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0012.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0013.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0014.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0015.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0016.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0017.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0018.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0019.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0020.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0021.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0022.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0023.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0024.png'), (23,30)))
        self.sprites.append(pygame.transform.scale(pygame.image.load('firespritesheet/fireB0025.png'), (23,30)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        self.speed = BULLET_BASE_SPEED
        self.des_x = des_x
        self.des_y = des_y
        self.distance = math.sqrt((self.des_x-self.rect.centerx)**2 + (self.des_y-self.rect.centery)**2)
        self.time = self.distance / self.speed 
        self.movement_vector = ((self.des_x-self.rect.centerx)//self.time, (self.des_y-self.rect.centery)//self.time)
        
    
    def update(self):
        #Animation
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        self.image.set_colorkey(BLACK)
        
        # Movement
        if self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            bullet_group.remove(self)
        nx, ny = self.rect.center
        ax, ay = self.movement_vector
        self.rect.center = (nx + ax, ny + ay)



#Player
class Player(pygame.sprite.Sprite):
    def __init__(self, colisions):
        super().__init__()
        self.image = pygame.image.load("Daco_5744159.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT - 100)
        self.hp = PLAYER_BASE_MAX_HP
        self.speed = PLAYER_BASE_SPEED
        self.colisions = colisions
       

    def hadle_movement(self, key_pressed):
        #move
        
        if key_pressed[pygame.K_a] and self.rect.left - self.speed > 0: #LEFT
            self.rect.left -= self.speed
            move(self.rect, [-1,0], self.colisions)
        if key_pressed[pygame.K_d] and self.rect.right + self.speed < WIDTH: #RIGHT
            self.rect.left += self.speed
            move(self.rect, [1,0], self.colisions)
        if key_pressed[pygame.K_w] and self.rect.top - self.speed > 0: #UP
            self.rect.top -= self.speed
            move(self.rect, [0,-1], self.colisions)
        if key_pressed[pygame.K_s] and self.rect.bottom + self.speed < HEIGHT: #LEFT
            self.rect.top += self.speed
            move(self.rect, [0,1], self.colisions)


    def shoot(self, des_x, des_y):
        if len(bullet_group) < 2:
            shoot_sound.play()
            new_bullet = Bullet(self, des_x, des_y)
            bullet_group.add(new_bullet)

    

class Hp_bar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface([player.hp * 50 + 10, 10 + 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.center = (WIDTH//2, 50)
    
    def update(self):
        self.image = pygame.Surface([player.hp * 50, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, 50)


    
class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("box.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 200)



#Bullets
bullet_group = pygame.sprite.Group()

#Box
box = Box()
box_group = pygame.sprite.Group()
box_group.add(box)

#Player
player_group = pygame.sprite.Group()
player = Player(box_group)
player_group.add(player)
hp_bar = Hp_bar(player)
hp_bar_group = pygame.sprite.Group()
hp_bar_group.add(hp_bar)


class Enemy(pygame.sprite.Sprite):
    def __init__(self,player , pos_x, pos_y, hp, color, speed=3):
        super().__init__()
        self.image = pygame.image.load("demon.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.hp = hp
        self.speed = speed
        self.des_x = player.rect.centerx
        self.des_y = player.rect.centery
        self.distance = math.sqrt((self.des_x-self.rect.centerx)**2 + (self.des_y-self.rect.centery)**2)  
        self.time = self.distance / self.speed 
        self.movement_vector = ((self.des_x-self.rect.centerx)/self.time, (self.des_y-self.rect.centery)/self.time)
        self.sex = random.randrange(2)

    def update(self):
        if self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            enemy_group.remove(self)
        
        self.des_x = player.rect.centerx
        self.des_y = player.rect.centery
        self.distance = math.sqrt((self.des_x-self.rect.centerx)**2 + (self.des_y-self.rect.centery)**2)  
        self.time = self.distance / self.speed 
        self.movement_vector = ((self.des_x-self.rect.centerx)/self.time, (self.des_y-self.rect.centery)/self.time)
        nx, ny = self.rect.center
        ax, ay = self.movement_vector
        self.rect.center = (nx + ax, ny + ay)
        move(self.rect, [ax, ay], box_group)


#Enemies
enemy_group = pygame.sprite.Group()

def draw_sprites(SCREEN):
    
    SCREEN.blit(background, (0,0))
    #Update
    bullet_group.update()
    enemy_group.update()
    player_group.update()
    hp_bar_group.update()
    #Draw
    bullet_group.draw(SCREEN)
    player_group.draw(SCREEN)
    enemy_group.draw(SCREEN)
    box_group.draw(SCREEN)
    hp_bar_group.draw(SCREEN)

def check_colisions():
    for bullet in bullet_group:
        for box_elem in box_group:    
            if bullet.rect.colliderect(box_elem):
                bullet_group.remove(bullet)
            
        for enemy in enemy_group:
            if bullet.rect.colliderect(enemy):
                bullet_group.remove(bullet)
                hurt_sound.play()
                if enemy.hp == 1:
                    enemy_group.remove(enemy)
                else:
                    enemy.hp -= 1
        

    for enemy in enemy_group:
        move(enemy.rect,enemy.movement_vector, enemy_group)
        for player in player_group:
            if player.rect.colliderect(enemy):
                hurt_player_sound.play()
                if(player.hp>1):
                    player.hp -= 1
                    enemy_group.remove(enemy)
                else:
                    player.hp = PLAYER_BASE_MAX_HP
                    return True

    return False



def generate_level(current_level):
    if len(enemy_group) == 0:
        for i in range(current_level):
            ex = random.randrange(0,1080)
            ey = random.randrange(0,720)
            while abs(ex - player.rect.centerx) < 200 and abs(ey - player.rect.centery) < 200:
                ex = random.randrange(0,1080)
                ey = random.randrange(0,720)
            new_enemy = Enemy(player, ex, ey, 2, RED)
            enemy_group.add(new_enemy)
        current_level += 1
    return current_level