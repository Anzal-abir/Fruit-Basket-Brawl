for idx in range(GRID_ROWS * GRID_COLS):
        if matched[idx] and not removed[idx] and matched_time[idx] is not None:
            if now - matched_time[idx] > 1.0:  # Show green when matched for 1 second
                removed[idx] = True
                basket_fruits[current_player].append(fruit_grid[idx])
        
    glutPostRedisplay()