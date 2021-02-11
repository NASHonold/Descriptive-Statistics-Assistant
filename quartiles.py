

def Process_Data_String(string):
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


def Get_Median(data_list):
    list_length = len(data_list)
    if list_length % 2 == 1:
        median_index = int(list_length/2)
        return data_list[median_index]
    else:
        median_index2 = int(list_length/2)
        median_index1 = median_index2 - 1
        median_value = (data_list[median_index1] + data_list[median_index2]) / 2
        return median_value


def Get_Median_Index(data_list):
    list_length = len(data_list)
    median_index2 = 0
    if list_length % 2 == 1:
        median_index = int(list_length/2)
        return median_index,median_index2
    else:
        median_index2 = int(list_length/2)
        median_index1 = median_index2 - 1
        return median_index1, median_index2


def Get_Quartiles(data_list):
    median_index = 0
    median_index2 = 0
    median_index, median_index2 = Get_Median_Index(data_list)
    
    if median_index2 == 0:
        q2 = data_list[median_index]
        a_list = data_list[0:median_index]
        b_list = data_list[(median_index + 1):]
        q1 = Get_Median(a_list)
        q3 = Get_Median(b_list)
    else:
        q2 = Get_Median(data_list)
        a_list =data_list[0:median_index2]
        b_list = data_list[median_index2:]
        q1 = Get_Median(a_list)
        q3 = Get_Median(b_list)
    print(a_list, b_list)
    return data_list[0],q1,q2,q3,data_list[-1]



data_list = Process_Data_String(get_data_set())

min, q1, q2, q3, max = Get_Quartiles(data_list)
iqr = (q3 - q1)
lower_fence = q1 - (1.5 * iqr)
upper_fence = q3 + (1.5 * iqr)
min = format(min, '.4f')
q1 = format(q1, '.4f')
q2 = format(q2, '.4f')
q3 = format(q3, '.4f')
max = format(max, '.4f')
iqr = format(iqr, '.4f')
lower_fence = format(lower_fence, '.4f')
upper_fence = format(upper_fence, '.4f')


print('''
The five number summary is: 
Min: {}
q1: {}
q2: {}
q3: {}
Max: {}
IQR: {}
Lower Fence: {}
Upper Fence: {}
'''.format(min, q1, q2,q3,max,iqr,lower_fence,upper_fence))


