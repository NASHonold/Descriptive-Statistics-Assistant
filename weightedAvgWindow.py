import tkinter as tk
from tkinter.scrolledtext import ScrolledText as scrolledText
import valid as valid


#function for calculate button


def weightAvgWindow(windows):
    window = tk.Toplevel()
    windows.append(window)
    window.title('Weighted Average Calculator')
    window.iconbitmap('images/icon.ico')
    window.geometry("610x270+1200+425")
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
   
    #creating calculate button 

    tk.mainloop()


