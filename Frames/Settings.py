import tkinter as tk
from tkinter.ttk import *

class Settings(Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)
        self.stage_order = controller.stage_order
        self.stage_list = controller.stage_list
        self.controller = controller        
        self.stage_order_str = tk.StringVar()
        self.stage_order_str.set(str(self.stage_order))
        
        # s = Style()
        # s.configure('debug.TFrame', background='green')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        setting_container = Frame(self, padding='30 15 30 15', style='debug.TFrame')
        setting_container.grid(row=0, column=0, sticky="NSEW")
        setting_container.columnconfigure(0, weight=1)
        setting_container.columnconfigure(1, weight=1)     
        # setting_container.rowconfigure(0, weight=3)
        setting_container.rowconfigure(3, weight=1)
        
        
        stage_1_time = self.stage_list[list(self.stage_list.keys())[0]]
        self.stage_1_min = tk.StringVar()
        self.stage_1_min.set(int(stage_1_time.split(':')[0]))
        self.stage_1_sec = tk.StringVar()
        self.stage_1_sec.set(int(stage_1_time.split(':')[1]))
        
        stage_2_time = self.stage_list[list(self.stage_list.keys())[1]]
        self.stage_2_min = tk.StringVar()
        self.stage_2_min.set(int(stage_2_time.split(':')[0]))
        self.stage_2_sec = tk.StringVar()
        self.stage_2_sec.set(int(stage_2_time.split(':')[1]))

        stage_3_time = self.stage_list[list(self.stage_list.keys())[2]]
        self.stage_3_min = tk.StringVar()
        self.stage_3_min.set(int(stage_3_time.split(':')[0]))
        self.stage_3_sec = tk.StringVar()
        self.stage_3_sec.set(int(stage_3_time.split(':')[1]))      
        
        stage_1_label = Label(setting_container, text=list(self.stage_list.keys())[0])
        stage_1_label.grid(row=0, column=0, sticky='W')
        stage_1_adj_frame = Frame(setting_container)
        stage_1_adj_frame.grid(row=0, column=1, sticky='E')        
        stage_1_min_spin = tk.Spinbox(stage_1_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_1_min, format='%02.0f', width=2)
        stage_1_min_spin.pack(side='left')        
        stage_1_sec_spin = tk.Spinbox(stage_1_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_1_sec, format='%02.0f', width=2)
        stage_1_sec_spin.pack(side='left')

        stage_2_label = Label(setting_container, text=list(self.stage_list.keys())[1])
        stage_2_label.grid(row=1, column=0, sticky='W')
        stage_2_adj_frame = Frame(setting_container)
        stage_2_adj_frame.grid(row=1, column=1, sticky='E')        
        stage_2_min_spin = tk.Spinbox(stage_2_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_2_min, format='%02.0f', width=2)
        stage_2_min_spin.pack(side='left')        
        stage_2_sec_spin = tk.Spinbox(stage_2_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_2_sec, format='%02.0f', width=2)
        stage_2_sec_spin.pack(side='left')

        stage_3_label = Label(setting_container, text=list(self.stage_list.keys())[2])
        stage_3_label.grid(row=2, column=0, sticky='W')
        stage_3_adj_frame = Frame(setting_container)
        stage_3_adj_frame.grid(row=2, column=1, sticky='E')        
        stage_3_min_spin = tk.Spinbox(stage_3_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_3_min, format='%02.0f', width=2)
        stage_3_min_spin.pack(side='left')        
        stage_3_sec_spin = tk.Spinbox(stage_3_adj_frame, from_=00, to=59, increment=1, textvariable=self.stage_3_sec, format='%02.0f', width=2)
        stage_3_sec_spin.pack(side='left')

        save_button = Button(setting_container, text='Save Settinigs', command=self.save_settings)
        save_button.grid(row=3, column=0, sticky='W')

        timer_button = Button(setting_container, text='Back to Timer', command=show_timer)
        timer_button.grid(row=3, column=1, sticky='E')

        stage_order_entry = Entry(setting_container, textvariable=self.stage_order_str)
    
    def save_settings(self):
        self.controller.stage_list[list(self.stage_list.keys())[0]] = f'{self.stage_1_min.get()}:{self.stage_1_sec.get()}'
        self.controller.stage_list[list(self.stage_list.keys())[1]] = f'{self.stage_2_min.get()}:{self.stage_2_sec.get()}'
        self.controller.stage_list[list(self.stage_list.keys())[2]] = f'{self.stage_2_min.get()}:{self.stage_2_sec.get()}'
        print(self.controller.stage_list)
        return

    


        