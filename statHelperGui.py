'''
Program: Stat Helper
File: statHelperGui.py
Author: N. Honold
Date: 02.08.2021
Purpose: To assist with early statistics and allow for larger data sets to be used without the need to 
input in personal calculator in a more user friendly way
'''


from oneVarStatWindow import oneVarStat
import os,sys, pathlib
from os import path
from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

#local imports
from explain import explain

'''
------------------ restart_program() ------------------
Restarts program and clears all currently open windows
'''
def restart_program():
    python = str(pathlib.Path(__file__).absolute())
    base.quit()
    
    os.startfile(python)
'''
when i eventually want to open without terminal i can look 
to do it in several different ways
1 create executable file and call it
2 determine the ways to do this on all os's and and then 
    determine os and then execute block of code that 
    pertains to that os.
3  try catch blocks??? probably not though 
'''



base = Tk()
base.title('Stat Helper Free')
base.iconbitmap('images/icon.ico')
w = 360
h = 300

#get screen width and height
sw = base.winfo_screenmmwidth()
sh = base.winfo_screenheight()
print('screenwidth is : {} and screenheight is : {}'.format(sw,sh))

x =200
y= 100

base.geometry('%dx%d+%d+%d' % (w, h, x, y))


qmark = Image.open('images/qmark.png')
qmark = resizeimage.resize_contain(qmark, [20,20])
qmark = ImageTk.PhotoImage(qmark)


#main menu buttons to open the specific tools
mmm_button = Button(base, text='1 Variable Stats',relief=RAISED,command=oneVarStat)
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

q2 = Button(base, image=qmark, relief=RAISED, command= lambda : explain(2))
q2.grid(row=2, column=2, sticky=W, padx=(5,60))

q3 = Button(base, image=qmark, relief=RAISED, command= lambda : explain(3))
q3.grid(row=3, column=2, sticky=W, padx=(5,60))

q4 = Button(base, image=qmark, relief=RAISED, command= lambda : explain(4))
q4.grid(row=4, column=2, sticky=W, padx=(5,60))

q5 = Button(base, image=qmark, relief=RAISED, command= lambda : explain(5))
q5.grid(row=5, column=2, sticky=W, padx=(5,60))

#reset button
reset_button = Button(base, text='Reset Windows', command=restart_program, border=5)
reset_button.grid(row=6 , column=0, columnspan=3, ipadx=77, ipady=30)




mainloop()
