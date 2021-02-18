# get l1 data
#get l2 data

#do calc 

#print result

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



def get_numerator(a_list, b_list):
    sum = 0
    for number in range(len(a_list)):
        sum += (a_list[number] * b_list[number])
    return sum

def get_denominator(b_list):
    value = float(sum(b_list))
    return value

def get_weighted(numerator, denominator):
    result = numerator / denominator
    return result

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
        a_list = list_from_string(get_data_set())
        print('---------- Weight List ----------')
        print('What are the weights for list 2. (d) when done:')
        b_list = list_from_string(get_data_set())
    return a_list, b_list

#document file
#create check for lists of same length and while loop to rectify
print('=================================================')
print('         Calculating weighted averages')
print('=================================================')
print(
    '''
You can calculated the weighted averages 
for your tables with this calculator. 
When inputting data you can copy and paste,
you can hand key it in and it doesnt have to be 
on seperate lines. Ex enter data: 48 54 65 78 etc.
When you are done with that set of data hit enter
 then type (d) for done. This will save that data 
and move on to the next set. Also, you can type 
(q) at any time to quit or of course just exit
the window. Let's get started
=================================================
'''
)

while True:
    print('---------- Value List ----------')
    print('What are the mean values in list one.(d) when done:')
    a_list = list_from_string(get_data_set())
    print('---------- Weight List ----------')
    print('What are the weights for list 2. (d) when done:')
    b_list = list_from_string(get_data_set())
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
    if run_var.strip() == 'q':
        break
    print('================================================\n')
