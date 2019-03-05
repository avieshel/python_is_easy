import shutil

'''
  Validate the input parameters against what is returned by 'shutil' 
'''
def is_input_valid(rows, cols):
    max_width, max_height = shutil.get_terminal_size()
    input_is_valid = True
    if (rows > max_height):
        print(rows,' parameter is greater than the max height (',max_height,')')
        input_is_valid = False
    if (cols > max_width):
        print(cols, ' parameter is greater than the max width (',max_width,')')
        input_is_valid = False
    return input_is_valid

'''
  Draw a board that looks like:
   | | 
  -----
   | | 
  -----
   | |

   size will be rows * cols
   note: for better looking results rows & cols should be odd numbers
'''
def make_board(rows, cols):
    if is_input_valid(rows, cols) == False:
        return False
    for row in range (rows):
        if row % 2 == 0:
            #this is an even row, we need to draw the columns
            for col in range (cols):
                if col % 2 == 0:
                    print(' ', end='')
                else:
                    print('|', end='')
        else:
            # this is an odd number row, we need to draw the seperator
            for col in range (cols):
                print('-', end='')
        print('') # add the new line at the end of the row

# define parameters:
ROWS = 15
COLUMNS = 15

# run the function
make_board(ROWS, COLUMNS)



