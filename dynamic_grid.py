from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
from math import sin, cos, pi
paused = False


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