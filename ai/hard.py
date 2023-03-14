import random

enemy = 2
piece = 1


def hard(rows, moves, symbol):
    global enemy, piece
    piece = symbol
    if symbol == 2:
        enemy = 1
    row_1 = rows[0]
    row_2 = rows[1]
    row_3 = rows[2]

    '''
    A bit more advanced of an AI but still relatively easy
    This AI will check if it has 2 in a row first
    If it doesn't find any it the checks if the player has 2 in a row
    If it still doesn't find anything it makes a random move
    '''

    # Checks if the AI has 2 in a row and can win
    if check(rows, symbol):
        # If it doesn't it checks if the player has 2 in a row and can win
        if check(rows, enemy):
            '''
             If it doesn't detect any potential wins it does a random move
             Eventually I may make the AI make actual moves rather than random ones but im too stupid to think of how rn
             '''

            # On AI's first move it takes 2,2 if not taken otherwise it takes a corner
            if moves == 2:
                if row_2[1] == 0:
                    row_2[1] = 2
                    print("AI placed at 2,2")
                    return
                while True:
                    move = random.randrange(1, 3, 1)
                    spot = random.randrange(1,3,1)
                    if move == 1:
                        if spot == 1 and row_1[0] == 0:
                            row_1[0] = piece
                            print("AI placed at 1,1")
                            return
                        elif spot == 2 and row_1[2] == 0:
                            row_1[2] = piece
                            print("AI placed at 1,3")
                            return
                    elif move == 2:
                        if spot == 1 and row_3[0] == 0:
                            row_3[0] = piece
                            print("AI placed at 3,1")
                            return
                        elif spot == 2 and row_3[2] == 0:
                            row_3[2] = piece
                            print("AI placed at 3,3")
                            return

            # If it doesn't detect any potential wins it does a random move
            while True:
                move = [random.randrange(1, 4, 1), random.randrange(1, 4, 1)]
                if move[0] == 1 and row_1[move[1] - 1] == 0:
                    row_1[move[1] - 1] = piece
                    print("AI placed at " + str(move[0]) + "," + str(move[1]))
                    return
                elif move[0] == 2 and row_2[move[1] - 1] == 0:
                    row_2[move[1] - 1] = piece
                    print("AI placed at " + str(move[0]) + "," + str(move[1]))
                    return
                elif move[0] == 3 and row_3[move[1] - 1] == 0:
                    row_3[move[1] - 1] = piece
                    print("AI placed at " + str(move[0]) + "," + str(move[1]))
                    return


def check(rows, symbol):
    rowNum = 1
    for row in rows:
        # Checks if there are 2 x's in a row, if there are it places its piece in the open space
        rowX = row.count(symbol)
        if rowX == 2:
            for x in range(3):
                if row[x] == 0:
                    row[x] = piece
                    print("AI placed at " + str(rowNum) + "," + str(x + 1))
                    return False
        rowNum += 1
    # Check Vertically
    rowNum = 1
    for x in range(3):
        rowX = 0
        for row in rows:
            if row[x] == symbol:
                rowX += 1
        if rowX == 2:
            for row in rows:
                if row[x] == 0:
                    row[x] = piece
                    print("AI placed at " + str(rowNum) + "," + str(x + 1))
                    return False
        rowNum += 1
    # Check Diagonally
    # Check downwards slope
    rowX = 0
    for x in range(3):
        if rows[x][x] == symbol:
            rowX += 1
    if rowX == 2:
        for x in range(3):
            if rows[x][x] == 0:
                rows[x][x] = piece
                print("AI placed at " + str(x + 1) + "," + str(x + 1))
                return False
    # Check upwards slope
    rowX = 0
    rowNum = 0
    for x in range(2, -1, -1):
        if rows[rowNum][x] == symbol:
            rowX += 1
        rowNum += 1
    rowNum = 0
    if rowX == 2:
        for x in range(2, -1, -1):
            if rows[rowNum][x] == 0:
                rows[rowNum][x] = piece
                print("AI placed at " + str(rowNum + 1) + "," + str(x + 1))
                return False
            rowNum += 1
    return True
