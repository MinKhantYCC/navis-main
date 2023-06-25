import tkinter as tk
import math
import numpy as np

class meter():
    def __init__(self, master, height, width,
                 background='#000000', active_color = '#5500ff', deactive_color = '#ffffff',
                 meter_size = 75, total_amount = 200, amount_used = 145,
                 label=None, sub_label = None, font_color = "#ffbf18"):
        # fixed-value parameters
        self.master = master                    # master frame (tkinter frame object)
        self.height = height                    # height of the canvas (int)
        self.width = width                      # width of the canvas (int)
        self.background = background            # background color of the frame (str)
        self.active_color = active_color        # the color of tick for used amount (str)
        self.deactive_color = deactive_color    # the color of tick for unused amount (str)
        self.meter_size = meter_size            # the size of meter (int)
        self.total_amount = total_amount        # total amount of the meter (int)
        self.amount_used = amount_used          # used amount of the meter (int)
        self.label = label                      # Label of the meter (str)
        self.sub_label = sub_label              # unit label of the meter (str)
        self.font_color = font_color

        # dynamic-value parameters
        self.center_x = width//2                # center coordinate on x-axis of the meter
        self.center_y = height//2               # center coordinate on y-axis of the meter
        if self.meter_size>100:
            self.tick_length = meter_size * 0.15    # length of tick 0.15
            self.tick_width = meter_size * 0.04     # width of tick 0.03
            self.font_size = int(meter_size * 0.2)  # font size 0.2
        else:
            self.tick_length = meter_size * 0.15    # length of tick 0.15
            self.tick_width = meter_size * 0.04     # width of tick 0.03
            self.font_size = int(meter_size * 0.3)  # font size 0.2
        self.font = ('Arial', self.font_size)       # font
    
    def draw_meter(self):
        '''
            This function draw a semi-type meter on a tkinter canvas. 
        '''
        in_degree = int(self.amount_used/self.total_amount * 245)       # used amount to degree
        in_range = range(in_degree)                                     # used amount range
        text_center_x = self.center_x - self.font_size *0.5             # center x of value
        text_center_y = self.center_y - self.font_size *0.7             # center y of value

        self.canvas_frame = tk.Frame(self.master, height=self.height, width=self.width)  # create a frame
        self.canvas_frame.config(background=self.background)
        self.canvas_frame.pack()                                            # place it
        canvas = tk.Canvas(self.canvas_frame, height=self.height, width=self.width,
                           background=self.background)                  # create a canvas
        canvas.config(background=self.background)
        canvas.pack()                                                   # place it
        
        # start of ticks
        # we will only use 0-245 degree range and one tick per 5 degree
        # so limit is 49
        for i in range(49):
            angle = (i*5-30)*math.pi/180                #convert degrees to radian 
            # get x1, y1, x2, y2
            x1 = self.center_x - math.cos(angle) * (self.meter_size - self.tick_length)
            y1 = self.center_y - math.sin(angle) * (self.meter_size - self.tick_length)
            x2 = self.center_x - math.cos(angle) * self.meter_size
            y2 = self.center_y - math.sin(angle) * self.meter_size
            if i*5 in in_range:
                # if the degree is in used range
                canvas.create_line(x1, y1, x2, y2, fill = self.active_color, width = self.tick_width, tags = 'lines')
            else:
                # if the degree is not in used range
                canvas.create_line(x1, y1, x2, y2, fill = self.deactive_color, width = self.tick_width, tags = 'lines')

        # value label
        canvas.create_text(text_center_x, text_center_y, text= str(self.amount_used), 
                           font=self.font, fill=self.font_color)

        # Text label
        if self.label != None:
            label_center_x = self.center_x - self.font_size * 0.15
            label_center_y = text_center_y + self.font_size * 1.25
            canvas.create_text(label_center_x, label_center_y, text = self.label, 
                               font=('Arial', int(self.font_size*0.65)), fill=self.font_color)

        # unit label
        if self.sub_label != None:
            w_c = 0
            for i in range(3):
                if self.amount_used >= (10**i):
                    w_c += 1
            sub_label_center_x = self.center_x + (w_c * self.font_size * 0.5)
            sub_label_center_y = text_center_y + 10
            canvas.create_text(sub_label_center_x, sub_label_center_y, text = self.sub_label,
                               font = ('Arial', int(self.font_size*0.5)), fill=self.font_color)

    def set_amount_used(self, value):
        '''
            This function set the used_amount parameter value and redraw the meter.
        '''
        self.amount_used = value
        # reset the frame
        for widget in self.master.winfo_children():
            widget.destroy()
        # draw meter
        self.draw_meter()

    def simu(self):
        '''
            This function is used to update the meter every 3s
        '''
        val = np.random.randint(1,self.total_amount)
        # val = 100
        self.set_amount_used(val)
        self.master.after(5000, self.simu)

# root = tk.Tk()
# root.geometry('1366x768')
# root.config(background='#212b38')
# screen_width = root.winfo_screenwidth()                 # get screen width
# screen_height = root.winfo_screenheight()               # get screen height
# size = screen_width * 0.1 + screen_height * 0.2
# mymeter = meter(root, height=screen_height, width=screen_width, meter_size= size, 
#                 label='SPEED', sub_label='ms', active_color='#41ff21', deactive_color='#ff0000')
# mymeter.draw_meter()
# mymeter.simu()
# root.mainloop()