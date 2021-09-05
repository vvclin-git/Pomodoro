import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER
from tkinter.ttk import *
from Frames import Timer, Settings
from windows import set_dpi_awareness

set_dpi_awareness()

# Color Palette Definition
COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class Pomodoro_Timer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pomodoro Timer')
        self.geometry('300x200')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)                
        self.stage_list = {}
        
        # Styling
        style = Style()
        style.theme_use('clam')
        style.configure("Timer.TFrame", background=COLOUR_PRIMARY)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font="Courier 38",
            anchor=tk.CENTER
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Calibri", 16)
        )

        style.configure(
            "SettingsLightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Calibri", 12)
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Calibri", 11)
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )
        self["background"] = COLOUR_PRIMARY
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