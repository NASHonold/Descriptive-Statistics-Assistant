
import meanMedianMode

def print_menu():
    print('''
================== Menu ==================
Select from the options below to select
that tool. The letter you type in will 
be indicated by the number after the 
description inside the (). 

 1 Variable stats---------------------(A)
    Includes the general ouputs for 
    a data set such as mean, median,
    mode, variance and deviation, and
    5 number summary including IQR
    and low and high fence. 
    Just enter the data set!

 Grouped Frequency Distribution-------(B)
    You will be prompted for the
    width of the classes, number of
    classes, what the first lower 
    class boundary is, and then 
    to input your data set. 
    Will output lower and upper 
    class boundaries, class midpoints, 
    and the estimated x-bar(mean)

Z score calculations------------------(C)
    This will calculate your z score
    given the x value, population mean,
    and the standard deviation. Will 
    also let you calculate what your
    x value would be given you have 
    the z score, mean, and deviation.

Weighted Average calculation----------(D)
    This will take two lists of data 
    sets for the given values and 
    their correlating weighted values.
    *Important* 
    When entering data ensure you 
    enter the correct weight for 
    the correct value. 

Histogram Maker-----------------------(E)
    Will allow you to input your data
    set and fine tune the class widths
    as well as the boundaries or the
    class data. Will output information
    to construct a proper histogram.

Quit----------------------------------(Q)
    Type (Q) for quit!

=========================================
    ''')





def print_intro():

    print('''
==============================================
          General Statistics Helper
==============================================

This is a set of tools to assist in general
statistics and is so far built for the first 
quarter of the class. 

This includes tools to help with mean, median, 
and range, weighted averages, assistance with 
frequancy graphs, ranking(percentile), 
standard and population deviations and
variances. Also includes zscore calculations
and weighted averages.
Possibly more later!
'''
)

def get_menu_choice():
    print()
    choice = input('Enter Selection Here: ').upper()
    options = ['A','B','C','D','E','Q']

    while choice not in options:
        print('\n=========================================\n')
        print('That is not an option on the list.',
        '\nTry again.\n')
        print_menu()
        choice = input('Enter Selection Here: ').upper()
    return choice





def main_loop():
    print_intro()
    while True:
        print_menu()
        choice = get_menu_choice()
        
        if choice == 'A':
            meanMedianMode.main_loop()
            print('in a')

        elif choice == 'B':
            print()

        elif choice == 'C':
            print()

        elif choice == 'D':
            print()

        elif choice == 'E':
            print()

        elif choice == 'Q':
            print('Thanks for using the stat helper!')
            break

main_loop()


        
        









