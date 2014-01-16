row = (184, 234, 286, 344, 399, 453, 507, 561, 616)
column = (81, 132, 187, 240, 292, 356, 405, 463, 516)

def virtual2board():
    """transform the virtual pos(like (3, 2)) to board filed"""
    v_2_b = {}
    for x in range(1, 9):
        for y in range(1, 9):
            v_2_b[(x, y)] = {}
            v_2_b[(x, y)]['column'] = (column[x-1], column[x])
            v_2_b[(x, y)]['row']    = (row[y-1], row[y])
            v_2_b[(x, y)]['center'] = ((sum(v_2_b[(x, y)]['row']) / 2.0),
                                       (sum(v_2_b[(x, y)]['column']) / 2.0))
    
    return v_2_b          

def board2virtual(board_pos):
    """transform the board pos(like (185.2, 131.8)) to a virtual pos"""
    x = board_pos[1]
    y = board_pos[0]
    v_x = 0
    v_y = 0
    
    for i in range(9):
        if x > column[i]:
            pass
        else:
            v_x = i
            break
        
    for i in range(9):
        if y > row[i]:
            pass
        else:
            v_y = i
            break
    
    if v_x * v_y != 0:
        return (v_x, v_y)
    
    else:
        return False              