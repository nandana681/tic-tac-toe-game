board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_win(player):
    win_cond = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_cond)

def tic_tac_toe():
    turn = "X"
    for _ in range(9):
        print_board()
        move = int(input(f"{turn}'s move (0-8): "))
        if board[move] == " ":
            board[move] = turn
            if check_win(turn):
                print_board()
                print(f"{turn} wins!")
                return
            turn = "O" if turn=="X" else "X"
        else:
            print("Spot taken!")
    print_board()
    print("Draw!")

tic_tac_toe()