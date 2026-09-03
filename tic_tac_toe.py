# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

import os


winning_boards = [((0,0), (0,1), (0,2)),
                    ((1,0), (1,1), (1,2)),
                    ((2,0), (2,1), (2,2)),

                    ((0,0), (1,0), (2,0)),
                    ((0,1), (1,1), (2,1)),
                    ((0,2), (1,2), (2,2)),

                    ((0,0), (1,1), (2,2)),
                    ((0,2), (1,1), (2,0)),                    
                ]

def get_coordinates(turn_count, cur_player, board) -> tuple:
    coordinates = input(f"Turn {turn_count}: Player {cur_player} choose a coordinate 'xy': ")
    while True:
        if coordinates.isdecimal() and len(coordinates) == 2:
            number_coordinate = int(coordinates[0]),int(coordinates[1])
            if number_coordinate[0] in [1,2,3] and number_coordinate[1] in [1,2,3]:
                if board[number_coordinate[1]-1][number_coordinate[0]-1] == None:
                    break
        coordinates = input("That input was invalid, try again (e.g. 23): ")
    return number_coordinate

def choose_player_symbol() -> tuple:     
    player_a = input("Player 1: Presss 'x' or 'o' to choose symbol: ").lower()
    while player_a != 'x' and player_a != 'o':
        player_a = input("Only 'x' or 'o', try again: ").lower()
    if player_a == 'x':
        player_b = 'o'
    else:
        player_b = 'x'
    return player_b, player_a

def display_board(board: list[list[str|None]]):
    def get_symbol(symbol: str|None):
        return " " + symbol if symbol else ' .'
    print('  1 2 3')
    for i, row in enumerate(board): 
        cur_row = str(i+1)
        for symbol in row:
            cur_row += get_symbol(symbol)
        print(cur_row)

def update_board(board: list[list[str|None]], player_input: tuple[int, int], player_symbol: str):
    transformed_input = tuple((player_input[0] - 1, player_input[1] - 1))
    board[transformed_input[1]][transformed_input[0]] = player_symbol

def check_if_won(board_state: list[list[str|None]], symbol_to_check: str) -> bool:

    for winning_board in winning_boards:
        has_won = True

        for x, y in winning_board: #((0,2), (1,1), (2,0))
            if board_state[x][y] != symbol_to_check:
                has_won = False
                break

        if has_won:
            return True
    
    return False


# Tic-tac-toe game
if __name__ == "__main__":

    print("Moin, welcome to TicTacToe")
    player_symbols = choose_player_symbol()
    #player_symbols = ('x','o') #for testing
    print(f"Player 1 is '{player_symbols[0]}' and Player 2 is '{player_symbols[1]}'")

     
    play = True
    
    while play == True:
        # Init game
        board =   [ [None, None, None], 
                    [None, None, None], 
                    [None, None, None]
                    ]
        turn_count = 1
        

        # Clear the Screen
        os.system('cls')

        #Start game
        while turn_count <= 9:
            if turn_count % 2 == 1:
                cur_player = 1
            else :
                cur_player = 2

            display_board(board)

            coordinates = get_coordinates(turn_count, cur_player,board)

            update_board(board,coordinates, player_symbols[cur_player-1])

            if check_if_won(board, player_symbols[cur_player-1] ):
                print(f"Player {cur_player}, you won!")
                break

            turn_count += 1
        
        if turn_count == 10:
            print("It is a draw!")
        
        again = input("Wanna go again? [y/n] : ").lower()
        while again not in ["y", "n"]:
            again =  input("Answer with 'y' or 'n': ").lower()

        play = True if again == "y" else False
    
    print("\nThanks for playing, see you soon!\n")

