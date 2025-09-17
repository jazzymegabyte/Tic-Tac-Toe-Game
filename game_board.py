user_input = int(input("Enter thre num of dimensions of game board:  "))

rows  = user_input
cols = user_input

def game_board(rows, cols):
    for r in range(rows):
        print(" ---" * cols)

        print("|   " * cols +"|")

        print(" ---" * cols)


game_board(rows,cols)

