line_1 =  '         ____'
line_2 =  '        /   |'
line_3 =  '    ___|____|___'
line_4 =  '     |  *  * |'
line_5 =  '      \  <  /      \|/'
line_6 =  '      .>    <.      W'
line_7 =  '    /   *      \---<|'
line_8 =  '   |   *        |   |'
line_9 =  '    \   *      /    |'
line_10 = '.....>       <..... |'

snowman = [line_1,line_2,line_3,line_4,line_5,line_6,line_7,line_8,line_9,line_10]
# draw the snowman according to the player's status
def draw_snowman(wrong_answers_count):
    for index, line in enumerate(snowman):
        if index < len(snowman) - wrong_answers_count:
            print() # print empty line
        else:
            print(line)

def draw_word(word, guessed):
    for letter in word:
        if letter in guessed:
            print('',letter,'', end="")
        else:
            print("__ ", end="")
    print() # add a new line


def clear_screen():
    print(chr(27) + "[2J") 

def get_guess_form_user(guesses):
    valid_input = False
    while not valid_input:
        guess = input('Guess a letter:')
        if guess not in guesses:
            guesses.append(guess)
            valid_input = True
        else:
            print('You have already guessed ',guess)
    return guess
    
def calculate_impact(word, guesses):
    for l in word:
        if l not in guesses:
            return False
    return True

def has_only_letters(word):
    return word.isalpha()

def get_word_from_file():
    words_file = open('words.txt', 'r')
    words_list = words_file.readlines()
    words_file.close() # prevent memory leaks
    import random
    rand = random.randint(1, len(words_list) -1)
    return words_list[rand].strip()


def get_word_from_user():
    clear_screen()
    valid_input = False
    while not valid_input:
        word = input('Enter the word to be guessed by player 2: ')
        valid_input = True # assume input is OK, if any of the checks fail set this to False
        if len(word) < 2:
            print('Word length must be greater than 2')
            valid_input = False
        if len(word) > 10:
            print('Word length must be less than or equal to 10')
            valid_input = False
        if not has_only_letters(word):
            print('Word must have only english letters a-z')
            valid_input = False
    clear_screen()
    return word


def welcome_screen():
    clear_screen()
    print('Welcome to snowman game!\nIn this game you\'ll have to guess a secret word before the snowman image is displayed on screen')
    print('\nYou can either enter a word for another player to guess or have the computer pick a random word for you')
    valid_input = False
    while not valid_input:
        get_random_word  = input('Enter:\n  \'yes\' to get have a computer select a random word\n  \'no\' to manullay enter a word\n(yes / no): ')
        if get_random_word == 'yes' or get_random_word == 'no':
            valid_input = True
        else:
            print('incorrect value', get_random_word,' valid values are: \'yes\' / \'no\' only')
    return get_random_word

def play():
    
    get_random_word = welcome_screen()
    if get_random_word == 'no':
        word = get_word_from_user()
    elif get_random_word == 'yes':
        word = get_word_from_file() 
    else:
        print('Unexpected error, aborting...') # should never happen
        exit(1) # quit the game
    
    game_over = False
    
    max_wrong_answers = len(snowman) # 10 max wrong guesses
    wrong_answers = 0

    guesses = []

    while not game_over:
        # draw the snowman
        draw_snowman(wrong_answers)
        # draw the word guess template
        draw_word(word, guesses)
        # prompt the user for input 
        guess = get_guess_form_user(guesses)
        # calculate the impact
        if guess in word:
            game_over = calculate_impact(word, guesses)
            end_msg = 'Good Job!'
        else:
            wrong_answers +=1
            game_over = wrong_answers >= max_wrong_answers
            end_msg = 'Sorry you lost, the secret was: ' + word
        
        if game_over:
            draw_snowman(wrong_answers)
            draw_word(word, guesses)
            print(end_msg)
        else:
            clear_screen()
play()