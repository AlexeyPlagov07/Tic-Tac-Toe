board = [['-','-','-'],['-','-','-'],['-','-','-']]
columns = "ABC"
rows = "123"
turn = 0
def show_board(board):
    print(" ", 'ABC')
    for i in range(len(board)):
        print(i+1, ''.join(board[i]))
def user_turn(turn):
    if turn % 2 == 0:
        return "X"
    else:
        return "O"
    
def do_turn(turn):
    user_input = input("Enter coord(A1, B2, etc...): ")
    column = columns.index(user_input[0])
    row = rows.index(user_input[1])
    if board[row][column] == '-':
        board[row][column] = user_turn(turn)
    else:
        do_turn(turn)

def check_row():
    for i in board:
        if ''.join(i) == "XXX" or ''.join(i) == "OOO":
            show_board(board)
            print(f"{user_turn(turn)} won!")
            quit()
    return False


def check_column():
    for i in range(3):
        if board[0][i]+board[1][i]+board[2][i] == "XXX" or board[0][i]+board[1][i]+board[2][i] == "OOO":
            show_board(board)
            print(f"{user_turn(turn)} won!")
            quit()
    return False

def check_diag():
    if board[0][0]+board[1][1]+board[2][2] == "XXX" or board[0][0]+board[1][1]+board[2][2] == "OOO":
        show_board(board)
        print(f"{user_turn(turn)} won!")
        quit()
    elif board[0][2]+board[1][1]+board[2][0] == "XXX" or board[0][2]+board[1][1]+board[2][0] == "OOO":
        show_board(board)
        print(f"{user_turn(turn)} won!")
        quit()
    return False

while turn < 9:
    show_board(board)
    do_turn(turn)
    check_row()
    check_column()
    check_diag()
    turn += 1
print("TIE!!!!")