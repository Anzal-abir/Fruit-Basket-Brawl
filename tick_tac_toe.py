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
