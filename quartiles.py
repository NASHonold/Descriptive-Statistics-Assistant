import valid



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
    return data_list[0],q1,q2,q3,data_list[-1]


def main_func(data_string):
    data_list = valid.process_data_string(data_string)
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
---------------------------
The five number summary is: 
Min: {}
q1: {}
q2: {}
q3: {}
Max: {}
IQR: {}
Lower Fence: {}
Upper Fence: {}
---------------------------
'''.format(min, q1, q2,q3,max,iqr,lower_fence,upper_fence))


