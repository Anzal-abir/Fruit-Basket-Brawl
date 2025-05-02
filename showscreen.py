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