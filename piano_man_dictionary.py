piano_man_dict = {}

# Song name
piano_man_dict['name'] = "Piano Man"

# Song writer
piano_man_dict['written_by'] = "Billy Joel"

# The first album the song was featured in
piano_man_dict['album'] = "Piano Man"

# Music Producer
piano_man_dict['producer'] = "Micheal Stewart"

# Music Genre
piano_man_dict['genre'] = "Soft Rock"

# Date integer the song was released
piano_man_dict['released_day'] = 2

# Month integer the song was released
piano_man_dict['released_month'] = 11

# Year integer the song was released
piano_man_dict['relesaed_year'] = 1973

# Relased date string
piano_man_dict['released_date_string'] = "November 2nd, 1973"

# Total song length in seconds
piano_man_dict['length_seconds'] = 5*60 + 40

# Total song length in minutes (note: five minutes and thirty seconds is represented as 5.5 not 5:30)
piano_man_dict['length_min'] = piano_man_dict['length_seconds'] *1.0 / 60

# Wikepedia page URL
piano_man_dict['wikipedia_value'] = "https://en.wikipedia.org/wiki/Piano_Man_(song)"

# Additional background information about the song
piano_man_dict['about'] = "The song is sung from Joel's point-of-view working as a piano player at a bar, reminiscing on his experiences working there and the people that he encounters. \"Piano Man\" is based on Joel's real-life experiences working as a lounge musician in Los Angeles from 1972-73, in an effort to escape his contracted New York-based record company at the time, Family Productions, following the poor commercial performance of the album. Various different characters, including a bartender named John and a real-estate novelist named Paul, are introduced from Joel's perspective as he describes them, and are all based on real-life individuals that he encountered at the bar."

'''
The song full lyrics, formmated as verse_<number> and chorus for easier formatting
The lyrics variable is composed of verses and chorus between each to verses
Note: the values are already formatted with 'newline' (\n) characters to represent
      a traditional song format, not just a long line to text.
'''
piano_man_dict['verse_1'] = "\nIt's nine o'clock on a saturday \nRegular crowd shuffles in \nThere's an old man sittin' next to me \nMakin' love to his tonic and gin \nHe says son can you play me a memory? \nI'm not really sure how it goes \nBut it's sad and it's sweet and \nI knew it complete \nWhen I wore a younger man's clothes\n"
piano_man_dict['chorus'] = "\nLa-la-la de-de da \nLa-la de-de da da-da \nSing us a song you're the piano man \nSing us a song tonight \nWell we're all in the mood for a melody \nAnd you've got us feelin' alright\n"
piano_man_dict['verse_2'] = "\nNow John at the bar is a friend of mine \nHe gets me my drinks for free \nAnd he's quick with a joke or to light up your smoke \nBut there's someplace that he'd rather be \nHe says Bill I believe this is killing me \nAs a smile ran away from his face \nWell I'm sure that I could be a movie star \nIf I could get out of this place\n"
piano_man_dict['verse_3'] = "\nNow Paul is a real estate novelist \nWho never had time for a wife \nAnd he's talkin' with Davy who's still in the navy \nAnd probably will be for life \nAnd the waitress is practicing politics \nAs the businessmen slowly get stoned \nYes they're sharing a drink they call loneliness \nBut it's better than drinkin' alone...\n"
piano_man_dict['verse_4'] = "\nIt's a pretty good crowd for a saturday \nAnd the manager gives me a smile \n'Cause he knows that it's me they've been comin' to see \nTo forget about life for a while \nAnd the piano it sounds like a carnival \nAnd the microphone smells like a beer \nAnd they sit at the bar and put bread in my jar \nAnd say man what are you doin' here?\n"
piano_man_dict['lyrics'] = piano_man_dict['verse_1'] + piano_man_dict['chorus'] + piano_man_dict['verse_2'] + piano_man_dict['chorus'] + piano_man_dict['verse_3'] + piano_man_dict['chorus'] + piano_man_dict['verse_4'] + piano_man_dict['chorus']


# generic print dictionary function
def print_dict(dictionary):
    for key in dictionary:
        print(key," : ", dictionary[key])

# print the piano man song details
print_dict(piano_man_dict)


# check the guess against the dictionary
def guess_my_details(key_guess, value_guess):
    return key_guess in piano_man_dict and piano_man_dict[key_guess] == value_guess

# check wrong key name
assert guess_my_details("song_name", "Piano Man") is False, '"song_name" is NOT a valid key'
# check wrong value
assert guess_my_details("name", "november rain") is False, 'the value of "name" is NOT "november rain"'
# check corrent key & value
assert guess_my_details("name", "Piano Man") is True, 'the value of "name" is "Piano Man" (Capitalized)'
# check invalid arguments
assert guess_my_details(None, None) is False, 'invalid fucntion arguments'

# play the guessing game
def play_guessing_game():
    user_wants_to_play = True
    while (user_wants_to_play):
        key_guess = input('Type in your "key" guess: ')
        value_guess = input('Type in your "value" guess: ')
        if guess_my_details(key_guess, value_guess) == True:
            msg = 'Horray! consider playing the lottery today :D'
        else:
            msg = 'Too bad... you can try again'
        print(msg)

        play_again = input('Do you want to play again? [y/n] ')
        if (play_again == 'n'):
            user_wants_to_play = False

play_guessing_game()