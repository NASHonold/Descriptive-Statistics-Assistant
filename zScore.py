

# take in the value
# take the mean
# take standard deviation
def Get_Zscore(value, mean, deviation):
    numerator = value - mean
    denominator = deviation
    return (numerator / denominator)

def get_value(zscore, mean, deviation):
    return ((zscore * deviation) + mean)

def Zscore_with_value():
    value = float(input('What it is the x value?: '))
    mean = float(input('What it is the mean value?: '))
    deviation = float(input('What is the standard deviation?: '))
    answer = Get_Zscore(value, mean, deviation)
    print('Your z score is {}'.format(format(answer, '.2f')))


def get_value_from_zscore():
    zscore = float(input('What is the Z score?: '))
    mean = float(input('What it is the mean value?: '))
    deviation = float(input('What is the standard deviation?: '))
    answer = get_value(zscore, mean, deviation)
    print('Your value is {}'.format(format(answer, '.2f')))

while True:
    print('--------------------------------------------------')
    print('\nYou have to option of finding the zscore from value',
    '\nor the value from the zscore. Select below.\n')
    print('--------------------------------------------------')
    print('Type (z) to find zscore and (v) to find value and (q) to quit')
    operation = input('Enter selection here: ')
    if operation.strip() == 'z':
        Zscore_with_value()
        print()
    elif operation.strip() == 'v':
        get_value_from_zscore()
        print()
    elif operation.strip() == 'q':
        break




