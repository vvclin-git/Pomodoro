import tkinter as tk
from tkinter.ttk import *
from Frames import Timer, Settings

class Pomodoro_Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pomodoro Timer')
        self.geometry('300x200')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)                
        self.stage_list = {}
        
        with open('stage_settings.txt', 'r') as stage_settings_file:            
            lines = stage_settings_file.readlines()
            self.stage_order = lines.pop(0).rstrip().split(',')
            for l in lines:
                key = l.split(',')[0]
                value = l.split(',')[1].rstrip()
                self.stage_list[key] = value        

        container = Frame(self)
        container.grid(row=0, column=0, sticky='NSEW')
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky='NSEW')
        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky='NSEW')

        self.frames = {}
        self.frames[Settings] = settings_frame
        self.frames[Timer] = timer_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

root = Pomodoro_Timer()
root.mainloop()