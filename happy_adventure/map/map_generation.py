import numpy as np

def random_walk(matrix, initial_position, max_tunnel_lenght):
    valid_directions_dict = {
        "top" : (0, -1),
        "down" : (0, 1),
        "left" : (-1, 0),
        "right" : (1, 0)
    }

    tunnel_lenght = np.random.randint(1,max_tunnel_lenght)
    is_valid_coor = lambda pos_X, matrix_dim_X : True if pos_X >=0 and pos_X < matrix_dim_X else False
    is_valid_position = lambda pos, matrix_dim : True if all([is_valid_coor(posX,dimX) for posX,dimX in zip(pos,matrix_dim)]) else False
    get_new_position = lambda initial_position, increment : [posX+incrementX for posX,incrementX in zip(initial_position, increment)]
    get_valid_directions = lambda  initial_position, matrix_dim, valid_directions_dict : {key:value for key,value in valid_directions_dict.items() 
                                                                       if is_valid_position(get_new_position(initial_position, value), matrix_dim)}

    valid_directions = get_valid_directions(initial_position, matrix.shape, valid_directions_dict)
    selected_dir = np.random.choice(list(valid_directions))
    select_dir_pos = valid_directions[selected_dir]
    corr_pos = initial_position 

    for cont in range(tunnel_lenght):
        corr_pos = get_new_position(corr_pos, select_dir_pos)
        if is_valid_position(corr_pos, matrix.shape):
            matrix[corr_pos[0]][corr_pos[1]] = 1
        else:
            break
    
    print(corr_pos, selected_dir, tunnel_lenght)
    return corr_pos


def generate_map(dimention, num_tunnels, max_tunnel_lenght):
    matrix = np.zeros(dimention, dtype = object)
    corr_pos = (0,0)
    for cont_tunnel in range(num_tunnels):
        corr_pos = random_walk(matrix, corr_pos, max_tunnel_lenght)
    
    return matrix


def set_block_type(posX, posY, matrix):
    dict_count = {
        "grass"  : 1,
        "water"  : 1
    }

    jump_array = [-1,1,0]
    for jump_x in jump_array:
        for jump_y in jump_array:
            new_posX = posX + jump_x
            new_posY = posY + jump_y
            if is_valid_pos(new_posX, new_posY, matrix.shape):
                block_type = matrix[new_posX][new_posY]
                if block_type:
                    dict_count[block_type] = dict_count[block_type] + 1
    
    sum_houses = sum(dict_count.values())
    p = [cont/sum_houses for cont in dict_count.values()]
    matrix[posX][posY] = np.random.choice(["grass","water"], p = p)


def generate_map_2(posX, posY, matrix):
    jump_array = [-1,1,0]
    for jump_x in jump_array:
        for jump_y in jump_array:
            new_posX = posX + jump_x
            new_posY = posY + jump_y
            matrix_shape = matrix.shape
            if is_valid_pos(new_posX, new_posY, matrix_shape):
                if not matrix[new_posX][new_posY]:
                    set_block_type(new_posX, new_posY, matrix)
                    set_matrix(new_posX, new_posY, matrix)