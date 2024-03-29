from ai import easy, medium, hard

player1 = input("What is player one's name: ").strip().lower()
player2 = input("What is player two's name: ").strip().lower()
moves: int = 1
gCoords = [0, 0]
aiMode1 = None
aiMode2 = None
turn = False

row_1 = [0, 0, 0]
row_2 = [0, 0, 0]
row_3 = [0, 0, 0]
rows = [row_1, row_2, row_3]

while player1 == "":
    player1 = input("Player1 can't be empty: ").lower()

while player2 == "":
    player2 = input("Player2 can't be empty:  ").lower()

if player1 == "easy":
    aiMode1 = "easy ai"
elif player1 == "medium":
    aiMode1 = "medium ai"
elif player1 == "hard":
    aiMode1 = "hard ai"

if player2 == "easy":
    aiMode2 = "easy ai"
elif player2 == "medium":
    aiMode2 = "medium ai"
elif player2 == "hard":
    aiMode2 = "hard ai"


def print_board():
    board: str = ""
    for row in rows:
        for num in row:
            if num == 0:
                board = board + " - "
            elif num == 1:
                board = board + " X "
            elif num == 2:
                board = board + " O "
        board = board + "\n"
    print(board)


print_board()


def check_input(Input):
    if Input == "stop":
        exit()
    gotcoord = False
    if ',' not in Input and len(Input) < 3:
        print("Input improperly formatted it should be formatted as x,y please try again!")
        return False
    for char in Input:
        if char.isdigit():
            if int(char) > 3 or int(char) < 1:
                print("Numbers can't be bigger than 3 or less than one! Please try again.")
                return False
            elif not gotcoord:
                gCoords[0] = int(char)
                gotcoord = True
            else:
                gCoords[1] = int(char)
    return True


def check_board():
    # Checks horizontally
    for row in rows:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == 1:
                print(player1 + " has won the game!")
                exit()
            if row[0] == 2:
                print(player2 + " has won the game!")
                exit()
    # Checks Vertically
    for i in range(3):
        if row_1[i] != 0:
            if row_1[i] == row_2[i] and row_2[i] == row_3[i]:
                if row_1[i] == 1:
                    print(player1 + " has won the game!")
                    exit()
                if row_1[i] == 2:
                    print(player2 + " has won the game!")
                    exit()
    # Checks diagonally
    if row_1[0] != 0:
        if row_1[0] == row_2[1] and row_2[1] == row_3[2]:
            if row_1[0] == 1:
                print(player1 + " has won the game!")
                exit()
            if row_1[0] == 2:
                print(player2 + " has won the game!")
                exit()
    if row_1[2] != 0:
        if row_1[2] == row_2[1] and row_2[1] == row_3[0]:
            if row_1[2] == 1:
                print(player1 + " has won the game!")
                exit()
            if row_1[2] == 2:
                print(player2 + " has won the game!")
                exit()
    if moves > 9:
        print("It is a draw!")
        exit()


def put_piece(Input, symbol):
    global moves, turn
    if Input[0] == 1 and row_1[Input[1] - 1] == 0:
        row_1[Input[1] - 1] = symbol
        moves += 1
        turn = not turn
        print_board()
    elif Input[0] == 2 and row_2[Input[1] - 1] == 0:
        row_2[Input[1] - 1] = symbol
        moves += 1
        turn = not turn
        print_board()
    elif Input[0] == 3 and row_3[Input[1] - 1] == 0:
        row_3[Input[1] - 1] = symbol
        moves += 1
        turn = not turn
        print_board()
    else:
        print("You cannot place your piece there! Please try again.")
        return


while True:
    # Check if a player has won,  Will only check after 3 moves because a player can't win until then
    if turn:
        # Play against AI
        if aiMode2 is not None:
            print("AI 2's turn")
            if aiMode2 == "easy ai":
                easy.easy(rows, 2)
                moves += 1
                turn = not turn

                print_board()
            elif aiMode2 == "medium ai":
                medium.medium(rows, 2)
                moves += 1
                turn = not turn
                print_board()
            elif aiMode2 == "hard ai":
                hard.hard(rows, moves, 2)
                moves += 1
                turn = not turn
                print_board()
        else:
            # player two's turn
            if check_input(input(player2 + ", please type your move: ")):
                put_piece(gCoords, 2)
    else:
        if aiMode1 is not None:
            print("AI 1's turn")
            if aiMode1 == "easy ai":
                easy.easy(rows, 1)
                moves += 1
                turn = not turn

                print_board()
            elif aiMode1 == "medium ai":
                medium.medium(rows, 1)
                moves += 1
                turn = not turn
                print_board()
            elif aiMode1 == "hard ai":
                hard.hard(rows, moves, 1)
                moves += 1
                turn = not turn
                print_board()
        # player one's turn
        else:
            if check_input(input(player1 + ", please type your move: ")):
                put_piece(gCoords, 1)
    check_board()
