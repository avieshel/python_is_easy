
# global board size settings
ROWS = 6
COLUMNS = 7

# number of chips in row/column/diagonal needed for winning
STREAK_LENGTH = 4 

# global player face settings
PLAYER_ONE = '\u2B2E' # Black vertical ellipse
PLAYER_TWO = '\u2B2F' # White vertical ellipse

# get a representation of the game board according to global size settings
def get_empty_board():
    return  [ [ ' ' for col in range(COLUMNS) ] for row in range(ROWS) ]


def draw_board(board):
    for r in range(ROWS):
        for c in range(COLUMNS):
            print('|',board[r][c],'', end='')
        print('|') # draw the last vertical seperator and a newline
        print('-' * 4 * COLUMNS + '-') # print the horizontal seperator which is '---' (3 dashes per column) and on to close off the line
 

def play(player1, player2, board):
    game_ended = False
    players = [player1, player2]
    moves_count = 0
    while game_ended == False:
        draw_board(board)
        current_player = players[moves_count % 2]
        colum_to_play = get_player_input(current_player, board)
        put_chip_at_column(current_player, colum_to_play,board)
        moves_count += 1 # increment the moves counter to keep track of the game
        game_ended = check_board(board)
    draw_board(board) # draw the winning board
    print('Game Ended')

def is_valid_column(column, board):
    # check the entered value is between 1 and COLUMNS (inclusive)
    if column < 0 or COLUMNS < column: 
        return False
    # check that the column isn't stacked all the way to the top
    if board[0][column] != ' ':
        return False
    return True # in case the move is valid


def get_player_input(player, board):
    column = -1
    done = False
    while not done:
        # prompt user for input and cast to integer
        column_string = input('Player ' + player + '  Select colum to play [1 - ' + str(COLUMNS) +']: ')
        try:
            column = int(column_string)
            column -= 1 # we need to convert user input [1:COLUMNS] =>to array values [0:COLUMNS-1]
            if is_valid_column(column, board) == False:
                print('The column:',column+1,'is invalid or stacked to the top, please try again...')
            else:
                done = True
        except ValueError:
            print('Error: The value:',column_string,'is not an integer value')
    return column # return a valid column input shifted to array index
    
        
def check_board(board):
    for r in range(ROWS):
        for c in range(COLUMNS):
            if check_four_in_column(r,c,board) == True:
                return print('Winner!',STREAK_LENGTH,'in column')
            if check_four_in_row(r,c,board) == True:
                return print('Winner!',STREAK_LENGTH,'in a row')
            if check_four_in_diagonal_bottom_left(r,c,board) == True:
                return print('Winner!',STREAK_LENGTH,'diagonal bottom left to top right')
            if check_four_in_diagonal_top_left(r,c,board) == True:
                return print('Winner!',STREAK_LENGTH,'diagonal top left to bottom right')
    return False # check the whole board, no winner yet


def put_chip_at_column(player, column, board):
    # start at the top row
    row = 0 
    # move down until we reach the bottom row or a non empty space
    while (row < ROWS and board[row][column] == ' '):
        row += 1
    # put the player's chip in board[row-1][column] as the loop will stop the row counter one place after the valid place
    row -= 1
    board[row][column] = player

# return true if there are 4 (winning streak length) chips for the player in a row (to the right) starting at 'row','column'
def check_four_in_row(row, column, board):
    # get the value in the starting cell
    player = board[row][column]
    if player == ' ':
        return False # starting point is empty
    # check for four in a row (left to right)
    for i in range(1,STREAK_LENGTH):
        if column+i >= COLUMNS or board[row][column+i] != player:
            return False #one of the cells to the right is either empty, blocked by other player or out of board limits
    return True # found a winning streak in a row!

# return true if there are 4 (winning streak length) chips for the player stacked in column starting at 'row', 'column'
def check_four_in_column(row, column, board):
    player = board[row][column]
    if player == ' ': 
        return False # starting point is empty
    for i in range(1,STREAK_LENGTH):
        if row+i >= ROWS or board[row+i][column] != player:
            return False #one the the cells below is either empty, blocked by other player or out of board limitss
    return True # found a winnign streak in column!

# return True iff there are 4 (winning streak length) chips for the same player diagonally (top left -> bottom right) [Note: row 0 is top row!]
def check_four_in_diagonal_top_left(row, column, board):
    player = board[row][column]
    if player == ' ':
        return False # starting point is empty
    for i in range(1,STREAK_LENGTH):
        if row+i >= ROWS or column+i >= COLUMNS or board[row+i][column+i] != player:
            return False # one of the cells in the diagonal is either blocked by other player or out of bounds of the board
    return True

# return True iff there are 4 (winning streak length) chips for the same player diagonall (bottom left -> top right) [Note: row 0 is top row!]
def check_four_in_diagonal_bottom_left(row, column, board):
    player = board[row][column]
    if player == ' ':
        return False # starting point is empty
    for i in range(1,STREAK_LENGTH):
        if row-i < 0 or column+i >= COLUMNS or board[row-i][column+i] != player:
            return False # one of the cells in the diagonal is either blocked by other player or out of bounds of the board
    return True

# play the game
play(PLAYER_ONE, PLAYER_TWO, get_empty_board())
