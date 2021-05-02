import tkinter as tk
from tkinter.ttk import *

class Timer(Frame):
    def __init__(self, window, controller, show_settings):
        super().__init__(window)
        self.time_str = tk.StringVar()
        self.running = False           
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        timer_container = Frame(self, padding='30 15 30 15', style='debug.TFrame')
        timer_container.grid(row=0, column=0, sticky="NSEW")


        timer_container.columnconfigure(0, weight=1)
        timer_container.columnconfigure(1, weight=1)
        timer_container.columnconfigure(2, weight=1)
        timer_container.rowconfigure(0, weight=1)
        timer_container.rowconfigure(1, weight=3)
        timer_container.rowconfigure(2, weight=1)
        # self.stage_list = {'Pomodoro':'25:00', 'Short Break':'05:00', 'Long Break':'10:00'}
        self.stage_list = controller.stage_list
        self.stage_order = controller.stage_order
        self.current_order = 0
        self.current_stage = tk.StringVar()
        self.current_stage.set(self.stage_order[self.current_order])
        self.time_str.set(self.stage_list[self.stage_order[self.current_order]])
        self._tick_job = None
        top_label = Label(timer_container, textvariable=self.current_stage)
        top_label.grid(row=0, column=0, columnspan=2, sticky='W')

        setting_button = Button(timer_container, text='Settings', command=show_settings)
        setting_button.grid(row=0, column=2, sticky='E')

        time_label = Label(timer_container, textvariable=self.time_str)
        time_label.grid(row=1, column=0, columnspan=3, sticky='NS')
        
        start_button = Button(timer_container, text='Start', command=self.start_timer)
        start_button.grid(row=2, column=0, sticky='EW')

        stop_button = Button(timer_container, text='Stop', command=self.stop_timer)
        stop_button.grid(row=2, column=1, sticky='EW')

        reset_button = Button(timer_container, text='Reset', command=lambda: self.reset_timer(0))
        reset_button.grid(row=2, column=2, sticky='EW')
    
    def reset_timer(self, stage_order):
        print(f'reset timer to order {stage_order}')
        self.running = False
        self.current_order = stage_order        
        self.time_str.set(self.stage_list[self.stage_order[self.current_order]])
        self.current_stage.set(self.stage_order[self.current_order])
        return
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.tick()
        print(self.current_stage.get())
        return
    
     

    def stop_timer(self):
        self.running = False
        if self._tick_job:
            self.after_cancel(self._tick_job)
            self._tick_job = None
        return
    
    def tick(self):
        current_time = self.time_str.get()            
        print(f'stage: {self.current_stage.get()}, order: {self.current_order}, time: {current_time}')
        current_minute, current_second = current_time.split(':')
        if self.running:
            if current_time != '00:00':            
                if int(current_second) > 0:
                    current_second = int(current_second) - 1
                    current_minute = int(current_minute)
                else:
                    current_second = 59
                    current_minute = int(current_minute) - 1
                # update time to gui and continue ticking
                self.time_str.set(f'{current_minute:02d}:{current_second:02d}')
                self._tick_job = self.after(1000, self.tick)
            else:            
                self.running = False
                if self.current_order < len(self.stage_order) - 1:
                    self.current_order += 1
                else:
                    self.current_order = 0            
                self.reset_timer(self.current_order)
                self.start_timer()            

        return          

    def time_str_parse(self, time_str):
        time_str_delimited =  time_str.split(':')
        minute = int(time_str_delimited[0])
        second = int(time_str_delimited[1])
        total_second = second + 60 * minute
        return total_second
    
    def time_str_output(self, total_second):
        time_str = '{:02d}'.format(int(total_second/60)) + ":" + '{:02d}'.format(total_second % 60)
        return time_str