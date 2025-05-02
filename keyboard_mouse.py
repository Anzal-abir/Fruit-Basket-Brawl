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