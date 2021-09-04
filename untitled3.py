# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:07:32 2021

@author: shram
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import pandas as pd
from pandas import DataFrame

root=tk.Tk()   
root.title("Anomaly Detection Using Vibration Analysis")
#root.resizable(False, False)
title=tk.Label(root, text="Anomaly Detection Using Vibration Analysis", padx=25, pady=6, font=("", 12)).pack()
root.geometry('500x500')                      #creating a window

file='0Enew2.csv'

def upload_file():
    global file
    file=tk.filedialog.askopenfilename()
    file=open(file ,'r')
    print(file.read())
    

    
    df=pd.read_csv(file.name)
    data2 = {'Vibration': df.Vibration_1, 'Time': df.index }
    df2 = DataFrame(data2,columns=['Vibration','Time'])
    figure2 = plt.Figure(figsize=(5,4), dpi=80)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    df2 = df2[['Vibration','Time']].groupby('Time').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='b', fontsize=10)


    canvas=FigureCanvasTkAgg(figure2, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
    toolbar=NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    

    
browse= tk.Button(root, text="Browse", bg="black", fg="white", command=lambda: upload_file())  #creating browse button
browse.bind("<Button-1>")
browse.place(x=300, y=150) 





frame = tk.Frame(root, bg='white')

get_data=tk.Label(root, text="Dataset (a CSV file)", fg="black", font=("", 12))    #creating dataset label
get_data.place(x=100, y=150)

check_result=tk.Button(root, text="Check Result", bg="black", fg="white")         #creating check result table
check_result.bind("<Button-1>")
check_result.place(x=250, y=300)

#def show_result():          
get_result=tk.Label(root, text="Result", fg="black", font=("", 12))    #creating dataset label
get_result.place(x=150, y=400)    
   

root.mainloop()