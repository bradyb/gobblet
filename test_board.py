import board

game = board.Board()
for move in game.available_moves("black"):
    print(move)
