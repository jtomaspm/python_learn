import pygame, os

def generate_bidimentional_array(x, y, val=0):
    array = []
    for i in range(y):
        array.append([val])
        for k in range(x-1):
            array[i].append(val)
    
    return array

def bidimentional_array_insert_value(array, x, y, val):
    array[y][x] = val
    return array


def check_divisor(user_input):
    width = int(user_input[0])
    height = int(user_input[1])
    tile_width = int(user_input[2])
    if len(user_input) > 3:
        tile_height = int(user_input[3])
    else:
        tile_height = tile_width
    if width % tile_width == 0 and height % tile_height == 0:
        return True
    return False

def validade_input():
    
    print("Usage: \nWIDTH HEIGHT (TILE_SIZE | TILE_WIDTH TILE_HEIGHT)\n\n > WIDTH % TILE_WIDTH == 0\n\n > HEIGHT % TILE_HEIGHT == 0")
    user_input = input().split(" ")
    while not check_divisor(user_input):
        user_input = input("invalid, please try again\n").split(" ")
    width = int(user_input[0])
    height = int(user_input[1])
    tile_width = int(user_input[2])
    if len(user_input) > 3:
        tile_height = int(user_input[3])
    else:
        tile_height = tile_width
    return width, height, tile_width, tile_height



def get_file_paths():
    file_names = os.listdir('./tiles')
    file_paths = []
    for file in file_names:
        file_paths.append("tiles/" + str(file))    
    return file_paths


def save_map_to_file(id_map, path_dic):
    map_file = open("map.txt", "w")
    map_file.write("")
    map_file.close()
    map_file = open("map.txt", "a")
    for id in id_map:
        map_file.write(str(id) + "\n")
    map_file.close()

    solution_file = open("solution.txt", "w")
    solution_file.write("")
    solution_file.close()
    solution_file = open("solution.txt", "a")
    
    for solution in path_dic:
        solution_file.write(str(solution) + " " + str(path_dic[solution]) + "\n")
    solution_file.close()

def save_map(TILE_SELECTOR_GROUP, TILE_SPOT_GROUP, DRAW_MAP):
    path_dic = {}
    id_map = DRAW_MAP
    i = 1
    for tile in TILE_SELECTOR_GROUP:
        print(tile.path)
        path_dic[tile.path] = i
        i += 1
    for tile in TILE_SPOT_GROUP:
        if tile.path in path_dic:
            id_map = bidimentional_array_insert_value(id_map, tile.x, tile.y, int(path_dic[tile.path]))
    print(id_map)
    save_map_to_file(id_map, path_dic)
    return id_map, path_dic


