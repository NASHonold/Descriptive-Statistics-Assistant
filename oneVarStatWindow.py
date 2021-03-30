import tkinter as tk
from tkinter.constants import E, END, LEFT, RAISED, W
from tkinter.scrolledtext import ScrolledText
from typing import Text
import meanMedianMode, quartiles




def create_hw_string(dataset):
    dataset, mean, sum = meanMedianMode.handwritten_results(dataset)
    return_string =''
    for x in range(len(dataset[0])):
        value = dataset[0][x]
        after_sub = dataset[1][x]
        squared = dataset[2][x]

        first_line = 'For the value {}:'.format(value)+'\n'
        second = '{} - {:.4f} = {:.4f}'.format(value, mean, after_sub) + '\n'
        third = '{:.4f} squared is {:.4f}\n'.format(after_sub,squared)
        this_string = first_line + second + third + '\n'
        return_string = return_string + this_string 

    last_string = 'The sum of all squares is {:.4f}'.format(sum)

    return_string = return_string + last_string
    return return_string

def handwork(tkwindowname, hw_text):
    global handwork_title_label
    global handwork_text_label

    handwork_title_label = tk.Label(tkwindowname,text='Handwritten Figures:')
    handwork_title_label.grid(row=0, column=4 )

    handwork_text_label = tk.Label(tkwindowname, text=hw_text, justify=LEFT)
    handwork_text_label.grid(row=1, column=4, rowspan=9)





def calculate(text_widget, tkwindowname):
    
    dataset = text_widget.get('1.0', tk.END)
    mean, median, mode, data_range, sum_of_squares,variance, deviation,pop_variance, pop_deviation = meanMedianMode.main_func(dataset)

    min, q1, q2, q3, max = quartiles.get_quartiles(dataset)
    iqr = (q3 - q1)
    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)

    hw_string = create_hw_string(dataset)

    data_summary_text = '''
Mean:
Median:
Mode:
Range:
Standard Variance:
Standard Deviation:
Population Variance:
Population Variance:
    '''
    data_text = '''
{:.4f}
{}
{}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
    '''.format(mean,median,mode,data_range,variance,deviation,pop_variance, pop_deviation)
    
    
    
    five_summary_text = '''
Minimum:
Quartile 1:
Quartile 2:
Quartile 3:
Max:
Iqr:   
Lower Fence:
Upper Fence:
    '''

    five_summary_data = '''
{:.4f}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
{:.4f}
    '''.format(min, q1,q2,q3,max,iqr,lower_fence, upper_fence)
    
    #the labels for mean, median, mode, range, standard and population variance and deviation
    mean_label = tk.Label(tkwindowname, text='Dataset Info Summary:', justify=LEFT)
    mean_label.grid(row=2, column=0,columnspan=2, sticky=W)

    median_label = tk.Label(tkwindowname, text=data_summary_text,justify=LEFT)
    median_label.grid(row=3, column=0,sticky=W)

    mode_label = tk.Label(tkwindowname, text=data_text, justify=LEFT)
    mode_label.grid(row=3, column=1,sticky=W)

    #labels for 5 number summary 
    summary = tk.Label(tkwindowname, text='5 Number Summary:', justify=LEFT)
    summary.grid(row=2, column=2, columnspan=2, sticky=W)

    summary_label = tk.Label(tkwindowname, text=five_summary_text, justify=LEFT)
    summary_label.grid(row=3, column=2, sticky=W)

    summary_data_label = tk.Label(tkwindowname, text=five_summary_data, justify=LEFT)
    summary_data_label.grid(row=3, column=3, sticky=W)

    handwritten_button = tk.Button(tkwindowname, text='Handwritten Figures', 
        command= lambda: handwork(tkwindowname,hw_string), relief=RAISED)
    handwritten_button.grid(row=1, column=2, ipady=10, columnspan=2, sticky=W,ipadx=30 )


    try:
        global handwork_title_label
        global handwork_text_label
        handwork_title_label.destroy()
        handwork_text_label.destroy()

    except NameError:
        pass

    



def oneVarStat(windows):
    
    window = tk.Toplevel()
    windows.append(window)
    window.title('One Variable Stat')
    window.iconbitmap('images/icon.ico')
    window.geometry("+475+100")
    

    
    input_frame = tk.LabelFrame(window, text='Input Dataset here...')
    input_frame.grid(row=0, column=0, columnspan=4)

    data_set_entry = ScrolledText(input_frame, width = 60, height =10)
    data_set_entry.grid(row=0, column=0)
    data_set_entry.grid_propagate = False

    calc_button = tk.Button(window, text='Calculate', 
        command= lambda: calculate(data_set_entry, window))
    calc_button.grid(row=1, column=0, ipady=10,  ipadx=70, padx=(40,0),sticky=W, 
     columnspan=2)

    

    window.mainloop()
