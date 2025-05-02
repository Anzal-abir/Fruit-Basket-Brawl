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