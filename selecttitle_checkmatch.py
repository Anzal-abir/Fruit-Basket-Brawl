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