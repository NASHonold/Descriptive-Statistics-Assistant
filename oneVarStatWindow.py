import tkinter as tk
from tkinter.constants import E, END, LEFT, W
from tkinter.scrolledtext import ScrolledText
import meanMedianMode, quartiles


def calculate(text_widget, tkwindowname):
    
    dataset = text_widget.get('1.0', tk.END)
    mean, median, mode, data_range, sum_of_squares,variance, deviation,pop_variance, pop_deviation = meanMedianMode.main_func(dataset)

    min, q1, q2, q3, max = quartiles.get_quartiles(dataset)
    iqr = (q3 - q1)
    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)

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
    mean_label = tk.Label(tkwindowname, text='Dataset Info Summary:')
    mean_label.grid(row=2, column=0,columnspan=2)

    median_label = tk.Label(tkwindowname, text=data_summary_text,justify=LEFT)
    median_label.grid(row=3, column=0,sticky=W)

    mode_label = tk.Label(tkwindowname, text=data_text, justify=LEFT)
    mode_label.grid(row=3, column=1,sticky=W)

    #labels for 5 number summary 
    summary = tk.Label(tkwindowname, text='5 Number Summary:')
    summary.grid(row=2, column=2, columnspan=2)

    summary_label = tk.Label(tkwindowname, text=five_summary_text, justify=LEFT)
    summary_label.grid(row=3, column=2, sticky=W)

    summary_data_label = tk.Label(tkwindowname, text=five_summary_data, justify=LEFT)
    summary_data_label.grid(row=3, column=3, sticky=W)

    handwritten_button = tk.Button(tkwindowname, text='Handwritten Figures')
    handwritten_button.grid(row=1, column=2, ipady=10, sticky=W, columnspan=2, ipadx=70)


    


def oneVarStat():
    window = tk.Toplevel()
    window.title('One Variable Stat')
    window.iconbitmap('images/icon.ico')
    
    input_frame = tk.LabelFrame(window, text='Input Dataset here...')
    input_frame.grid(row=0, column=0, columnspan=4)

    data_set_entry = ScrolledText(input_frame, width = 45, height =20)
    data_set_entry.grid(row=0, column=0)
    data_set_entry.grid_propagate = False

    calc_button = tk.Button(window, text='Calculate', command= lambda: calculate(data_set_entry, window))
    calc_button.grid(row=1, column=0, ipady=10, sticky=W, columnspan=2, ipadx=70)



    this_text = data_set_entry.get('1.0','end')
    print(this_text)


    window.mainloop()
