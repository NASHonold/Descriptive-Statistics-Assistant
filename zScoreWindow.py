import tkinter as tk
from tkinter.constants import E, END, GROOVE, LEFT, RAISED, RIDGE, RIGHT, SUNKEN, W
from typing import Text
import zScore


def z_score_window(windows):
    directions = '''
In the input boxes enter the 3 pieces of 
data you have and click \"Calculate\" and 
the value will appear below.'''

    window = tk.Toplevel()
    windows.append(window)
    window.title('Z Score Calculator')
    window.iconbitmap('images/icon.ico')
    window.geometry("385x300+1200+350")

    # Directions
    direct = tk.Label(window, text=directions, width=54,)
    direct.grid(row=0, column=0, columnspan=4,padx=4)

    a_frame = tk.Frame(window, relief=GROOVE, bd=1)
    a_frame.grid(row=1, column=0, columnspan=4, padx=(0,3))
    # entry boxes
    x_value_input = tk.Entry(a_frame, width=15)
    x_value_input.grid(row=0, column=1,pady=(10,0))

    z_score_input = tk.Entry(a_frame, width=15)
    z_score_input.grid(row=1, column=1)

    mean_input = tk.Entry(a_frame, width=15)
    mean_input.grid(row=0, column=3,pady=(10,0))

    deviation_input = tk.Entry(a_frame, width=15)
    deviation_input.grid(row=1, column=3)

    #entry box labels
    x_value_label = tk.Label(a_frame, text='X value:')
    x_value_label.grid(row=0, column=0,pady=(10,0))

    z_score_label = tk.Label(a_frame, text='Z score:', height=2)
    z_score_label.grid(row=1, column=0)

    mean_label = tk.Label(a_frame, text='Mean:')
    mean_label.grid(row=0, column=2, sticky=E,pady=(10,0))

    deviation_label = tk.Label(a_frame, text='Standard Deviation:', height=2)
    deviation_label.grid(row=1, column=2)

    column_space = tk.Label(a_frame)
    column_space.grid(row=0, column=4)

    #calculate button
    calc_button = tk.Button(window, text='Calculate', width = 20)
    calc_button.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=W, padx=(15,0))

    #output labels
    x_value_output_label = tk.Label(window, text='X value:')
    x_value_output_label.grid(row=3, column=2, sticky=W,pady=(10,0))

    z_score_output_label = tk.Label(window, text='Z score:', justify=LEFT)
    z_score_output_label.grid(row=4, column=2, sticky=W)

    mean_output_label = tk.Label(window, text='Mean:')
    mean_output_label.grid(row=5, column=2, sticky=W)

    deviation_output_label = tk.Label(window, text='Standard Deviation:')
    deviation_output_label.grid(row=6, column=2, )



    #need to determine if need zscore or need x value
    # may not need the above if just create 4 input widgets and check if they contain values 
     
    # get data
    #calculate score
    #display data







    tk.mainloop()
    



