import tkinter as tk
from tkinter.constants import E, END, GROOVE, LEFT, RAISED, RIDGE, RIGHT, SUNKEN, W
from typing import Text
from valid import input_check_float
import zScore


def check_values(input_list):
    
    empty_val_count = 0
    value_list = []
    for value in input_list:
        val = value.get().strip()
        print('in for loop')
        if len(val) == 0:
            empty_val_count += 1
            value_list.append(0)
            print('found a value that was empty')
        elif len(val) != 0:
            try:
                print('made it into the try block ')
                val = float(val)
                print('was able to convert to float')
                value_list.append(val)
            except ValueError:
                return 'Cannot input non-numeric values'

    if empty_val_count > 1:
        return "There are not enough values for calculation"
    elif empty_val_count == 0:
        return 'Ther are too many values'
    if value_list[2] == 0 or value_list[3] == 0:
        return 'There are not enough values for calculation' 

    return value_list

def calc_button_command(input_list,output_list, error_label):
    global default_color
    error_label.config(text='', bg = default_color)

    check_result = check_values(input_list)


    if type(check_result) == str:
        error_label.config(text=check_result, bg='red', fg = 'yellow')
        error_label.grid(row=7, rowspan=5, column=0)

    elif check_result[0] == 0:
        answer = zScore.get_xvalue(check_result[1],check_result[2],check_result[3])

        output_list[0].config(text=str(answer))

        output_list[1].config(text=str(check_result[1]))

        output_list[2].config(text=str(check_result[2]))

        output_list[3].config(text=str(check_result[3]))
        # this is where we plug in the values
    else:
        answer = zScore.get_zscore(check_result[0],check_result[2],check_result[3])
        # this is where we plug in the values
        output_list[0].config(text=str(check_result[0]))

        output_list[1].config(text=str(answer))

        output_list[2].config(text=str(check_result[2]))

        output_list[3].config(text=str(check_result[3]))



def z_score_window(windows):
    directions = '''
In the input boxes enter the 3 pieces of 
data you have and click \"Calculate\" and 
the value will appear below.'''

    window = tk.Toplevel()
    windows.append(window)
    window.title('Z Score Calculator')
    window.iconbitmap('images/icon.ico')
    window.geometry("385x270+1200+350")

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

    #a list of Entry widgets to pass to function
    input_list = [x_value_input, z_score_input,mean_input, deviation_input]

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
    calc_button = tk.Button(window, text='Calculate', width = 20, command= lambda: calc_button_command(input_list, output_list,error_label))
    calc_button.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=W, padx=(15,0))

    #output labels
    x_value_output_label = tk.Label(window, text='X value:')
    x_value_output_label.grid(row=3, column=2,pady=(10,0),padx=(0,20),sticky=E)

    z_score_output_label = tk.Label(window, text='Z score:')
    z_score_output_label.grid(row=4, column=2,padx=(0,20), sticky=E)

    mean_output_label = tk.Label(window, text='Mean:')
    mean_output_label.grid(row=5, column=2,padx=(0,20),sticky=E)

    deviation_output_label = tk.Label(window, text='Standard Deviation:')
    deviation_output_label.grid(row=6, column=2, padx=(0,20),sticky=E)

    
    #temporary strings to fill the labels
    values = ['','','','']
    x_val = values[0]
    z_val = values[1]
    mean_val = values[2]
    dev_val = values[3]

    #output label values
    x_value_output = tk.Label(window, text='')
    x_value_output.grid(row=3, column=3,pady=(10,0),sticky=W)

    z_score_output = tk.Label(window, text='')
    z_score_output.grid(row=4, column=3,sticky=W)

    mean_output = tk.Label(window, text='')
    mean_output.grid(row=5, column=3,sticky=W)

    deviation_output = tk.Label(window, text='')
    deviation_output.grid(row=6, column=3, sticky=W)

    output_list = [x_value_output,z_score_output,mean_output,deviation_output]

    #creating the empty error label space to pass to the calc_command
    error_label = tk.Label(window, text='', pady=5)
    error_label.grid(row=7, column=0, columnspan=5)

    #grab default button color
    global default_color
    default_color = error_label['bg']
    #need to determine if need zscore or need x value
    # may not need the above if just create 4 input widgets and check if they contain values 
     
    # get data
    #calculate score
    #display data







    tk.mainloop()
    

a_string = '12.3'
a_number = float(a_string)
a_string = type(a_string)
print(a_string)
test_vals = ['12.3','','5','3']
