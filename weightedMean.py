import valid


'''
====================== get_numerator() ====================
Calculates what the numerator of our equation for weighted mean
'''
def get_numerator(a_list, b_list):
    sum = 0
    for number in range(len(a_list)):
        sum += (a_list[number] * b_list[number])
    return sum

'''
==================== get_denominator() =====================
Calculates what the denominator of our equation for weighted mean 
'''
def get_denominator(b_list):
    value = float(sum(b_list))
    return value

'''
==================== get_weighted() ========================= 
This calcualtes the value of dividing the numerator by 
the denominator whish is the weighted value
'''
def get_weighted(numerator, denominator):
    result = numerator / denominator
    return result
'''
======================= list_checker() ======================
This takes in the two lists provided by the user and checks
that they are the same length. This is because given a weighted
average each value must have a weight correlated with it.
This puts the user into a loop until the lists match in length
'''
def list_checker(a_list, b_list):
    while len(a_list) != len(b_list):
        print('''
------------------------------------
Your lists are not matching length.
In a weighted average every value has 
an associated weight.
Be careful and re-enter your values.
------------------------------------ 
        ''')
        print('---------- Value List ----------')
        print('What are the mean values in list one.(d) when done:')
        data_string = valid.get_data_set()
        a_list = valid.process_data_string(data_string, False)
        print('---------- Weight List ----------')
        print('What are the weights for list 2. (d) when done:')
        data_string = valid.get_data_set()
        b_list = valid.process_data_string(data_string, False)
    return a_list, b_list

#document file
#create check for lists of same length and while loop to rectify
def title_block():

    print('=================================================')
    print('         Calculating weighted averages')
    print('=================================================')
    print(
    '''
You can calculate the weighted averages 
for your tables with this calculator. 

Enter some or all of your dataset and hit enter to save.
Seperate data points with a comma or space.
The number of spaces or commas is not discriminate.

When all data is entered for that dataset enter \'d\'  
on an empty line when done and the program will continue 
to your next prompt. 

At any point you can type \'q\' to quit and return to 
main menu
=================================================
'''
)

'''
========================== main_loop() =====================
This is the main loop that processes two lists in from 
the user and then performs the calculations on both of
them and will then return the weighted average. 
'''
def main_loop():
    title_block()
    while True:
        print('---------- Value List ----------')
        print('What are the mean values in list one.(d) when done:')
        data_string = valid.get_data_set()
        if data_string == False:
            break
        a_list = valid.process_data_string(data_string, False)
        print('---------- Weight List ----------')
        print('What are the weights for list 2. (d) when done:')
        
        data_string = valid.get_data_set()
        if data_string == False:
            break
        b_list = valid.process_data_string(data_string, False)
        a_list, b_list = list_checker(a_list, b_list)
        print('---------------------------------------------\n')
        numerator = get_numerator(a_list, b_list)
        if numerator == False:
            break
        denominator = get_denominator(b_list)
        if denominator == False:
            break
        result = get_weighted(numerator, denominator)
        print('The weighted average for this data set is {}.'.format(format(result, '.4f')))
        print('\n---------------------------------------------\n')
        print('If you want to do another calculation press and key',
        '\nor just hit enter. Otherwise type (q) to quit. \n')
        run_var = input('Type your selection here, (q) for quit: ')
        if run_var.strip().lower() == 'q':
            break
        print('================================================\n')
