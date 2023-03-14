import random


def easy(rows, symbol):
    row_1 = rows[0]
    row_2 = rows[1]
    row_3 = rows[2]
    # Extremely simple AI since it only makes random moves
    while True:
        move = [random.randrange(1, 4, 1), random.randrange(1, 4, 1)]
        if move[0] == 1 and row_1[move[1] - 1] == 0:
            row_1[move[1] - 1] = symbol
            print("AI placed at " + str(move[0]) + "," + str(move[1]))
            return
        elif move[0] == 2 and row_2[move[1] - 1] == 0:
            row_2[move[1] - 1] = symbol
            print("AI placed at " + str(move[0]) + "," + str(move[1]))
            return
        elif move[0] == 3 and row_3[move[1] - 1] == 0:
            row_3[move[1] - 1] = symbol
            print("AI placed at " + str(move[0]) + "," + str(move[1]))
            return
