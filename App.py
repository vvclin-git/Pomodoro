import tkinter as tk
from tkinter.ttk import *

class Pomodoro_Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pomodoro Timer')
        self.geometry('300x200')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)        
        
        
        
        
        container = Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        timer_frame = Timer(container, self)
        timer_frame.grid(row=0, column=0, sticky='NSEW')


root = Pomodoro_Timer()
root.mainloop()