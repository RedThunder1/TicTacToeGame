import random


def hard(rows):
    row_1 = rows[0]
    row_2 = rows[1]
    row_3 = rows[2]
    if check(rows, 2):
        if check(rows, 1):
            # If it doesn't detect any potential wins it does a random move
            while True:
                move = [random.randrange(1, 4, 1), random.randrange(1, 4, 1)]
                if move[0] == 1 and row_1[move[1] - 1] == 0:
                    row_1[move[1] - 1] = 2
                    print("AI placed at " + str(move[0]) + "," + str(move[1]))
                    return
                elif move[0] == 2 and row_2[move[1] - 1] == 0:
                    row_2[move[1] - 1] = 2
                    print("AI placed at " + str(move[0]) + "," + str(move[1]))
                    return
                elif move[0] == 3 and row_3[move[1] - 1] == 0:
                    row_3[move[1] - 1] = 2
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
                    row[x] = 2
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
                    row[x] = 2
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
                rows[x][x] = 2
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
                rows[rowNum][x] = 2
                print("AI placed at " + str(rowNum + 1) + "," + str(x + 1))
                return False
            rowNum += 1
    return True
