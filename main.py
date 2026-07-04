import prisoners as pr

player1 = pr.Agression()
player2 = pr.Peace()

player1_moves = []
player2_moves = []

for _ in range(100):
    player1_move = player1.move(player2_moves)
    player2_move = player1.move(player1_moves)
    if player1_move > player2_move:
        player1.score += 5
    elif player1_move < player2_move:
        player2.score += 5
    elif player1_move == player2_move and player1_move == 0:
        player1.score += 3
        player2.score += 3
    else:
        player1.score += 1
        player2.score += 1

    player1_moves.append(player1_move)
    player2_moves.append(player2_move)
    
print(player1.score, player2.score)