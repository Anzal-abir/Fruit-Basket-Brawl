#Maliha Binte Mohsin Moumita 22301552
#Anzal Ahmed Abir 22301277
#Tasnim Sultana 22301594
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
from math import sin, cos, pi
paused = False

#camera vars and game vars
camera_pos = [0, 500, 500]
fovY = 120
GRID_LENGTH = 600

#fruit list
FRUITS = ['apple', 'orange', 'guava', 'pomegranate']
FRUIT_COLORS = {
    'apple': (1, 0, 0),
    'orange': (1, 0.5, 0),
    'guava': (0.7, 1.0, 0.6),
    'pomegranate': (0.7, 0, 0.2)
}

# # Player variables
# player_positions = [[-200, -200], [200, -200]]  # [ [x1, y1], [x2, y2] ]
# player_radius = 30  # For collision
# player_speed = 20
# player_selected_block = [None, None]  # Which block each player is on

GRID_ROWS = 3
GRID_COLS = 3
TILE_SIZE = 150
TILE_MARGIN = 100

fruit_grid = []
revealed = []
matched = []
removed = []
selected = []
scores = [0, 0]
current_player = 0
start_time = 0
game_over = False
timer_limit = 120  # seconds
block_colors=[]
matched_time=[]


#initial game state 
game_state = "initial_reveal"    
reveal_start_time = 0

#dynamically platform grid
PLATFORM_GRID_SIZE = 20
platform_colors = []

def setup_platform_colors():
    global platform_colors
    platform_colors = []
    for row in range(PLATFORM_GRID_SIZE):
        for col in range(PLATFORM_GRID_SIZE):
            pastel_colors = [
                (1.0, 0.773, 0.827),  # pastel pink
                (1.0, 0.976, 0.768),  # pastel yellow
                (0.8, 1.0, 0.8),      # pastel green
                (0.8, 0.9, 1.0),      # pastel blue
            ]
            color = random.choice(pastel_colors)
            platform_colors.append(color)

def draw_platform_grid():
    cell_size = (2 * GRID_LENGTH) / PLATFORM_GRID_SIZE
    start_x = -GRID_LENGTH
    start_y = -GRID_LENGTH
    z = -TILE_SIZE//2 - 10
    idx = 0
    for row in range(PLATFORM_GRID_SIZE):
        for col in range(PLATFORM_GRID_SIZE):
            glColor3f(*platform_colors[idx])
            x0 = start_x + col * cell_size
            y0 = start_y + row * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            glBegin(GL_QUADS)
            glVertex3f(x0, y0, z)
            glVertex3f(x1, y0, z)
            glVertex3f(x1, y1, z)
            glVertex3f(x0, y1, z)
            glEnd()
            idx += 1

#drawing the four fruits
def draw_apple():
    glColor3f(*FRUIT_COLORS['apple'])
    quad = gluNewQuadric()
    gluSphere(quad, 18,16,16)
    glColor3f(0.4, 0.2, 0)
    glPushMatrix()
    glTranslatef(0, 0, 22)
    gluCylinder(gluNewQuadric(), 2, 1, 7, 10, 10)
    glPopMatrix()

def draw_orange():
    glColor3f(*FRUIT_COLORS['orange'])
    quad = gluNewQuadric()
    gluSphere(quad, 18,16,16)
    glColor3f(0.8, 0.7, 0.2)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    quad = gluNewQuadric()
    gluSphere(quad, 3,10,10)
    glPopMatrix()

def draw_guava():
    glColor3f(*FRUIT_COLORS['guava'])
    quad = gluNewQuadric()
    gluSphere(quad, 17,16,16)
    
    glColor3f(1.0, 0.7, 0.8)
    glPushMatrix()
    glTranslatef(0, 0, 5)
    quad = gluNewQuadric()
    gluSphere(quad, 8,12,12)
    glPopMatrix()
    
    glColor3f(0.5, 0.8, 0.3)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    gluCylinder(gluNewQuadric(), 2, 1, 7, 10, 10)
    glPopMatrix()


def draw_pomegranate():
    glColor3f(*FRUIT_COLORS['pomegranate'])
    quad = gluNewQuadric()
    gluSphere(quad, 16,16,16)
    glColor3f(1, 0.2, 0.4)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    glutSolidCone(4, 8, 10, 10)
    base_radius = 4
    height = 8
    slices = 12
    tip = (0, 0, height)
    glBegin(GL_LINES)
    for i in range(slices):
        angle1 = 2 * pi * i / slices
        angle2 = 2 * pi * (i+1) / slices
        x1 = base_radius * cos(angle1)
        y1 = base_radius * sin(angle1)
        z1 = 0
        
        glVertex3f(x1, y1, z1)
        glVertex3f(*tip)
        
        x2 = base_radius * cos(angle2)
        y2 = base_radius * sin(angle2)
        glVertex3f(x1, y1, z1)
        glVertex3f(x2, y2, z1)
    glEnd()
    glPopMatrix()

def draw_fruit(fruit_type):
    if fruit_type == 'apple':
        draw_apple()
    elif fruit_type == 'orange':
        draw_orange()
    elif fruit_type == 'guava':
        draw_guava()
    elif fruit_type == 'pomegranate':
        draw_pomegranate()

# def draw_players():
#     # Player 1: rectangle
#     glPushMatrix()
#     glColor3f(0.2, 0.6, 1.0)
#     # glTranslatef(player_positions[0][0], player_positions[0][1], 0)
#     glScalef(1.2, 1.2, 1)
#     # glutSolidCube(player_radius)
#     glPopMatrix()

#     # Player 2: circle (sphere)
#     glPushMatrix()
#     glColor3f(1.0, 0.4, 0.4)
#     # glTranslatef(player_positions[1][0], player_positions[1][1], 0)
#     # glutSolidSphere(player_radius/2, 20, 20)
#     glPopMatrix()

#drawing the baskets
basket_fruits = [[], []]  # 2 indices for 2 players

def draw_basket(x, y, z, fruits):
    
    glColor3f(0.5, 0.3, 0.11)  
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glBegin(GL_QUADS)
    glVertex3f(-40, -20, 0)
    glVertex3f(40, -20, 0)
    glVertex3f(40, 20, 0)
    glVertex3f(-40, 20, 0)
    glEnd()
    
    glBegin(GL_QUADS)
    
    glVertex3f(-40, -20, 0)
    glVertex3f(-40, -20, 30)
    glVertex3f(-40, 20, 30)
    glVertex3f(-40, 20, 0)
    
    glVertex3f(40, -20, 0)
    glVertex3f(40, -20, 30)
    glVertex3f(40, 20, 30)
    glVertex3f(40, 20, 0)
    
    glVertex3f(-40, 20, 0)
    glVertex3f(-40, 20, 30)
    glVertex3f(40, 20, 30)
    glVertex3f(40, 20, 0)
    
    glVertex3f(-40, -20, 0)
    glVertex3f(-40, -20, 30)
    glVertex3f(40, -20, 30)
    glVertex3f(40, -20, 0)
    glEnd()
    

    handle_color = (0.55, 0.35, 0.22)  

    
    side_w = 4
    side_h = 30
    side_z0 = 30
    side_z1 = side_z0 + side_h
    side_y = 18  

    # Left Handle 
    glColor3f(*handle_color)
    glBegin(GL_QUADS)
    glVertex3f(-40, side_y - side_w//2, side_z0)
    glVertex3f(-40, side_y + side_w//2, side_z0)
    glVertex3f(-40, side_y + side_w//2, side_z1)
    glVertex3f(-40, side_y - side_w//2, side_z1)
    glEnd()

    # Right Handle
    glBegin(GL_QUADS)
    glVertex3f(40, side_y - side_w//2, side_z0)
    glVertex3f(40, side_y + side_w//2, side_z0)
    glVertex3f(40, side_y + side_w//2, side_z1)
    glVertex3f(40, side_y - side_w//2, side_z1)
    glEnd()

    # Top Bridge 
    bridge_len = 80 
    bridge_w = 4
    bridge_z = side_z1
    glBegin(GL_QUADS)
    glVertex3f(-40, side_y - bridge_w//2, bridge_z)
    glVertex3f(40, side_y - bridge_w//2, bridge_z)
    glVertex3f(40, side_y + bridge_w//2, bridge_z)
    glVertex3f(-40, side_y + bridge_w//2, bridge_z)
    glEnd()


    # Fruit inside basket
    for i, fruit in enumerate(fruits):
        glPushMatrix()
        glTranslatef(-25 + (i%4)*16, -5 + (i//4)*18, 35)
        draw_fruit(fruit)
        glPopMatrix()
    glPopMatrix()

# def move_player(player_idx, dx, dy):
#     # Compute new position
#     new_x = player_positions[player_idx][0] + dx
#     new_y = player_positions[player_idx][1] + dy

#     # Platform bounds
#     min_xy = -GRID_LENGTH + player_radius
#     max_xy = GRID_LENGTH - player_radius

#     # Clamp to platform
#     new_x = max(min_xy, min(max_xy, new_x))
#     new_y = max(min_xy, min(max_xy, new_y))

#     # Collision check with other player
#     other_idx = 1 - player_idx
#     ox, oy = player_positions[other_idx]
#     dist_sq = (new_x - ox)**2 + (new_y - oy)**2
#     min_dist = player_radius * 1.5
#     if dist_sq < min_dist**2:
#         return  # Block move if colliding

#     # Move allowed
#     player_positions[player_idx][0] = new_x
#     player_positions[player_idx][1] = new_y

#     update_player_block_selection()

# def keyboardListener(key, x, y):
#     global ttt_mode, game_over, paused 
    

#     # Player 1: WASD
#     if key == b'w':
#         move_player(0, 0, player_speed)
#     elif key == b's':
#         move_player(0, 0, -player_speed)
#     elif key == b'a':
#         move_player(0, -player_speed, 0)
#     elif key == b'd':
#         move_player(0, player_speed, 0)

#     # Player 2: Arrow keys (handled in specialKeyListener)
#     # (see below)
#     if player_selected_block[0] is not None:
#         select_tile(player_selected_block[0])
#     # ... (rest of your existing code unchanged)
#     glutPostRedisplay()

    # if key in [b'q', b'Q']:
    #     paused = not paused
    #     glutPostRedisplay()
    #     return

# def specialKeyListener(key, x, y):
#     # Player 2: Arrow keys
#     if key == GLUT_KEY_UP:
#         move_player(1, 0, player_speed)
#     elif key == GLUT_KEY_DOWN:
#         move_player(1, 0, -player_speed)
#     elif key == GLUT_KEY_LEFT:
#         move_player(1, -player_speed, 0)
#     elif key == GLUT_KEY_RIGHT:
#         move_player(1, player_speed, 0)
#     # ... (rest of your camera code)
#     glutPostRedisplay()

# def update_player_block_selection():
#     for p in range(2):
#         px, py = player_positions[p]
#         selected = None
#         for row in range(GRID_ROWS):
#             for col in range(GRID_COLS):
#                 idx = row * GRID_COLS + col
#                 x = (col - GRID_COLS/2 + 0.5) * (TILE_SIZE + TILE_MARGIN)
#                 y = (row - GRID_ROWS/2 + 0.5) * (TILE_SIZE + TILE_MARGIN)
#                 # Check if player is over the block
#                 if abs(px - x) < TILE_SIZE/2 and abs(py - y) < TILE_SIZE/2:
#                     selected = idx
#         player_selected_block[p] = selected


# Tic Tac Toe cheat mode
ttt_grid = [0] * 9  
ttt_turn = 1        
ttt_winner = 0     
ttt_cheatcode_given = False
ttt_cheatcode_used = False
ttt_mode = False

def setup_ttt():
    global ttt_grid, ttt_turn, ttt_winner, ttt_cheatcode_given, ttt_cheatcode_used
    ttt_grid[:] = [0]*9
    ttt_turn = 1
    ttt_winner = 0
    ttt_cheatcode_given = False
    ttt_cheatcode_used = False

def draw_ttt():
    base_x = 590
    base_y = 200
    cell = 85
    glColor3f(1,1,1)
    glLineWidth(3)
    for i in range(1,3):
        glBegin(GL_LINES)
        glVertex3f(base_x + i*cell, base_y, 0)
        glVertex3f(base_x + i*cell, base_y + 3*cell, 0)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(base_x, base_y + i*cell, 0)
        glVertex3f(base_x + 3*cell, base_y + i*cell, 0)
        glEnd()
    for idx in range(9):
        row = idx // 3
        col = idx % 3
        display_number = row * 3 + col + 1
        cx = base_x + col*cell + cell//2
        cy = base_y + row*cell + cell//2
        if ttt_grid[idx] == 1:
            glColor3f(1,0.2,0.2)
            glLineWidth(2)
            glBegin(GL_LINES)
            glVertex3f(cx-12, cy-12, 0)
            glVertex3f(cx+12, cy+12, 0)
            glVertex3f(cx-12, cy+12, 0)
            glVertex3f(cx+12, cy-12, 0)
            glEnd()
        elif ttt_grid[idx] == 2:
            glColor3f(0.2,0.6,1)
            for a in range(0,360,30):
                theta1 = a * pi / 180
                theta2 = (a+30) * pi / 180
                glBegin(GL_LINES)
                glVertex3f(cx + 14 * cos(theta1), cy + 14 * sin(theta1), 0)
                glVertex3f(cx + 14 * cos(theta2), cy + 14 * sin(theta2), 0)
                glEnd()
        glColor3f(0.8,0.8,0.8)
        glRasterPos2f(cx-7, cy-7)
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(str(idx+1)))
    if ttt_winner == 0:
        draw_text(base_x-450, base_y + 200, f"Tic Tac Toe: {'X' if ttt_turn==1 else 'O'}'s turn")
    elif ttt_winner == 3:
        draw_text(base_x-450, base_y + 200, "Tic Tac Toe: Draw!")
    else:
        draw_text(base_x-450, base_y + 200, f"Tic Tac Toe: {'X' if ttt_winner==1 else 'O'} wins!")
        if not ttt_cheatcode_given:
            draw_text(base_x, base_y + 120, "Winner gets a cheatcode! (Press K in fruit mode)")
        else:
            draw_text(base_x+150, base_y + 120, "Cheatcode used!")

def ttt_check_win():
    g = ttt_grid
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if g[w[0]]==g[w[1]]==g[w[2]]!=0:
            return g[w[0]]
    if all(cell != 0 for cell in g):
        return 3  # Draw
    return 0

def ttt_handle_key(idx):
    global ttt_turn, ttt_winner, ttt_cheatcode_given
    if ttt_winner != 0 or ttt_grid[idx]!=0:
        return
    ttt_grid[idx] = ttt_turn
    ttt_winner = ttt_check_win()
    if ttt_winner == 0:
        ttt_turn = 2 if ttt_turn==1 else 1
    glutPostRedisplay()

def use_cheatcode():
    global ttt_cheatcode_given, ttt_cheatcode_used, scores, ttt_winner
    if ttt_winner in [1,2] and not ttt_cheatcode_given and not ttt_cheatcode_used:
        scores[ttt_winner - 1] += 1  # ttt_winner is 1 or 2, so index is 0 or 1
        ttt_cheatcode_given = True
        ttt_cheatcode_used = True

#Setting up the game
def setup_fruits():
    global fruit_grid, revealed, matched, removed, selected, scores, current_player, game_over, start_time
    global game_state, reveal_start_time, basket_fruits, matched_time
    global block_colors
    total_tiles = GRID_ROWS * GRID_COLS
    fruit_types = (FRUITS * ((total_tiles // len(FRUITS)) + 1))[:total_tiles // 2]
    fruit_types = fruit_types * 2
    matched_time = [None] * (GRID_ROWS * GRID_COLS)
    if len(fruit_types) < total_tiles:
        fruit_types.append(random.choice(FRUITS))
    random.shuffle(fruit_types)
    block_colors = []
    for _ in range(GRID_ROWS * GRID_COLS):
        
        base = [random.uniform(1,0) for _ in range(3)]
        pastel = [0.6 * c + 0.4 * 1.0 for c in base]
        block_colors.append(tuple(pastel))
    fruit_grid[:] = [fruit_types[i] for i in range(total_tiles)]
    revealed[:] = [True] * total_tiles   # we reveal at the start
    matched[:] = [False] * total_tiles
    removed[:] = [False] * total_tiles
    selected.clear()
    scores[:] = [0, 0]
    basket_fruits[0].clear()
    basket_fruits[1].clear()
    current_player = 0
    game_over = False
    start_time = time.time()
    game_state = "initial_reveal"
    reveal_start_time = time.time()
    setup_platform_colors()
    setup_ttt()

def draw_gradient_cube(size, base_color): #pastel gradient coloured cubes    
    s = size / 2
    vertices = [
        [-s, -s, -s],
        [ s, -s, -s],
        [ s,  s, -s],
        [-s,  s, -s],
        [-s, -s,  s],
        [ s, -s,  s],
        [ s,  s,  s],
        [-s,  s,  s],
    ]
    #defining 6 faces of the cube
    faces = [
        [0, 1, 2, 3], # back
        [4, 5, 6, 7], # front
        [0, 1, 5, 4], # bottom
        [2, 3, 7, 6], # top
        [1, 2, 6, 5], # right
        [0, 3, 7, 4], # left
    ]
    #random pastel colour
    pastel = lambda c: 0.5 + 0.5 * c
    r, g, b = base_color
    vertex_colors = [
        (pastel(r), pastel(g), pastel(b)),
        (pastel(r*0.9), pastel(g*0.9), pastel(b*1.2)),
        (pastel(r*1.2), pastel(g*1.2), pastel(b*0.9)),
        (pastel(r*1.1), pastel(g*0.8), pastel(b*1.1)),
        (pastel(r*0.8), pastel(g*1.1), pastel(b*1.1)),
        (pastel(r*1.1), pastel(g*1.1), pastel(b*0.8)),
        (pastel(r*0.9), pastel(g*1.2), pastel(b*1.2)),
        (pastel(r*1.2), pastel(g*0.9), pastel(b*1.1)),
    ]
    for face in faces:
        glBegin(GL_QUADS)
        for vi in face:
            glColor3f(*vertex_colors[vi])
            glVertex3f(*vertices[vi])
        glEnd()



def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            idx = row * GRID_COLS + (GRID_COLS - 1 - col)

            if removed[idx]:
                continue
            x = (col - GRID_COLS/2 + 0.5) * (TILE_SIZE + TILE_MARGIN)
            y = (row - GRID_ROWS/2 + 0.5) * (TILE_SIZE + TILE_MARGIN)
            glPushMatrix()
            glTranslatef(x, y, 0)
            if matched[idx]:
                draw_gradient_cube(TILE_SIZE, (0.2, 0.8, 0.2))
            elif idx in selected:
                draw_gradient_cube(TILE_SIZE, (1, 1, 0))
            else:
                color = block_colors[idx] #random gradient pastel
                draw_gradient_cube(TILE_SIZE, color)


            if revealed[idx] or matched[idx]:
                glTranslatef(0, 0, TILE_SIZE/2 + 10)
                draw_fruit(fruit_grid[idx])

            
            glColor3f(1, 1, 1)
            glRasterPos3f(0, 0, TILE_SIZE/2 + 35)
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(str(idx+1)))
            glPopMatrix()

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def setupCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    x, y, z = camera_pos
    gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

def select_tile(idx):
    global selected, revealed, matched, removed, current_player, scores, game_over
    if matched[idx] or revealed[idx] or removed[idx]:
        return
    if idx in selected:
        return
    if len(selected) < 2:
        selected.append(idx)
        revealed[idx] = True
        glutPostRedisplay()
    if len(selected) == 2:
        glutTimerFunc(1000, check_match, 0)

def check_match(value):
    global selected, revealed, matched, removed, current_player, scores, game_over, basket_fruits
    if len(selected) < 2:
        return
    i1, i2 = selected
    if fruit_grid[i1] == fruit_grid[i2]:
        matched[i1] = True
        matched[i2] = True
        
        matched_time[i1] = time.time()
        matched_time[i2] = time.time()
        scores[current_player] += 1
        
    else:
        revealed[i1] = False
        revealed[i2] = False
        current_player = (current_player + 1) % 2
    selected.clear()
    if all(matched):
        game_over = True
    glutPostRedisplay()

def tile_from_mouse(x, y):
    wx = (x / 1000.0) * GRID_COLS
    wy = ((800 - y) / 800.0) * GRID_ROWS
    col = int(wx)
    row = int(wy)
    idx = row * GRID_COLS + col
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        return idx
    return None

def keyboardListener(key, x, y):
    global ttt_mode, game_over, paused 
    if key == b't':
        ttt_mode = not ttt_mode
        glutPostRedisplay()
        return
    if ttt_mode:
        if key in [b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9']:
            idx = int(key.decode()) - 1
            if 0 <= idx < 9:
                ttt_handle_key(idx)
        return
    if game_over:
        if key == b'r':
            setup_fruits()
        return
    if key == b'r':
        setup_fruits()
    if key == b'c':
        global camera_pos
        camera_pos = [0, 500, 500] if camera_pos != [0, 500, 500] else [0, 0, 100]
        glutPostRedisplay()
    if key == b'k':
        use_cheatcode()
    if key in [b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9']:
        idx = int(key.decode()) - 1
        if idx < GRID_ROWS * GRID_COLS:
            select_tile(idx)
    if key in [b'q', b'Q']: #Exit logic (not entirely working)
        paused = not paused
        glutPostRedisplay()
        return

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global camera_pos
    x, y, z = camera_pos
    if key == GLUT_KEY_LEFT:
        x -= 50
    elif key == GLUT_KEY_RIGHT:
        x += 50
    elif key == GLUT_KEY_UP:
        z += 50
    elif key == GLUT_KEY_DOWN:
        z -= 50
    camera_pos[:] = [x, y, z]
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    if ttt_mode:
        return
    if game_over:
        return
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        idx = tile_from_mouse(x, y)
        if idx is not None:
            select_tile(idx)
    glutPostRedisplay()

def idle():
    global game_over, game_state, revealed, reveal_start_time, paused, matched, removed, matched_time, basket_fruits, fruit_grid, current_player
    
    if game_state == "initial_reveal":
        if time.time() - reveal_start_time > 2.0: #the tiles are revealed for 2 secs as a hint in the beginning of the game
            revealed[:] = [False] * (GRID_ROWS * GRID_COLS)
            game_state = "playing"
    if paused: 
        return 
    if not game_over and time.time() - start_time > timer_limit:
        game_over = True

    now = time.time()
    for idx in range(GRID_ROWS * GRID_COLS):
        if matched[idx] and not removed[idx] and matched_time[idx] is not None:
            if now - matched_time[idx] > 1.0:  # Show green when matched for 1 second
                removed[idx] = True
                basket_fruits[current_player].append(fruit_grid[idx])
        
    glutPostRedisplay()

def get_game_result_message(): #message is shown when player wins
    max_points = 5
    p1 = scores[0]
    p2 = scores[1]
    if p1 == 2 and p2 == 2:
        return "Draw!"
    elif p1 > max_points // 2:
        return "Player 1 wins!"
    elif p2 > max_points // 2:
        return "Player 2 wins!"
    else:
        return "Draw!"

def showScreen():
    global paused 
    # draw_players()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)
    setupCamera()
    draw_platform_grid()
    draw_grid()

    # drawing the baskets for both players
    draw_basket(-350, 400, 0, basket_fruits[0])
    draw_text(90, 60, "Player 2 Basket")
    draw_basket(350, 400, 0, basket_fruits[1])
    draw_text(780, 60, "Player 1 Basket")
    draw_ttt()
    # User Interface
    if ttt_mode:
        draw_text(10, 770, "Tic Tac Toe Mode (T to toggle, 1-9 to play, K for cheat)")
    else:
        draw_text(10, 770, f"Fruit Matching Mode (T to toggle, 1-9 to play, K for cheat)")
        draw_text(10, 740, f"Player {current_player+1}'s turn")
        draw_text(10, 710, f"Scores: P1={scores[0]}  P2={scores[1]}")
    if game_over:
        result_message = get_game_result_message()
        draw_text(400, 400, f"Game Over! {result_message}", GLUT_BITMAP_TIMES_ROMAN_24)
        draw_text(400, 370, "Press R to restart.", GLUT_BITMAP_HELVETICA_18)
    if paused:
        draw_text(420, 650, "PAUSED", GLUT_BITMAP_TIMES_ROMAN_24)
    
    if not game_over:
        # Calculate remaining time
        time_left = max(0, int(timer_limit - (time.time() - start_time)))
        mins, secs = divmod(time_left, 60)
        timer_str = f"Time Left: {mins:02d}:{secs:02d}" #time display mm:ss
        draw_text(800, 770, timer_str, GLUT_BITMAP_HELVETICA_18)
        if game_over and time_left == 0:
            draw_text(400, 430, "Time's up!", GLUT_BITMAP_TIMES_ROMAN_24)


    glutSwapBuffers()

def main():
    setup_fruits()
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Fruit Basket Brawl")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()
