

def get_class_widths():
    class_width = int(input('What is the width of the classes?: '))
    number_of_classes = int(input('How many classes are there?: '))
    starting_class_value = int(input('What is the very first lower class boundary?: '))
    class_list = []
    for x in range(number_of_classes):
        print(starting_class_value)
        class_list.append(starting_class_value + (class_width / 2) )
        starting_class_value = starting_class_value + class_width  + 1
    return class_list

def get_values():
    value_list = []
    print()
    print('Type in the frequency values below. When you have entered all values enter \'d\' for done.')
    while True:
        value = input('What is the value:')
        if value != 'd':
            value_list.append(float(value))
        elif value == 'q':
            return False
            break
        else: 
            return value_list
            break

def get_estimated_xbar(value_list, class_list):
    multi_list = []
    for x in range(len(value_list)):
        multi_list.append(value_list[x] * class_list[x])

    multi_list_sum = sum(multi_list)
    frequency_sum = sum(value_list)
    return multi_list_sum / frequency_sum

while True:
    class_widths = get_class_widths()
    values = get_values()
    if values == False:
        break
    xbar = get_estimated_xbar(values, class_widths)
    print('Your Values: ')
    print(*values, ', ')
    print('Your class midpoint values:')
    print(*class_widths, ', ')
    print('Your estimated xbar is : ' + str(xbar))
    print('=======================================================')



