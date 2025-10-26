

def display_board(board):
    print("\n " *100)
    
    print('   |   |')
    print(' ' + board[7] +  ' | ' + board[8] +  ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] +  ' | ' + board[5] +  ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] +  ' | ' + board[2] +  ' | ' + board[3])
    print('   |   |')


test_board = [''] * 10
display_board(test_board)


def player_input():
    marker = ''
    # keep asking player 1 to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#Tuples unpacking
player1_marker, player2_marker = player_input()
print(f'Player 1 is {player1_marker} and Player 2 is {player2_marker}')

def place_marker(board, marker, position):
    board[position] = marker
# place_marker(test_board, '$', 8)
display_board(test_board)   

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
print(win_check(test_board, 'X'))
def choose_first():
    import random
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
print(choose_first())

def space_check(board, position):
    return board[position] == ' '
print(space_check(test_board, 1))

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False # it means there is at least one empty space
    return True # IT means board is full
print(full_board_check(test_board))

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

print(player_choice(test_board))

def replay():
    choice = input("Do you want to play again? Enter Yes or No: ")
    return choice.lower().startswith('y')   
print(replay())

# While loop to keep the game running
while True:
     # Reset the board

     # set everything up (board, whos first, choose markers X,O)
     the_board = [' '] * 10
     player1_marker, player2_marker = player_input()               
     turn = choose_first()
     print(turn + ' will go first.')   
     play_game = input('Are you ready to play? Enter Yes or No. ')
     if play_game.lower()[0] == 'y':
         game_on = True
     else:
         game_on = False

     while game_on:
         if turn == 'Player 1':
             #show the board
             display_board(the_board)
             #choose a position
             position =player_choice(the_board)
             #place the marker on the position
             place_marker(the_board, player1_marker, position)


             if win_check(the_board, player1_marker):
                 display_board(the_board)
                 print('Congratulations! Player 1 has won the game!')
                 game_on = False


             else:
                 if full_board_check(the_board):               
                     display_board(the_board)
                     print('The game is a draw!')
                     break
                 else: 
                     turn = 'Player 2'
         else:
             display_board(the_board)      
             position = player_choice(the_board)           
             place_marker(the_board, player2_marker, position)
             if win_check(the_board, player2_marker):
                 display_board(the_board)      

                 print('Congratulations! Player 2 has won the game!')
                 game_on = False
             else:
                 if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                 else:
                        turn = 'Player 1'   
         if not replay():
            break

                    