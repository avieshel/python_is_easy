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
    quit()

# file did exist, close it and continue with options
file_descriptor.close()

# prompt user with options
action = input('Enter "read" if you wish to read the file: ' + notes_file + '\nEnter "delete" if you with to the delete the file: ' + notes_file + '\nEnter "append" if you wish to append another note to the file: ' + notes_file + '\nEnter "edit" if you with to edit a specific line in the file: ' + notes_file + '\n')
#action = input('read / delete / append?')
# use this flag to check that a valid action was acted on
acted_on_action = False

if (action == "read" and acted_on_action == False):
    # mark 'read' action as acted on
    acted_on_action = True
    # open file for reading (we know it exists)
    file_descriptor = open(file = notes_file, mode = 'r')
    # print the file line by line, note we ommit the default \n from the print statement as it's redundant
    lines = file_descriptor.readlines()
    for line in lines:
        print(line, end = '')
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
if (action == 'edit' and acted_on_action == False):
    # mark the 'edit' action as acted on
    acted_on_action = True
    # get the line number from the user as int
    line_to_edit = int(input('Enter the line you would like to edit: '))
    # validate that it's value is between 1 and 1000 (this is a random limit, should limit based on MAX_FILE_ZISE)
    if (1 <= line_to_edit and line_to_edit <= 1000):
        # get the new note from the user
        new_data = input('Enter the new text: ')
        # open the file for writing
        file_descriptor = open(file=notes_file, mode='r')
        # read the current contents of the file
        lines = file_descriptor.readlines()
        # close the file we just read
        file_descriptor.close()
        # edit the line given by the user, consider case when file has 2 lines and the user wants to edit the 5th line (which does not exit)
        if 1 <= line_to_edit and line_to_edit <= len(lines):
            # replace the old data with new data, note line index is +1 than list index, don't forget the newline char
            lines[line_to_edit -1] = new_data + '\n'
            # open the same file for writing
            file_descriptor = open(file=notes_file, mode = 'w')
            # write the edited data
            file_descriptor.writelines(lines)
            # close the file
            file_descriptor.close()
        else:
            print('cannot edit line ' + line_to_edit + ' the file you are trying to edit has ' + str(len(lines)) + 'lines')
    else:
        print('cannot edit line ' + line_to_edit + ' value must be between 1 and 1000')

if (acted_on_action == False):
    print('Entered option',action,'is not a valid option, please choose between "read", "delete" or "append"')


