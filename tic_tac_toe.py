#W02 prove developer - solo code submission
#Tic-Tac-Toe game development
#Author: Emediong Henry Edet

def main():
    print()
    player = next_player("")
    board = create_board()
    while not (winner(board) or draw_game(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Great game! Thanks for playing")


def create_board():
    board = []
    for square in range(16):
        board.append(square + 1)
    return board
 


def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}|{board[7]}")
    print("-+-+-+-+-")
    print(f"{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print("-+-+-+-+-")
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}")
    print()

def draw_game(board):
    for square in range(16):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    choice = int(input(f"{player}'s turn to choose a square (1-16):"))
    board[choice - 1] = player

def next_player(current):
    if current == "" or current == "o":
        print("Great move there!")
        return "x"
    elif current == "x":
        print("Perfect!")
        return "o"

if __name__ == "__main__":
    main()




