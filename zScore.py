
import valid
'''
=================== get_zscore() ==================
THis will take the x value, the mean of the sample, 
and the supplied deviation and will return the given 
zscore
'''
def get_zscore(value, mean, deviation):
    numerator = value - mean
    denominator = deviation
    return (numerator / denominator)

'''
======================== get_xvalue ===================
This takes in the zscore and the mean and the deviation
and determines what the xvalue is
'''
def get_xvalue(zscore, mean, deviation):
    return ((zscore * deviation) + mean)

'''
===================== zscore_with_xvalue() ===============
This func is used to get values from user when the user is
provided with the xvalue and needs to find the zscore. Will
then return the zscore. 
'''
def zscore_with_xvalue():
    value = valid.get_float_selection('What it is the x value?: ')
    if value == False:
        return False
    mean = valid.get_float_selection('What it is the mean value?: ')
    if mean == False:
        return False
    deviation = valid.get_float_selection('What is the standard deviation?: ')
    if deviation == False:
        return False
    answer = get_zscore(value, mean, deviation)
    return answer
    

'''
====================== get_xvalue_from_zscore() ===============
This will get user valuse and determine what the x value is 
given the zscore, mean, and deviation is what has been given to 
the user. 
'''
def get_xvalue_from_zscore():
    zscore = valid.get_float_selection('What is the Z score?: ')
    if zscore == False:
        return False
    mean = valid.get_float_selection('What it is the mean value?: ')
    if mean == False:
        return False
    deviation = valid.get_float_selection('What is the standard deviation?: ')
    if deviation == False:
        return False
    answer = get_xvalue(zscore, mean, deviation)
    return answer
    print('Your  x value is {}'.format(format(answer, '.4f')))


'''
======================== main_loop() ====================
This loop will repeatedly prompt the user for input and 
continue to provide output until the user enters q for quit
'''
def main_loop():
    while True:
        print('--------------------------------------------------')
        print('\nYou have the option of finding the zscore from value',
        '\nor the value from the zscore. Select below.\n')
        print('--------------------------------------------------')
        print('Type (z) to find zscore and (v) to find value and (q) to quit')
        operation = input('Enter selection here: ')
        if operation.strip() == 'z':
            answer = zscore_with_xvalue()
            if answer == False:
                break
            print('Your z score is {}'.format(format(answer, '.4f')))
        elif operation.strip() == 'v':
            answer = get_xvalue_from_zscore()
            if answer == False:
                break
            print('Your  x value is {}'.format(format(answer, '.4f')))
        elif operation.strip() == 'q':
            break






