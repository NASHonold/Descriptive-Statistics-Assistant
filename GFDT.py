
import valid

def title_block():
    print('''
============ Grouped Frequency Distribution ============
Follow the prompts below. 

Enter some or all of your dataset and hit enter to save.
Seperate data points with a comma or space.
The number of spaces or commas is not discriminate.

When all data is entered for that data set enter \'d\' for 
done and the program will continue to your next prompt. 

At any point you can type \'q\' to quit and return to 
main menu

    ''')

def get_class_widths():
    class_width_prompt = 'What is the width of the classes?: '
    number_of_classes_prompt = 'How many classes are there?: '
    starting_class_prompt = 'What is the very first lower class boundary?: '

    class_width = valid.get_int_selection(class_width_prompt)
    if class_width == False:
        return False
    print()
    number_of_classes = valid.get_int_selection(number_of_classes_prompt)
    if number_of_classes == False:
        return False
    print()
    starting_class_value = valid.get_int_selection(starting_class_prompt)
    if starting_class_value == False:
        return False

    class_list = []

    for x in range(number_of_classes):
        class_list.append(starting_class_value + (class_width / 2))
        starting_class_value = starting_class_value + class_width + 1

    
    return class_list

'''
======================= get_values ========================
This will take in the frequency values for the dataset 
and will only promt the user the the number of times equal to 
the number of classes. 
'''
def get_values(class_list):
    value_list = []
    value_num = len(class_list)
    counter = 0
    print('Type in the frequency values below. You will be '
    ,'prompted {} times for your {} classes.'.format(value_num, value_num))
    for counter in range(value_num):
        user_input = valid.get_float_selection('What is the frequency for class {}?: '.format(counter +1))
        if user_input != False:
            value_list.append(user_input)
        
        else:
            return False
            
    return value_list

'''
==================== get_estimates_xbar() ===================
This will take in both the value list and the class list and 
and return the xbar 
'''
def get_estimated_xbar(value_list, class_list):
    multi_list = []
    for x in range(len(value_list)):
        multi_list.append(value_list[x] * class_list[x])

    multi_list_sum = sum(multi_list)
    frequency_sum = sum(value_list)
    return multi_list_sum / frequency_sum

'''
===================== main_loop() =====================
Main_loop prompts the user for inputs, calculates xbar, 
and will contine until the user inputs a q for quit 
'''
def main_loop():
    title_block()
    while True:
        class_widths = get_class_widths()
        if class_widths == False:
            break
        values = get_values(class_widths)
        if values == False:
            break
        xbar = get_estimated_xbar(values, class_widths)
        print('----------------------------------------------------')
        print('Your Values: ')
        print(*values, ', ')
        print('Your class midpoint values:')
        print(*class_widths, ', ')
        print('Your estimated xbar is : ' + str(xbar))
        print('----------------------------------------------------')


