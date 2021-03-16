'''
Program: Stat Helper
File: statHelperGui.py
Author: N. Honold
Date: 02.08.2021
Purpose: To assist with early statistics and allow for larger data sets to be used without the need to 
input in personal calculator in a more user friendly way
'''


import os
from os import path
from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

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
        ''',
        '''
        ''',
        '''
        ''',
        '''
        '''

    ]

    num = num - 1
    helpWindow= Tk()
    helpWindow.title(' 1 Variable Stat Explained')
    helpWindow.iconbitmap('images/icon.ico')
    
    window_label = Label(helpWindow, text=text_list[num], relief=SUNKEN, justify=LEFT)
    window_label.pack()




base = Tk()
base.title('Stat Helper Free')
base.iconbitmap('images/icon.ico')

qmark = Image.open('images/qmark.png')
qmark = resizeimage.resize_contain(qmark, [20,20])
qmark = ImageTk.PhotoImage(qmark)

mmm_button = Button(base, text='1 Variable Stats',relief=RAISED)
mmm_button.grid(row=1, column=1, padx=(60,0),ipadx=61,pady=5, sticky=W)

gfdt_button = Button(base, text='Grouped Frequency Distribution Table', relief=RAISED)
gfdt_button.grid(row=2,column=1, padx=(60,0), sticky=W)

zscore_button = Button(base, text='Z score calculations', relief=RAISED)
zscore_button.grid(row=3,column=1, padx=(60,0),ipadx=48,pady=5, sticky=W)


weighted_button = Button(base, text='Weighted Average calculation', relief=RAISED)
weighted_button.grid(row=4,column=1, padx=(60,0),ipadx=21, sticky=W)


gfdt_button = Button(base, text='Histogram Maker', relief=RAISED)
gfdt_button.grid(row=5,column=1, padx=(60,0),ipadx=54,pady=5, sticky=W)

#help buttons to explain the functions
q1 = Button(base, image=qmark, relief=RAISED, command= lambda : explain(1))
q1.grid(row=1, column=2, sticky=W, padx=(5,60))

q2 = Button(base, image=qmark, relief=RAISED)
q2.grid(row=2, column=2, sticky=W, padx=(5,60))

q3 = Button(base, image=qmark, relief=RAISED)
q3.grid(row=3, column=2, sticky=W, padx=(5,60))

q4 = Button(base, image=qmark, relief=RAISED)
q4.grid(row=4, column=2, sticky=W, padx=(5,60))

q5 = Button(base, image=qmark, relief=RAISED)
q5.grid(row=5, column=2, sticky=W, padx=(5,60))

mainloop()
