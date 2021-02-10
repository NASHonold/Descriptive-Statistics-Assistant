import math

def list_from_string(string):
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
        
    a_list.sort()
    print(a_list)
    return a_list


       
            
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
            
def get_mean(data_list):
    list_length = len(data_list)
    list_total = sum(data_list)
    return list_total / list_length



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
        return "no mode avail"
    else:
        return current_mode

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

def get_range(data_list):
    min = data_list[0]
    max = data_list[-1]
    return (max - min)

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

def get_variance(data_list, sum_of_squares):
    return sum_of_squares / (len(data_list)-1)

def get_deviation(variance):
    return math.sqrt(variance)

def get_pop_variance(data_list, sum_of_squares):
    return sum_of_squares / (len(data_list))





while True:
    print('===========================================================')
    print('You can copy and paste your data values in',
    '\nas long as each data point is seperated by a comma or space.',
    '\nNote that it does not matter how many spaces or commas only that',
    '\nthe data is seperated. Type (q) when you want to quit ')
    print('===========================================================\n')


    print('AFTER ENTERING DATA SET TYPE (d) TO SIGNIFY DONE.\n')
    print('Do you need the handwritten figures as well?')
    handwritten = input('Type (y) for yes and (n) for no: ')
    while handwritten != 'y' and handwritten != 'n':
        print('That is not an option.',
        'Try again.')
        handwritten = input('Type (y) for yes and (n) for no: ')
    if handwritten == 'y':
        handwritten = True
    else:
        handwritten = False
    print()
    data_list = list_from_string(get_data_set())
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
    print('The mean is {}\nThe Median is {}\nThe Mode is {} '.format(format(mean,'.4f'), median, mode))
    print('The range is: {}'.format(data_range))
    
    print('The standard variance is: {}'.format(format(variance,'.4f')))
    print('The standard deviation is: {}'.format(format(deviation, '.4f')))
    print('The population variance is : {}'.format(format(pop_variance, '.4f')))
    print('The population deviation is : {}'.format(format(pop_deviation, '.4f')))
    if handwritten:
        print('Your Handwritten information: ')
        sum_of_the_squares(data_list, mean, handwritten)
        print('The sum of the squares is: {}'.format(format(sum_of_squares,'.4f')))

