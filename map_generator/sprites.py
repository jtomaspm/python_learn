import pygame
from settings import *


class Tile_Spot(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x*width, pos_y*height + TOP_BORDER_HEIGHT)
        self.path = ""

    def fill(self, selector):
        self.image = pygame.transform.scale(selector.tile,(self.width, self.height))
        self.path = selector.path
    
    def paste(self, selector):
        new_image = pygame.transform.scale(selector.tile,(self.width, self.height))
        self.image.blit(new_image,(0,0))
        self.path = selector.path



#BUTTONS

class Tile_Selector(pygame.sprite.Sprite):
    def __init__(self, number, image_file, pos_x, pos_y):
        super().__init__()
        self.number = number
        self.image = pygame.Surface([TILE_SELECTOR_SIZE, TILE_SELECTOR_SIZE])
        self.image.fill(BACKGROUND)
        self.path = image_file
        self.tile = pygame.transform.scale(pygame.image.load(image_file),(64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.image.blit(self.tile, (5, 5))
        self.selected = False;

    def unselect(self):
        self.selected = False
        self.image.fill(BACKGROUND)
        self.image.blit(self.tile, (5, 5))
        

    def select(self):
        self.selected = True
        self.image.fill(YELLOW)
        self.image.blit(self.tile, (5, 5))

    def rotate(self):
        self.tile = pygame.transform.rotate(self.tile, 90)
        self.image.fill(YELLOW)
        self.image.blit(self.tile, (5, 5))
        
class Save_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,TOP_BORDER_HEIGHT))
        self.image.fill(BLUE)
        self.text = OPTIONS_FONT.render("Save", 1, WHITE)
        self.image.blit(self.text,(25,7))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

class Update_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,TOP_BORDER_HEIGHT))
        self.image.fill(BLUE)
        self.text = OPTIONS_FONT.render("Update", 1, WHITE)
        self.image.blit(self.text,(15,7))
        self.rect = self.image.get_rect()
        self.rect.topleft = (130,0)
        

class Rotate_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,TOP_BORDER_HEIGHT))
        self.image.fill(BLUE)
        self.text = OPTIONS_FONT.render("Rotate", 1, WHITE)
        self.image.blit(self.text,(20,7))
        self.rect = self.image.get_rect()
        self.rect.topleft = (260,0)

class Paste_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,TOP_BORDER_HEIGHT))
        self.image.fill(BLUE)
        self.text = OPTIONS_FONT.render("Paste", 1, WHITE)
        self.image.blit(self.text,(23,7))
        self.rect = self.image.get_rect()
        self.rect.topleft = (390,0)
        self.ative = False

    def toggle_ative(self):
        self.ative = not self.ative
        if self.ative:
            self.image.fill(GREEN)
            self.image.blit(self.text,(23,7))
        else:
            self.image.fill(BLUE)
            self.image.blit(self.text,(23,7))
            
        