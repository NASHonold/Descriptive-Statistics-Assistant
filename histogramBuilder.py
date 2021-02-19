import valid



# sample data set
'''
125.0, 254.0, 119.0, 186.0, 185.0, 139.0, 186.0, 204.0, 166.0, 
 170.0, 203.0, 170.0, 177.0, 190.0, 139.0, 189.0, 165.0, 192.0, 156.0, 
 151.0, 141.0, 114.0, 185.0, 153.0, 176.0, 286.0, 143.0, 219.0, 196.0, 
 162.0
'''
def title_block():
    print('''
================= Histogram Builder =================
This will allow you to inout a data set and tweak
the class width and starting point of your 
histogram after calculating the standard class width 
and starting point based on common convention.
This will also report on the frequency of the class
that was created as well as its relative frequency. 

Enter some or all of your dataset and hit enter to save.
Seperate data points with a comma or space
The number of spaces or commas is not discriminate.

When all data is entered for that dataset enter \'d\'  
on an empty line when done and the program will continue 
to your next prompt. 

At any point you can type \'q\' to quit and return to 
main menu 
=====================================================

    ''')


def get_range(list):
    max_value = list[0]
    min_value = list[0]
    for index in list:
        if min_value >= index:
            min_value = index
        if max_value <= index:
            max_value = index

    range = max_value - min_value
    
    return range, min_value, max_value


def get_class_width(range, class_num):
    return format(range / class_num,'.6f')

def create_class_boundry_list(graph_start,class_width, number):
    boundaries = []
    boundaries.append(graph_start)
    for i in range(number):
        var = boundaries[-1] + class_width
        boundaries.append(var)
    return boundaries

def build_graph(sorted_list, boundary_list):
    sorted_list.sort()
    number = len(boundary_list) - 1
    master_list = []
    print('The Data for your Histogram by class:')
    for i in range(number):
        sublist = []
        for x in sorted_list:
            if x >= boundary_list[i] and x < boundary_list[i+1]:
                sublist.append(x)
            if x > boundary_list[i+1]:
                break
        master_list.append(sublist)
        print('For the class {} to {}'.format(boundary_list[i],boundary_list[i+1] ))
        print('Frequency is {}'.format(len(sublist)))
        relative_freq = len(sublist)/len(sorted_list)
        relative_freq = format(relative_freq,'.4f')
        print("Relative Frequency for this class is {}".format(relative_freq))
        sublist_string = str(sublist).strip('[]')
        print('Here are the data points in this class:\n ' + sublist_string)
        print('----------------------------------------')
    print(master_list)



def main_loop():
    title_block()
    while True:
        class_num = valid.get_int_selection('How many classes would you like in your data?: ')
        if class_num == False:
            break
        print()
        data_string = valid.get_data_set()
        if data_string == False:
            break
        data_list = valid.process_data_string(data_string)
        total_range, min, max = get_range(data_list)
        class_width = get_class_width(total_range, class_num)
        print('''

=========================
Class width is: {}
Minimum is:     {}
Maximum is:     {}
Range is :      {}
====================================================        
        '''.format(class_width,min,max,total_range))
        print('''
Your calculated class width is {} but sometimes 
you should set this width to a more friendly value.
Either enter a new class width value or confirm the 
above value below.
        '''.format(class_width))
        class_width = valid.get_float_selection('Enter Desired Width Here: ')
        if class_width == False:
            break
        print('''
====================================================
Your calculated starting point for your histogram
is {} but, like your class width, this
value is sometimes changed to be more friendly.
Either enter a new starting value for your
histogram or re enter the above value to 
confirm below.
        '''.format(min))
        graph_start = valid.get_float_selection('Enter your desired starting point: ')
        if graph_start == False:
            break
        print('\n----------------------------------------')
        class_boundaries = create_class_boundry_list(graph_start,class_width,class_num)
        build_graph(data_list,class_boundaries)








