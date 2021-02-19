import math
import quartiles
import valid

            
'''
========================== float gen_mean() =========================
method takes the data list after it has been parsed and calculates 
the mean of the entire data set
'''
def get_mean(data_list):
    list_length = len(data_list)
    list_total = sum(data_list)
    return list_total / list_length

'''
========================== float get_mode() =========================
method takes the data list after it has been parsed and calculates 
the mode of the data set. If there is not a value that occurs more 
than any others it will return 'no mode available
'''
def get_mode(data_list):
    index = 0
    current_mode = 0
    #mode_index = 0
    frequency = 0
    for value in data_list:
        if data_list.count(data_list[index]) > frequency:
            frequency = data_list.count(data_list[index])
            #mode_index = index
            current_mode = data_list[index]
        index += 1
    if frequency == 1:
        return "There is no mode available."
    else:
        return current_mode



'''
========================== float get_median() =========================
method takes the data list after it has been parsed and calculates 
the median of the data set. This works with either a value in the
data set that represents the median or if the median had to be 
calculated from the two center values. 
'''
def get_median(data_list):
    list_length = len(data_list)

    if list_length % 2 == 1:
        median_index = int(list_length/2)
        return data_list[median_index]
    else:
        median_index2 = int(list_length/2)
        median_index1 = median_index2 - 1
        median_value = (data_list[median_index1] + data_list[median_index2]) / 2
        return median_value

'''
========================== get_range() ===========================
using the dataset this will determine the range of the set
'''

def get_range(data_list):
    min = data_list[0]
    max = data_list[-1]
    return (max - min)


'''
========================== sum_of_the_squares() ===================
Method takes the dataset, the mean, and an optional boolean value 
in case an additional print statement is needed for the user. 
*This is specifically if the user must show work for this type of 
problem. 
'''
def sum_of_the_squares(data_list, mean, value=False):
    sum = 0
    for number in data_list:
        num = number - mean
        if value:
            print('------------------------------------')
            print('{} - {} = {}'.format(number,format(mean,'.4f'),format(num,'.4f')))
            print('{} squared is : {}'.format(format(num,'.4f'), format((num**2), '.4f')))
            print('------------------------------------')
        num = num**2
        sum += num
        
    return sum


'''
=========================== get_variance() =========================
Takes the dataset as argument as well as the return value from 
sum_of_the_squares() and will determine the variance for this 
dataset. 
'''
def get_variance(data_list, sum_of_squares):
    return sum_of_squares / (len(data_list)-1)


'''
============================ get_deviation() =======================
returns the standard deviation of the dataset with the argument 
that is produced from the get_variance() method 
'''
def get_deviation(variance):
    return math.sqrt(variance)


'''
========================= get_pop_variance() =======================
This does the same as the above method except for population 
variance as that formula is slightly different
'''
def get_pop_variance(data_list, sum_of_squares):
    return sum_of_squares / (len(data_list))

def title_block():
    print('''

==================== 1 Variable Stats =====================
This will provide the bulk of data needed for several types
of statistics problems. 

Enter some or all of your dataset and hit enter to save.
Seperate data points with a comma or space.
The number of spaces or commas is not discriminate.

When all data is entered for that dataset input \'d\'  
on an empty line when done and the program will continue 
to your next prompt. 

At any point you can type \'q\' to quit and return to 
main menu
''')
'''
=========================== main_loop() ===========================
Main loop that will continue to run as long as the user needs. 
'''
def main_loop():

    while True:
        print('\n==================== 1 Variable Stats =====================')
        print('===========================================================')
        print('You can copy and paste your data values in',
        '\nas long as each data point is seperated by a comma or space.',
        '\nNote that it does not matter how many spaces or commas only ',
        '\nthat the data is seperated. Type (q) when you want to quit ')
        print('===========================================================\n')


        print('AFTER ENTERING DATA SET: TYPE (d) TO SIGNIFY DONE.\n')
        print('Do you need the handwritten figures as well?',
        '\n(This is sometimes asked for in early homework)')
        handwritten = input('Type (y) for yes and (n) for no: ')
        while handwritten.lower() != 'y' and handwritten.lower() != 'n' and handwritten.lower() != 'q':
            print('\nThat is not an option.',
                'Try again.\n')
            print('Do you need the handwritten figures as well?',
            '\n(This is sometimes asked for in early homework)')
            handwritten = input('Type (y) for yes and (n) for no: ')
        if handwritten == 'y':
            handwritten = True
        elif handwritten == 'q':
            break
        else:
            handwritten = False
        print()
        data_string = valid.get_data_set()
        data_list = valid.process_data_string(data_string)
        if  data_list == False:
            break

        mean = get_mean(data_list)
        median = get_median(data_list)
        mode = get_mode(data_list)
        data_range = get_range(data_list)
        big_n = len(data_list)
        sum_of_squares = sum_of_the_squares(data_list, mean)
        variance = get_variance(data_list, sum_of_squares)
        pop_variance = get_pop_variance(data_list, sum_of_squares)
        deviation = get_deviation(variance)
        pop_deviation = get_deviation(pop_variance)

        print('------------------------------------')
        print('Sorted list below:')
        print(*data_list, sep=', ')
        print()
        print('\nThe mean is {}\nThe Median is {}\nThe Mode is {} '.format(format(mean,'.4f'), median, mode))
        print()
        print('The range is: {}'.format(format(data_range,'.4f')))
        print()
        print('============== Standard( Working with Sample )')
        print('The standard variance is: {}'.format(format(variance,'.4f')))
        print('The standard deviation is: {}'.format(format(deviation, '.4f')))
        print('\n========== Population(When working with all data from pop)=====')
        print('The population variance is : {}'.format(format(pop_variance, '.4f')))
        print('The population deviation is : {}'.format(format(pop_deviation, '.4f')))

        if handwritten:
            data_set_unsorted = valid.process_data_string(data_string, sort = False)
            print('------------------------------------')
            print('Your Handwritten information: ')
            sum_of_the_squares(data_list, mean, handwritten)
            print('The sum of the squares is: {}'.format(format(sum_of_squares,'.4f')))
            print('------------------------------------')
        quartiles.main_func(data_string)

