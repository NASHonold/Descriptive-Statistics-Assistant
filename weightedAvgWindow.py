import tkinter as tk
from tkinter.constants import LEFT, TOP
from tkinter.scrolledtext import ScrolledText as scrolledText
from typing import Text
import valid as valid
import weightedMean

#function for calculate button

def calculate(tkWindowName, entryWidgetOne, entryWidgetTwo):
    global output
    global errorMsg 
    outputText = ""
    try:
       output.destroy()
    except NameError:
        pass
    try:
       errorMsg.destroy()
    except NameError:
        pass

    # try:
    #     errorMsg.destroy()
    # except NameError:
    #     pass

    dataSetOne = valid.process_data_string(entryWidgetOne.get('1.0', tk.END),False)

    dataSetTwo = valid.process_data_string(entryWidgetTwo.get('1.0', tk.END),False)

    print(dataSetOne)
    print(dataSetTwo)

    if len(dataSetOne) != len(dataSetTwo):
        errorMsg = tk.Label(tkWindowName, text = "Error: Datasets don't have the same number of elemets", fg="red")
        errorMsg.grid(row=1, column=1, rowspan= 2)
    else:
        outputText = weightedMean.get_weighted(weightedMean.get_numerator(dataSetOne,dataSetTwo), weightedMean.get_denominator(dataSetTwo))
        print(str(outputText))
        output = tk.Label(tkWindowName, text = format(outputText, '.4f'))
        output.grid(row=3, column=3)
    

def weightAvgWindow(windows):
    window = tk.Toplevel()
    windows.append(window)
    window.title('Weighted Average Calculator')
    window.iconbitmap('images/icon.ico')
    window.geometry("610x280+1200+425")
    #create 2 frames for the two input windows to take both datasets
    inputFrameLeft = tk.LabelFrame(window, text='Input dataset Here...')
    inputFrameLeft.grid(row=0, column=0, columnspan=2)

    inputFrameRight = tk.LabelFrame(window, text="Input dataset with weighted values here...")
    inputFrameRight.grid(row=0, column=2, columnspan=2)
    #creates both scrolled text windows that are like entry windows to take in 
    #dataset inputs. They are placed in their respective LabelFrames
    datasetLeft = scrolledText(inputFrameLeft, width = 35, height =10)
    datasetLeft.grid(row=0, column=0)
    datasetLeft.grid_propagate = False

    datasetRight = scrolledText(inputFrameRight, width = 35, height =10)
    datasetRight.grid(row=0, column=2)
    datasetRight.grid_propagate = False

    #create calculate button
    calcButton = tk.Button(window, text = "Calculate", width=30, height=4, command= lambda: calculate(window, datasetLeft, datasetRight))
    calcButton.grid(row=3, column=0, columnspan=2)

    #create label for output
    outputTitle = tk.Label(window, text="Weighted Average: ", justify=LEFT)
    outputTitle.grid(row=3, column=2 )
   
     

    tk.mainloop()


