import valid


'''
====================== get_median() =====================
This is a method that takes in a method and return the 
value of the median. This is indiscriminate of the index 
so does not provide context for the quartile calculations
without haveing the index if the median value has multiple
occurences and different indicies. 
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
=================== get_median_index() ==================
The is method return two values since the median index
could be the value at the senter of the index or it
could be the two indecies in the senter of the dataset. 
If the median is only one value this will return its
index as the first median value while the other will 
return 0. If there are two values it will return both. 
'''
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

'''
==================== get_quartiles() ===================
This processes the data list and utilizes the above 2 
methods to determine the quartiles and returns the 5 
number summary as 5 different values

*could possibly return this data as a singular list
and later in main_func could append this list with the 
additional values. Could then pass this list to a print
func...
'''
def get_quartiles(data_list):
    
    median_index, median_index2 = Get_Median_Index(data_list)
    
    if median_index2 == 0:
        q2 = data_list[median_index]
        a_list = data_list[0:median_index]
        b_list = data_list[(median_index + 1):]
        q1 = get_median(a_list)
        q3 = get_median(b_list)
    else:
        q2 = get_median(data_list)
        a_list =data_list[0:median_index2]
        b_list = data_list[median_index2:]
        q1 = get_median(a_list)
        q3 = get_median(b_list)
    return data_list[0],q1,q2,q3,data_list[-1]

'''
====================== main_func() ======================
This utilizes all above functions to assign all data values
needed and then also does basic calculations to produce 
other data values. This is then printed in a print state-
ment
'''

def main_func(data_string):
    data_list = valid.process_data_string(data_string)
    min, q1, q2, q3, max = get_quartiles(data_list)
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


