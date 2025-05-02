def idle():
    global game_over, game_state, revealed, reveal_start_time, paused, matched, removed, matched_time, basket_fruits, fruit_grid, current_player
    
    if game_state == "initial_reveal":
        if time.time() - reveal_start_time > 2.0: #the tiles are revealed for 2 secs as a hint in the beginning of the game
            revealed[:] = [False] * (GRID_ROWS * GRID_COLS)
            game_state = "playing"