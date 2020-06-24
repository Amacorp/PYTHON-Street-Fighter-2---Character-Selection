def street_fighter_selection(fighters, initial_position, moves):
    cur_pos = [initial_position[0], initial_position[1]]
    selected_fighters = []

    for move in moves:
        if move == "up": 
            cur_pos[0] = 0
        elif move == "down": 
            cur_pos[0] = 1
        elif move == "right":
            cur_pos[1] = (cur_pos[1] + 1) % 6
        elif move == "left":
            cur_pos[1] = (cur_pos[1] - 1) % 6
        selected_fighters.append(fighters[cur_pos[0]][cur_pos[1]])

    return selected_fighters
    
    
    
 OR
 
 
 
 def street_fighter_selection(f, i, m):
    select = []
    vp, hp = 0,0 # For vertical and horizontal position
    for i in m:
        if i == 'right' and hp != 5: hp += 1
        elif i == 'right' and hp == 5: hp = 0
        elif i == 'left' and hp != 0: hp += -1
        elif i == 'left' and hp == 0: hp = 5
        elif i == 'up' and vp != 0: vp += -1
        elif i == 'down' and vp != 1: vp += 1
        select.append(f[vp][hp])
    return select
    
    
    
    
OR



def street_fighter_selection(fighters, initial_position, moves):
    x, y = initial_position
    size_x = len(fighters[0])
    size_y = len(fighters)
    result = []
    for move in moves:
        if move == 'right':
            x = (x + 1) % size_x
        elif move == 'left':
            x = (x - 1) % size_x
        elif move == 'down' and y < (size_y - 1):
            y += 1
        elif move == 'up' and y > 0:
            y -= 1
        result.append(fighters[y][x])
    return result
