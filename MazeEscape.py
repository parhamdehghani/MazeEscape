id_bot = int(input())
input_visible= []
for _ in range(2):
    grid.append(input().strip())
initial_face = 'RIGHT'
cells = [(0,1),(1,2),(1,0),(2,1)]
def next_move(id_bot,input_visible):
    for i,j in cells:
        if input_visible[i][j] == '-' and i,j == cells[0]:
            initial_face = 'UP'
            return initial_face
            break
        if input_visible[i][j] == '-' and i,j == cells[1]:
            initial_face = 'RIGHT'
            return initial_face 
            break
        if input_visible[i][j] == '-' and i,j == cells[2]:
            initial_face = 'LEFT'
            return initial_face 
            break
        if input_visible[i][j] == '-' and i,j == cells[3]:
            initial_face = 'DOWN'
            return initial_face 
            break
