import pygame, sys
from functions import *
from settings import *
from sprites import *

#Get Settings
WIDTH, HEIGHT, TILE_WIDTH, TILE_HEIGHT = validade_input()
DRAW_MAP = generate_bidimentional_array(WIDTH//TILE_WIDTH, HEIGHT//TILE_HEIGHT)
SOLUTION_DIC = {}
TILE_NUMBER_HORIZONTAL = len(DRAW_MAP[0])
TILE_NUMBER_VERTICAL = len(DRAW_MAP)
TILE_SELECTOR_ROWS = 1

#Initiate game
pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT + TILE_SELECTOR_SIZE*TILE_SELECTOR_ROWS*2 + TOP_BORDER_HEIGHT))

def check_change_display_size(change_display_size):
    if change_display_size:
        SCREEN = pygame.display.set_mode((WIDTH,HEIGHT + TILE_SELECTOR_SIZE*TILE_SELECTOR_ROWS*2 + TOP_BORDER_HEIGHT))
    return False

#option buttons
SAVE_BUTTON = Save_Button()
UPDATE_BUTTON = Update_Button()
ROTATE_BUTTON = Rotate_Button()
PASTE_BUTTON = Paste_Button()
OPTION_BUTTON_GROUP = pygame.sprite.Group()
OPTION_BUTTON_GROUP.add(SAVE_BUTTON)
OPTION_BUTTON_GROUP.add(UPDATE_BUTTON)
OPTION_BUTTON_GROUP.add(ROTATE_BUTTON)
OPTION_BUTTON_GROUP.add(PASTE_BUTTON)

#Tile Selectors
TILE_SELECTOR_GROUP = pygame.sprite.Group()
def populate_tile_selector_group():
    global TILE_SELECTOR_ROWS, TILE_SELECTOR_GROUP
    TILE_SELECTOR_GROUP = pygame.sprite.Group()
    TILE_SELECTOR_ROWS = 1
    file_paths = get_file_paths()
    i = 1
    max_size = (WIDTH // TILE_SELECTOR_SIZE)*TILE_SELECTOR_SIZE
    for path in file_paths:
        size = (i-1)*TILE_SELECTOR_SIZE
        if size >= max_size*(TILE_SELECTOR_ROWS):
            TILE_SELECTOR_ROWS += 1
        TILE_SELECTOR_GROUP.add(Tile_Selector(i, path, size - max_size*(TILE_SELECTOR_ROWS-1), HEIGHT + TOP_BORDER_HEIGHT + (TILE_SELECTOR_ROWS-1)*TILE_SELECTOR_SIZE))
        i += 1 

populate_tile_selector_group()

#Tile Spots
TILE_SPOT_GROUP = pygame.sprite.Group()
def generate_tile_spots():
    tile_spots = []
    for x in range(TILE_NUMBER_HORIZONTAL):
        for y in range(TILE_NUMBER_VERTICAL):
            tile_spots.append(Tile_Spot(x, y, TILE_WIDTH, TILE_HEIGHT))
    return tile_spots
def populate_tile_spot_group(tiles):
    global TILE_SPOT_GROUP
    for tile in tiles:
        TILE_SPOT_GROUP.add(tile)
populate_tile_spot_group(generate_tile_spots())

def draw_content():
    SCREEN.fill(BACKGROUND)
    TILE_SELECTOR_GROUP.draw(SCREEN)
    OPTION_BUTTON_GROUP.draw(SCREEN)
    TILE_SPOT_GROUP.draw(SCREEN)

def handle_mouse_colisions():
    global DRAW_MAP, SOLUTION_DIC
    mx, my = pygame.mouse.get_pos()
    #hadle paste
    if PASTE_BUTTON.rect.collidepoint(mx, my):
        PASTE_BUTTON.toggle_ative()
    #handle update
    elif UPDATE_BUTTON.rect.collidepoint(mx, my):
        populate_tile_selector_group()
    #handle rotate
    elif ROTATE_BUTTON.rect.collidepoint(mx, my):
        for selector in TILE_SELECTOR_GROUP:
            if selector.selected:
                selector.rotate()
    #handle save
    elif SAVE_BUTTON.rect.collidepoint(mx, my):
        DRAW_MAP, SOLUTION_DIC = save_map(TILE_SELECTOR_GROUP, TILE_SPOT_GROUP, DRAW_MAP)
    else:    
        #handle tile selectors
        selecting = False
        for ts in TILE_SELECTOR_GROUP:
            if ts.rect.collidepoint(mx, my):
                selecting = True
                selected = ts.selected
                new_selection = ts
        if selecting:
            for ts in TILE_SELECTOR_GROUP:
                ts.unselect()
            if not selected:   
                new_selection.select()
        
        #handle tile spots
        for spot in TILE_SPOT_GROUP:
            if spot.rect.collidepoint(mx, my):
                for selector in TILE_SELECTOR_GROUP:
                    if selector.selected:
                        #hadle paste
                        if PASTE_BUTTON.ative:
                            spot.paste(selector)
                        else:    
                            spot.fill(selector)

def main():
    global TILE_SELECTOR_ROWS
    run = True
    change_display_size = False

    while run:
        change_display_size = check_change_display_size(change_display_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   #left-click
                    handle_mouse_colisions()
                if event.button == 3:   #right-click
                    #erase_tile()
                    pass
        
        draw_content()
        pygame.display.flip()
        clock.tick(FRAMES_PER_SECOND)

    pygame.quit()
    sys.exit()

main()