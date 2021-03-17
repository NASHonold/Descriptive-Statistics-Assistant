
def q_check(string_input):
    if string_input.lower() == 'q':
        return True
    else:
        return False


def input_check_int(string_input):
    try:
        string_input = int(string_input)
        return True
    except ValueError:
        return False


def input_check_float(string_input):
    try:
        string_input = float(string_input)
        return True
    except ValueError:
        return False

def get_int_selection(prompt):
    while True:
        user_input = input(prompt)
        if input_check_int(user_input):
            user_input = int(user_input)
            return user_input
        elif q_check(user_input):
            return False
        else:
            print('That is not an option. Only input an integer or \'q\' for quit',
            '\nTry again\n')

def get_float_selection(prompt):
    while True:
        user_input = input(prompt)
        if input_check_float(user_input):
            user_input = float(user_input)
            return user_input
        elif q_check(user_input):
            return False
        else:
            print('\nThat is not an option. Only input a number or \'q\' for quit',
            '\nTry again...\n')


'''
==================== process_data_string() ===========================
This method takes a string composed of numbers from the user 
input and parses it and appends the data to a string. THis method
uses spaces and to dilineate between numbers in the string. 
'''
def process_data_string(string, sort = True):
    if string == False:
        return False
    good_list = ['0','1','2','3','4','5','6','7','8','9','.']
    a_list = []
    final_index = len(string)
    working_string = ''
    
    for index in range(final_index):
        if string[index] in good_list:
            working_string += string[index]
        if string[index] not in good_list or index == (final_index - 1):
            if len(working_string) == 1:
                if working_string == '.':
                    working_string = ''
            if len(working_string) > 0:
                a_list.append(float(working_string))
                working_string = ''
    if sort == True:
        a_list.sort()
    return a_list

'''
====================  String get_data_set() ========================
This takes the user input and either returns the string of user data
for processing or returns Boolean value False which starts a chain
reaction to break the main while loop. 
'''            
def get_data_set():
    run = True
    string = ''
    while run:
        data_set = input('Copy and paste or enter data set here: ')
        string += data_set
        
        if data_set.lower() == 'd':
            run = False
        string += ' '
        if data_set == 'q':
            run = False
            return False
    return string