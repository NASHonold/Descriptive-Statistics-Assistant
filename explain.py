
from tkinter import *
'''
This file contains the text for all of the question mark buttons to display. 
The function explain takes a num input that is the index for both arrays of strings. 
then it simply displays that data in a new window for the user so they can 
understand what the menu item does before clicking on it. 

'''
def explain(num):
    text_list = [
        '''
This will provide the bulk of data needed for several types
of statistics problems.

Enter your dataset in the dataset box and click the calculate button.
This will provide you with:
    mean
    median
    mode
    range
    Standard variance and deviation
    Population variance and deviation

If you need Handwritten calculations for the variance and deviation
figures you should click the 'handwritten' button. This is useful
early in stats when sometimes your work must be shown for this.

        ''',
        '''
This tool allows you to give the width of your classes,
number of classes, the starting lower boundary, 
and your dataset. Once you click 'calculate' this will propose
a precise class width that you can adjust but will give you 
upper and lower class boundaries, class midpoints, and 
estimated xbar(mean)

        ''',
        '''
This tool will let you make Z score calulations for you. 
This can either get your Z score from x value, population mean,
and standard deviation 

--OR--

can calculate your x value from Z score, population mean, 
and standard deviation.
        ''',
        '''
This tool is used to calculate weighted averages using 
2 datasets. The first set is the data and the second is the 
associated weights. Because of this it is IMPERATIVE that 
the datasets are in the same order. 

Ex.

data                   weight
100                    .23
144                    .27
200                    .50
Therefore:
data = 100, 144, 200
weight = .23,.27,.5

if you mixed up the order of the weights to the datapoints you 
would get a different and wrong output. 
        ''',
        '''
This tool will take your dataset, allow you to fine tune the 
class widths and boundaries and give you the data to produce 
a representative Histogram for the dataset.
        '''

    ]

    title_list =[
        '1 Variable Stats',
        'Grouped Frequency Distribution',
        'Z Score Calculations',
        'Weighted Average Calculation',
        'Histogram Maker'
    ]

    num = num - 1
    helpWindow= Tk()
    helpWindow.title(title_list[num] + ' Explained')
    helpWindow.iconbitmap('images/icon.ico')
    
    window_label = Label(helpWindow, text=text_list[num], relief=SUNKEN, justify=LEFT)
    window_label.grid(row=0, column=0, ipadx=25)
