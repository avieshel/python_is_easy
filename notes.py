import os


# Prompt the user for notes file to use
notes_file = input('Please enter notes file to use: ')

# Open the file
try:
    file_descriptor = open(file=notes_file, mode='r')
except FileNotFoundError:
    # Prompt the user to enter a note
    note_text = input('Please enter the note you want to keep:\n')

    #create a new file
    file_descriptor = open(file=notes_file, mode = 'w')
    
    # write the note to file
    file_descriptor.write(note_text)
    
    # close the file
    file_descriptor.close()

    # terminate the program
    exit()

# file did exist, close it and continue with options
file_descriptor.close()

# prompt user with options
action = input('Enter "read" if you wish to read the file: ' + notes_file + '\nEnter "delete" if you with to the delete the file: ' + notes_file + '\nEnter "append" if you wish to append another note to the file: ' + notes_file + '\n')
#action = input('read / delete / append?')
# use this flag to check that a valid action was acted on
acted_on_action = False

if (action == "read" and acted_on_action == False):
    # mark 'read' action as acted on
    acted_on_action = True
    # open file for reading (we know it exists)
    file_descriptor = open(file = notes_file, mode = 'r')
    # print the file line by line, note we ommit the default \n from the print statement as it's redundant
    for line in file_descriptor.readlines():
        print(line, end='')
    # close the file
    file_descriptor.close()
if (action == "delete" and acted_on_action == False):
    # mark 'delete' action as acted on
    acted_on_action = True
    # remove the file from the file system
    os.remove(notes_file)
if (action == "append" and acted_on_action == False):
    # mark 'append' action as acted on
    acted_on_action = True
    # get the text we want to append to the file
    note_to_append = input('Please enter the note you want to append to file: '+ notes_file + '\n')
    # add a newline to make the appended note in a new line
    note_to_append = '\n' + note_to_append
    # open the file in append mode
    file_descriptor = open(file=notes_file, mode='a')
    # write the data that will be appended to a new line in the file
    file_descriptor.write(note_to_append)
    # close the file
    file_descriptor.close()
if (acted_on_action == False):
    print('Entered option',action,'is not a valid option, please choose between "read", "delete" or "append"')

