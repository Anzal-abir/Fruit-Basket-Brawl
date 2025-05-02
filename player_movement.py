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