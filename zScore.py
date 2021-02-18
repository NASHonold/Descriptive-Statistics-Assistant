
import valid

def Get_Zscore(value, mean, deviation):
    numerator = value - mean
    denominator = deviation
    return (numerator / denominator)

def get_value(zscore, mean, deviation):
    return ((zscore * deviation) + mean)

def Zscore_with_value():
    value = valid.get_float_selection('What it is the x value?: ')
    if value == False:
        return False
    mean = valid.get_float_selection('What it is the mean value?: ')
    if mean == False:
        return False
    deviation = valid.get_float_selection('What is the standard deviation?: ')
    if deviation == False:
        return False
    answer = Get_Zscore(value, mean, deviation)
    return answer
    


def get_value_from_zscore():
    zscore = valid.get_float_selection('What is the Z score?: ')
    if zscore == False:
        return False
    mean = valid.get_float_selection('What it is the mean value?: ')
    if mean == False:
        return False
    deviation = valid.get_float_selection('What is the standard deviation?: ')
    if deviation == False:
        return False
    answer = get_value(zscore, mean, deviation)
    return answer
    print('Your  x value is {}'.format(format(answer, '.4f')))



def main_loop():
    while True:
        print('--------------------------------------------------')
        print('\nYou have the option of finding the zscore from value',
        '\nor the value from the zscore. Select below.\n')
        print('--------------------------------------------------')
        print('Type (z) to find zscore and (v) to find value and (q) to quit')
        operation = input('Enter selection here: ')
        if operation.strip() == 'z':
            answer = Zscore_with_value()
            if answer == False:
                break
            print('Your z score is {}'.format(format(answer, '.4f')))
        elif operation.strip() == 'v':
            answer = get_value_from_zscore()
            if answer == False:
                break
            print('Your  x value is {}'.format(format(answer, '.4f')))
        elif operation.strip() == 'q':
            break


main_loop()



