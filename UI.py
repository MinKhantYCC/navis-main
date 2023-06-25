# import the required modules
from tkinter import *
import ttkbootstrap as ttkb
import math
import simulations as sm
import menu
import datetime
from meter import meter

# create a window 
root = ttkb.Window(themename= 'superhero')
root.title('NAVIS')                                     # set window title
screen_width = root.winfo_screenwidth()                 # get screen width
screen_height = root.winfo_screenheight()               # get screen height
screen_ratio = round(screen_height/screen_width,2)
root.geometry(f'{screen_width}x{screen_height}')        # set window size to screen
root.configure(background = '#212b38')                  # Custom root's background color
root.wm_state('zoomed')                                 # maximize the window
root.resizable(0,0)                                     # disable window resizing
root.attributes('-fullscreen', True)
#---------------------------------------------------UI section---------------------------------------------------------
menubar = menu.menu(root)
root.config(menu=menubar)

#Frames Size Definition
BF_width = int(screen_width * 0.15)     # button frame width
BF_height = int(screen_height *0.98)    # button frame height
DF_width = int(screen_width*0.85)       # dashboard frame width
DF_height = int(screen_height *0.98)    # dashboard frame height
TF_height = int(DF_height * 0.5)        # Top frame in dashboard frame height
MF_height = int(DF_height * 0.2)        # Middle frame in dashboard frame height
BtF_height = int(DF_height * 0.3)       # Bottom frame in dashboard frame height

# Custom Frame Styles
Button_Frame_Style = ttkb.Style()
Button_Frame_Style.configure('Btn.TFrame', background = '#37465b')
Dashboard_Frame_Style = ttkb.Style()
Dashboard_Frame_Style.configure('Dsh.TFrame',background = '#212b38')
Nav_Frame_Style1 = ttkb.Style()
Nav_Frame_Style1.configure('Nav1.TFrame', background='#37465b')
Nav_Frame_Style2 = ttkb.Style()
Nav_Frame_Style2.configure('Nav2.TFrame', background='#212b38')
Nav_Label_Style1 = ttkb.Style()
Nav_Label_Style1.configure('NavLab1.TLabel', background = '#37465b', foreground='#ffffff',
                           justify=ttkb.CENTER, font=('Roboto',13))
Nav_Label_Style2 = ttkb.Style()
Nav_Label_Style2.configure('NavLab2.TLabel', background = '#212b38', foreground='#ffffff',
                           justify=ttkb.CENTER, font=('Roboto',13))

# Creating Frame
Button_Frame = ttkb.Frame(root, height = BF_height, width = BF_width,               # Button_Frame
                          padding = 50, style = 'Btn.TFrame')
Dashboard_Frame = ttkb.Frame(root,height = DF_height, width = DF_width,             # Dashboard Frame
                             padding = 5, style = 'Dsh.TFrame')
Navigator = ttkb.Frame(root, height=screen_height*0.07//2, width=screen_width)      # Navigator Frame

# Frame Placing
Navigator.grid(row=0, column=0, columnspan=2)
Button_Frame.grid(row = 1, column = 0)
Dashboard_Frame.grid(row = 1, column = 1)

#disable frame from resize
Navigator.grid_propagate(0)
Button_Frame.grid_propagate(0)
Dashboard_Frame.grid_propagate(0)
Dashboard_Frame.pack_propagate(0)

# Frame and Label in Navigator
vs_label_frame = ttkb.Frame(Navigator, width=screen_width * 0.149, height= screen_height*0.07//2,style='Nav1.TFrame')
vs_name_label = ttkb.Label(vs_label_frame, text='Vessel Name', style='NavLab1.TLabel')
vs_name_frame = ttkb.Frame(Navigator, width=screen_width * 0.149, height= screen_height*0.07//2,style='Nav2.TFrame')
vs_name = ttkb.Label(vs_name_frame, text='NAVIS', style='NavLab2.TLabel')

IMO_label_frame = ttkb.Frame(Navigator, width=screen_width//9.5, height= screen_height*0.07//2,style='Nav1.TFrame')
IMO_Label = ttkb.Label(IMO_label_frame, text='IMO', style='NavLab1.TLabel')
IMO_num_frame = ttkb.Frame(Navigator, width=screen_width//9.5, height= screen_height*0.07//2,style='Nav2.TFrame')
IMO_number = ttkb.Label(IMO_num_frame, text='1234567', style='NavLab2.TLabel')

MMSI_label_frame = ttkb.Frame(Navigator, width=screen_width//8, height= screen_height*0.07//2,style='Nav1.TFrame')
MMSI_Label = ttkb.Label(MMSI_label_frame, text='MMSI', style='NavLab1.TLabel')
MMSI_num_frame = ttkb.Frame(Navigator, width=screen_width//8, height= screen_height*0.07//2,style='Nav2.TFrame')
MMSI_number = ttkb.Label(MMSI_num_frame, text='1234567', style='NavLab2.TLabel')

CS_label_frame = ttkb.Frame(Navigator, width=screen_width//8, height= screen_height*0.07//2,style='Nav1.TFrame')
CallSignLabel = ttkb.Label(CS_label_frame, text='CALL SIGN', style='NavLab1.TLabel')
CS_frame = ttkb.Frame(Navigator, width=screen_width//8, height= screen_height*0.07//2,style='Nav2.TFrame')
CallSign = ttkb.Label(CS_frame, text='1234567', style='NavLab2.TLabel')

# Place labels in Navigator
vs_label_frame.grid(row=0,column=0,padx=0)
vs_name_frame.grid(row=0,column=1,padx=0)
IMO_label_frame.grid(row=0, column=2)
IMO_num_frame.grid(row=0,column=3)
MMSI_label_frame.grid(row=0, column=4)
MMSI_num_frame.grid(row=0,column=5)
CS_label_frame.grid(row=0,column=6)
CS_frame.grid(row=0,column=7)

# disable frames in Navigator from resizing
for frames_ in Navigator.winfo_children():
    frames_.pack_propagate(0)
    for labels_ in frames_.winfo_children():
        labels_.pack(pady=2)

# frames in dashboard creation
Top_Frame = ttkb.Frame(Dashboard_Frame, height = TF_height, width = DF_width, style = 'Dsh.TFrame')
Middle_Frame = ttkb.Frame(Dashboard_Frame, height = MF_height, width = DF_width, style = 'Dsh.TFrame')
Bottom_Frame = ttkb.Frame(Dashboard_Frame, height = BtF_height, width = DF_width, style = 'Dsh.TFrame')

# disable frames in Dashboard from resizing
Top_Frame.grid_propagate(0)
Middle_Frame.grid_propagate(0)
Bottom_Frame.grid_propagate(0)

# Place the Frames in Dashboard Frame 
Top_Frame.grid(row = 0, column = 0, padx=40)
Middle_Frame.grid(row = 1, column = 0, padx=40)
Bottom_Frame.grid(row = 2, column = 0, padx=40)

# Define status variables of checkbutton
wind_show = ttkb.StringVar()
gps_show = ttkb.StringVar()
compass_show = ttkb.StringVar()
rudder_show = ttkb.StringVar()
rpm_show = ttkb.StringVar()
speed_show = ttkb.StringVar()
gyro_show = ttkb.StringVar()
echo_show = ttkb.StringVar()

# set them as Y (checked)
wind_show.set('Y')
gps_show.set('Y')
compass_show.set('Y')
rudder_show.set('Y')
rpm_show.set('Y')
speed_show.set('Y')
gyro_show.set('Y')
echo_show.set('Y')
top_show = True
mid_show = True
bot_show = True

# custom button style
Button_Style = ttkb.Style()
Button_Style.configure('Custom.TCheckbutton', 
                       background = '#37465b', 
                       font = ('Roboto', 15),
                       height = 12)

# Label
Dashboard_Label = ttkb.Label(Button_Frame, 
                             text = 'Dashboard', 
                             font = ('Roboto', 15, 'bold'),
                             width = 15, 
                             foreground = '#ffffff', 
                             background = '#37465b', 
                             justify = 'right')

# Checkbutton Creation
wind_indicator_button = ttkb.Checkbutton(Button_Frame, variable=wind_show, onvalue='Y', offvalue='N',
                         text = "Wind", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
gps_button = ttkb.Checkbutton(Button_Frame, variable=gps_show, onvalue='Y', offvalue='N', 
                         text = "GPS", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
rudder_button = ttkb.Checkbutton(Button_Frame, variable=rudder_show, onvalue='Y', offvalue='N', 
                         text = "Rudder", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
compass_button = ttkb.Checkbutton(Button_Frame, variable=compass_show, onvalue='Y', offvalue='N', 
                         text = "Compass", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
echo_sounder_button = ttkb.Checkbutton(Button_Frame, variable=echo_show, onvalue='Y', offvalue='N',
                         text = "Depth", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
speed_button = ttkb.Checkbutton(Button_Frame, variable=speed_show, onvalue='Y', offvalue='N',
                         text = "Speed", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
engine_rpm_button = ttkb.Checkbutton(Button_Frame, variable=rpm_show, onvalue='Y', offvalue='N',
                         text = "RPM", width = 15,style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())
gyro_button = ttkb.Checkbutton(Button_Frame, variable=gyro_show, onvalue='Y', offvalue='N',
                         text = "Gyro", width = 15, style = 'Custom.TCheckbutton',
                         command=lambda: CreateTF())

# Place checkbutton
Dashboard_Label.grid(row = 0, column = 0)
wind_indicator_button.grid(row = 1, column = 0)
gps_button.grid(row = 2, column = 0)
gyro_button.grid(row = 3, column = 0)
compass_button.grid(row = 4, column =0)
echo_sounder_button.grid(row = 5, column = 0)
speed_button.grid(row = 6, column = 0)
engine_rpm_button.grid(row = 7, column = 0)
rudder_button.grid(row = 8, column = 0)

for widget in Button_Frame.winfo_children():
    widget.grid(pady = int(screen_height/35))

def ResetFrame(parent):
    """ This function deletes all the widgets of a frame """
    for widget in parent.winfo_children():
        widget.destroy()

def UpdateFrameStauts():
    """
        This function detects changes in Frame status in order to change the visiblity of
        Top Frame, Middle Frame and Bottom Frame.
    """
    global top_show, mid_show, bot_show
    # if any widgets in Top Frame are selected, show top frame
    if wind_show.get() == 'Y' or gyro_show.get()=='Y' or gps_show.get() =='Y':
        top_show = True
    else:
        top_show = False
    
    # if any widgets in Middle Frame are selected, show Middle frame
    if compass_show.get()=='Y' or echo_show.get()=='Y':
        mid_show = True
    else:
        mid_show = False

    # if any widgets in Bottom Frame are selected, show Bottom frame
    if speed_show.get() == 'Y' or rpm_show.get() == 'Y' or rudder_show.get() == 'Y':
        bot_show = True
    else:
        bot_show = False

def ViewTopFrame(parent):
    """
       This function is responsible to show Wind, GPS and Rudder Widgets in parent frame.
    """
    global TF_height
    ResetFrame(parent)                          # Clear the top frame
    UpdateFrameStauts()                         # Check other frames' status
    if mid_show and bot_show:                   # if all widgets are selected
        TF_height = int(DF_height * 0.45)       # Top frame in dashboard frame height
    elif mid_show or bot_show:                  # if one of mid frame or bot frame are selected
        TF_height = int(DF_height * 0.6)        # Top frame in dashboard frame height
    else:                                       # if only top frame is selected
        TF_height = int(DF_height)              # Top frame in dashboard frame height
    # setting up the width for each widget in top frame
    wid_count = 0
    wid_count = (wid_count + 1) if wind_show.get() == 'Y' else 0
    wid_count = (wid_count + 1) if gps_show.get() == 'Y' else (wid_count+0)
    wid_count = (wid_count + 1) if gyro_show.get() == 'Y' else (wid_count+0)
    if wid_count == 0 or wid_count == 1:
        fwidth = DF_width * 0.9
    elif wid_count == 2:
        fwidth = DF_width * 0.44
    else:
        fwidth = DF_width//3.5
    Top_Frame.configure(height=TF_height, width=DF_width)
    # Since we add padding, must be exceed the number of widgets in top frame
    wid_height = TF_height//1.1
    # subsections of dashboard frame
    if top_show:
        # WIND 
        if wind_show.get() == 'Y':
            # Create a frame for wind indicator
            WIND = ttkb.Frame(parent, 
                            height = wid_height, 
                            width = fwidth, 
                            relief = "solid", style= 'Dsh.TFrame')   
            WIND.grid(row = 0, column = 0)                                      # place it on the 1st column
            WIND.pack_propagate(0)                                              # disable resizing
            #wind indicator  
            wind_speed = '40 kn'                                                # input data                   
            wind_canvas = Canvas(WIND, width = fwidth, height= wid_height)      # create canvas for drawing
            wind_canvas.configure(background = '#212b38')                       # set background color
            wind_canvas.pack()                                                  # just place canvas on the WIND frame
            #center and radius of the circle
            center_x = fwidth//2
            center_y = wid_height//2
            r_factor = fwidth/wid_height                                        # find the ratio of width and height
                                                                                # to adaptive to size changes
            if r_factor > 1:
                radius = (fwidth*0.023) + (wid_height*0.34)
            else:
                radius = (fwidth*0.2) + (wid_height*0.1)
            
            #add the tick marks and cardinal directions
            wind_direction = 0                                                  # input data
            for i in range(36):
                angle = i*10*math.pi/180 #convert degrees to radian
                tick_length = 15 if i%3==0 else 6
                x1 = center_x + math.cos(angle) * (radius - tick_length)
                y1 = center_y - math.sin(angle) * (radius - tick_length)
                x2 = center_x + math.cos(angle) * radius
                y2 = center_y - math.sin(angle) * radius
                wind_canvas.create_line(x1, y1, x2, y2, fill = 'white', width = 3)

                #add the cardinal directions
                if i == 9:
                    wind_canvas.create_text(center_x, center_y - radius + 25, text="N", fill="white")
                elif i == 18:
                    wind_canvas.create_text(center_x + radius - 25, center_y, text="E", fill="white")
                elif i == 27:
                    wind_canvas.create_text(center_x, center_y + radius - 25, text="S", fill="white")
                elif i == 0 or i == 36 - 1:
                    wind_canvas.create_text(center_x - radius + 25, center_y, text="W", fill="white")

                if i == 9:  # assume wind direction is 90 degrees
                    #calculate the coordinates of the triangle
                    tri_x = center_x + math.cos(angle) * (radius - tick_length + 20)
                    tri_y = center_y - math.sin(angle) * (radius - tick_length + 20)
                    tri_size = radius//13
                    tri_points = [
                        tri_x + tri_size * math.cos(angle + math.pi/2),
                        tri_y - tri_size * math.sin(angle + math.pi/2),
                        tri_x + tri_size * math.cos(angle - math.pi/2),
                        tri_y - tri_size * math.sin(angle - math.pi/2),
                        tri_x + tri_size * math.cos(angle),
                        tri_y + tri_size * math.sin(angle)
                    ]
                    #draw the triangle
                    tri = wind_canvas.create_polygon(tri_points, fill="#ffbf18", outline="#ffbf18", width = 2)

                    # Labels
                    # direction 
                    wind_direction = '90° N' # default
                    Direction = wind_canvas.create_text(center_x, center_y - 15, 
                                                        text = f"Direction: {wind_direction}", 
                                                        fill = "#ffbf18", font=('Roboto', 10, 'bold'))
                    # speed 
                    wind_speed = '20'
                    Speed = wind_canvas.create_text(center_x, center_y + 20, 
                                                    text = f"Speed: {wind_speed}", 
                                                    fill = "#ffbf18", font=('Roboto', 10, 'bold'))
                    # update wind direction and speed 
                    sm.update_wind_direction_speed(WIND, center_x, center_y, radius, tri_size, wind_canvas, tri, Direction, Speed)

                    for widget in WIND.winfo_children():
                        widget.grid(padx=3, pady=3)
        
        # GPS
        if gps_show.get() == 'Y':
            GPS = ttkb.Frame(parent,                                                 # Create GPS Frame
                            height = wid_height, 
                            width = fwidth, 
                            style = 'Dsh.TFrame', 
                            relief = "solid")
            GPS.grid(row = 0, column = 1)                                            # place it on the 2nd column
            GPS.grid_propagate(0)                                                    # disable resizing
            #GPS Label
            gps_label_frame = ttkb.Frame(GPS,                                       # create label frame
                                        width=fwidth,
                                        height = wid_height*0.1,
                                        style='Dsh.TFrame')
            gps_label_frame.grid(row=0, column=0, columnspan = 2)                   # place label frame
            gps_label = ttkb.Label(gps_label_frame,                                 # create Top label for the frame
                                    text='GPS', 
                                    font=('Roboto', 10),
                                    padding = 5, 
                                    justify = ttkb.CENTER, 
                                    bootstyle = 'success')
            gps_label.grid(row=0,column=0)                                          # place the label
            # Date Time
            date_time_frame = ttkb.Frame(GPS,                                       # create a separate frame for displaying value
                                height=wid_height*0.15,
                                width=fwidth-15,
                                padding=5,
                                style = 'Dsh.TFrame')
            date_time_frame.grid(row=1, column=0, columnspan=2, padx=10)            # place it on second row
            date_time_frame.grid_propagate(0)                                       # disable resizing
            # date time
            date_time = datetime.datetime.now()                                     # get the current date & time
            date_frame = ttkb.Frame(date_time_frame,padding = 1,                    # date frame
                                    width=fwidth*0.45,height=wid_height*0.1,style='Dsh.TFrame')
            date_frame.grid(row=0, column=0)                                        # place it
            date_frame.pack_propagate(0)                                            # disable resizing
            date_time_label1 = ttkb.Label(date_frame,                               # show date
                                    padding = 1,
                                    text= date_time.strftime('%x'), 
                                    font=('Roboto', 15, 'bold'),
                                    width= fwidth*0.45,
                                    justify = ttkb.LEFT,
                                    foreground = '#ffbf18',
                                    background= '#212b38')
            date_time_label1.pack(fill='both')                                      # place date label
            time_frame = ttkb.Frame(date_time_frame, padding=1,                     # time frame
                                    width=fwidth*0.5, height=wid_height*0.1,style='Dsh.TFrame') 
            time_frame.grid(row=0, column=1)
            time_frame.pack_propagate(0)                                            # disable resizing
            date_time_label2 = ttkb.Label(time_frame,                               # time frame
                                    padding = 1,
                                    text= date_time.strftime('%X'), 
                                    font=('Roboto', 15, 'bold'),
                                    width=fwidth*0.5,
                                    justify = ttkb.RIGHT,
                                    foreground = '#ffbf18',
                                    background= '#212b38')
            date_time_label2.pack(fill='both', padx=fwidth//10-20)
            sm.update_datetime(date_time_frame, date_time_label1,                   # simulate date_time
                               date_time_label2, ttkb.LEFT)

            #POS
            pos_frame = ttkb.Frame(GPS,                                             # create a separate frame for displaying value
                                height=wid_height*0.4,
                                width=fwidth-20,
                                padding=5,
                                style = 'Dsh.TFrame'
                                )
            pos_frame.grid(row=2, column=0, columnspan=2, padx=10)                  # place the frame
            pos_frame.pack_propagate(0)                                             # disable resizing
            #POS Label
            POS_label = ttkb.Label(pos_frame,                                       # create POS label
                                    text='POS', 
                                    font=('Roboto', 12),
                                    width= fwidth, 
                                    justify = 'left',
                                    background= '#212b38')
            POS_label.pack(fill='x', ipady=10)                                      # place POS label
            #POS value
            POS_value1 = "50° 39.6321' N\n 1° 42.7281 W'"                             # initial gps value
            POS_value_label1 = ttkb.Label(pos_frame,                                # display POS value
                                    padding = 1,
                                    text= POS_value1, 
                                    font=('Roboto', 20, 'bold'),
                                    width= fwidth,
                                    justify = ttkb.LEFT,
                                    foreground = '#ffbf18',
                                    background= '#212b38')
            POS_value_label1.pack(fill='x',ipady=10)                                # place POS value
            sm.update_gps(pos_frame, POS_value_label1, ttkb.LEFT)                   # simulate POS

            #Date, Time, SOG, COG
            SOG_COG_Frame = ttkb.Frame(GPS,                                         # create a frame to show Kn/ COG & DateTime
                                    height=wid_height * 0.25,
                                    width=fwidth-15,
                                    padding=5,
                                    style='Dsh.TFrame'
                                    )
            SOG_COG_Frame.grid(row=3, column=0, columnspan=2)                       # place the frame
            SOG_COG_Frame.grid_propagate(0)                                         # disable resizing
            #SOG
            SOG_frame = ttkb.Frame(SOG_COG_Frame,                                   # Kn Frame inside KnDt Frame
                                height=wid_height *0.3,
                                width = fwidth//2 - 10,
                                style='Dsh.TFrame')
            SOG_frame.grid(row=0, column=0)                                         # place Kn Frame at first column
            SOG_frame.pack_propagate(0)                                             # disable resizing
            SOG_label = ttkb.Label(SOG_frame,                                       # create label
                                text='SOG', 
                                font=('Roboto', 12),
                                padding= 5,
                                width= fwidth//2, 
                                justify = ttkb.LEFT,
                                background= '#212b38')
            SOG_label.pack(fill='x')                                                # place it and fill the frame
            SOG_value = ttkb.Label(SOG_frame,                                       # Create Kn Value Label
                                text='12.0', 
                                font=('Roboto', 16, 'bold'),
                                width= fwidth//2,
                                padding=3,
                                justify = ttkb.LEFT,
                                foreground = '#ffbf18',
                                background= '#212b38')
            SOG_value.pack(fill='x')                                                # place it and fill the frame
            sm.update_sog(SOG_COG_Frame,SOG_value,ttkb.LEFT)
            #COG
            COG_frame = ttkb.Frame(SOG_COG_Frame,                                   # Create COG Frame inside KnDt Frame
                                height=wid_height*0.3,
                                width = fwidth//2 - 10,
                                style='Dsh.TFrame')
            COG_frame.grid(row=0, column=1)                                         # Place the frame at second column
            COG_frame.pack_propagate(0)                                             # disable resizing
            COG_label = ttkb.Label(COG_frame,                                       # create COG label
                                text='COG M', 
                                font=('Roboto', 12),
                                padding= 5,
                                width= fwidth//2, 
                                justify = ttkb.LEFT,
                                background= '#212b38')
            COG_label.pack(fill='x')                                                # place it and fill the frame
            COG_value = ttkb.Label(COG_frame,                                       # create COG value label
                                text='125°', 
                                font=('Roboto', 16, 'bold'),
                                width= fwidth//3 -10,
                                padding=3,
                                justify = ttkb.LEFT,
                                foreground = '#ffbf18',
                                background= '#212b38')
            COG_value.pack(fill='x')                                                # place it and fill the frame
            sm.update_COG(SOG_COG_Frame,COG_value,ttkb.LEFT)

        # Gyro
        if gyro_show.get() == 'Y':
            GYRO = ttkb.Frame(parent, 
                            height = wid_height, 
                            width = fwidth, 
                            style = 'Dsh.TFrame', 
                            relief = "solid")        # create a frame for gyro
            GYRO.grid(row = 0, column = 2)           # place it on the another column
            GYRO.pack_propagate(0)                   # disable resizing
            # gyro_label = ttkb.Label(GYRO, 
            #                         text='GYRO', 
            #                         font=('Roboto', 10),
            #                         justify = ttkb.CENTER, 
            #                         bootstyle = 'success')
            # gyro_label.pack() 
            canvas_height = wid_height
            gyro_canvas = Canvas(GYRO, width = fwidth, height= canvas_height)      # create canvas for drawing
            gyro_canvas.configure(background = '#212b38')                       # set background color
            gyro_canvas.pack()                                                  # just place canvas on the WIND frame
            gyro_canvas.pack_propagate(0)
            gyro_val = 25
            #center and radius of the circle
            gyro_center_x = fwidth//2
            gyro_center_y = canvas_height//2
            gyro_r_factor = fwidth/canvas_height                                # find the ratio of width and height
                                                                                # to adaptive to size changes
            if gyro_r_factor > 1:
                gyro_radius = (fwidth*0.01) + (canvas_height*0.37)
            else:
                gyro_radius = (fwidth*0.2) + (canvas_height*0.1)
            
            for i in range(36):
                gyro_angle = i*10*math.pi/180 #convert degrees to radian
                tick_length = 15 if i%3==0 else 6
                x1 = gyro_center_x + math.cos(gyro_angle) * (gyro_radius - tick_length)
                y1 = gyro_center_y - math.sin(gyro_angle) * (gyro_radius - tick_length)
                x2 = gyro_center_x + math.cos(gyro_angle) * gyro_radius
                y2 = gyro_center_y - math.sin(gyro_angle) * gyro_radius
                gyro_canvas.create_line(x1, y1, x2, y2, fill = 'white', width = 3)

                #add the cardinal directions
                if i == 9:
                    gyro_canvas.create_text(gyro_center_x, gyro_center_y - gyro_radius + 25, text="0°", fill="white")
                elif i == 18:
                    gyro_canvas.create_text(gyro_center_x + gyro_radius - 25, gyro_center_y, text="90°", fill="white")
                elif i == 27:
                    gyro_canvas.create_text(gyro_center_x, gyro_center_y + gyro_radius - 25, text="180°", fill="white")
                elif i == 0 or i == 36 - 1:
                    gyro_canvas.create_text(gyro_center_x - gyro_radius + 25, gyro_center_y, text="270°", fill="white")

                if i == 9:  # assume wind direction is 90 degrees
                    #calculate the coordinates of the triangle
                    tri_x = gyro_center_x + math.cos(gyro_angle) * (gyro_radius - tick_length + 20)
                    tri_y = gyro_center_y - math.sin(gyro_angle) * (gyro_radius - tick_length + 20)
                    tri_size = gyro_radius//13
                    tri_points = [
                        tri_x + tri_size * math.cos(gyro_angle + math.pi/2),
                        tri_y - tri_size * math.sin(gyro_angle + math.pi/2),
                        tri_x + tri_size * math.cos(gyro_angle - math.pi/2),
                        tri_y - tri_size * math.sin(gyro_angle - math.pi/2),
                        tri_x + tri_size * math.cos(gyro_angle),
                        tri_y + tri_size * math.sin(gyro_angle)
                    ]
                    #draw the triangle
                    tri = gyro_canvas.create_polygon(tri_points, fill="#ffbf18", outline="#ffbf18", width = 2)

                    # Labels
                    Gyro_Label = gyro_canvas.create_text(gyro_center_x, gyro_center_y - 15, 
                                                        text = "GYRO COMPASS", 
                                                        fill = "#ffbf18", font=('Roboto', 13))
                    
                    gyro_val_label = gyro_canvas.create_text(gyro_center_x, gyro_center_y + 10, 
                                                    text = f"{gyro_val}°", 
                                                    fill = "#ffbf18", font=('Roboto', 10))
                    # update wind direction and speed 
                    sm.update_gyro(GYRO, gyro_center_x, gyro_center_y, gyro_radius, tri_size, gyro_canvas, tri, gyro_val_label)

                    for widget in GYRO.winfo_children():
                        widget.grid(padx=3, pady=3)
            
        # add padding for each widget in top frame
        for widget in parent.winfo_children():
            widget.grid(padx = 10, pady = 5)
    else:
        Top_Frame.configure(height=0, width=DF_width)

def ViewMiddleFrame(parent):
    '''
       This function shows Compass and Echo (Depth) widget in Middle Frame
    '''
    global mid_show, MF_height
    ResetFrame(parent)                          # clear the middle frame
    UpdateFrameStauts()                         # check other frames' status
    if top_show and bot_show:                   # if all widgets are selected
        MF_height = int(DF_height * 0.2)        # height
        pad_distance = MF_height * 0.1          # padding-y value
    elif top_show and not bot_show:             # if top frame is shown but not bottom frame
        MF_height = int(DF_height * 0.3)        # Middle frame in dashboard frame height
        pad_distance = MF_height * 0.1
    elif not top_show and bot_show:             # if bottom frame is shown but not top frame
        MF_height = int(DF_height * 0.45)       # Middle frame in dashboard frame height
        pad_distance = MF_height * 0.3
    else:                                       # if only middle frame is selected
        pad_distance = MF_height * 0.5
        MF_height = int(DF_height)              # Top frame in dashboard frame height
    Middle_Frame.configure(height = MF_height, width=DF_width)  # change middle frame size wrt top & bot
    # setting up width for each frame
    wid_count = 0
    wid_count = (wid_count + 1) if compass_show.get() == 'Y' else (wid_count+0)
    wid_count = (wid_count + 1) if echo_show.get() == 'Y' else (wid_count+0)
    if wid_count == 0 or wid_count == 1:
        Mwidth = DF_width * 0.9
    else:
        Mwidth = DF_width * 0.442
    if mid_show:
        # subsections of dashboard frame 
        if compass_show.get() == 'Y':
            compass = ttkb.Frame(parent,                    # create a frame for rudder 
                                height = MF_height//1.2, 
                                width = Mwidth, 
                                style = 'Dsh.TFrame', 
                                relief = "solid")
            compass.grid(row = 0, column = 0)               # place it on the 1st column
            compass.pack_propagate(0)                       # disable from resizing
            compass_label = ttkb.Label(compass,             # create label frame
                                    padding = 5, 
                                    text='Compass ROT', 
                                    font=('Roboto', 10),
                                    justify = ttkb.CENTER, 
                                    bootstyle = 'success')
            compass_label.pack()                            # place it
            can_width = Mwidth-20                           # canvas width
            can_height = MF_height - 60                     # canvas height
            compass_canvas = Canvas(compass, width=can_width,height=can_height) # create canvas
            compass_canvas.configure(background='#212b38')  # set canvas bg color to dark blue
            compass_canvas.pack(pady=5)                    # add padding to top
            x1 = can_width * 0.13                           # start points of compass
            y1 = can_height * 0.15 + pad_distance * 0.2
            y2 = y1 + 20                                    # y-start points + height of a line
            steps = 21                                      # 10 points + 0 point
            steps_dist = (can_width * 0.8)//steps           # distance between each line
            # left most line
            compass_canvas.create_line(x1,y1,x1,y2+10,fill = 'red', width = 5)
            compass_canvas.create_text(x1-30, y2+10, text='-60°', fill = "#ffbf18", font=('Roboto', 13))
            # negative half
            for i in range(9):
                x1 = x1 + steps_dist
                compass_canvas.create_line(x1,y1,x1,y2,fill = 'red', width = 5)
            # 0 degree
            x1 = x1 + steps_dist
            compass_canvas.create_line(x1,y1,x1,y2+10,fill = 'white', width = 5)
            compass_canvas.create_text(x1+4, y1-10, text='0°', fill = "#ffbf18", font=('Roboto', 13))
            # positive half
            for j in range(10):
                x1 = x1 + steps_dist
                compass_canvas.create_line(x1,y1,x1,y2,fill = 'green', width = 5)
            # right most line
            compass_canvas.create_line(x1,y1,x1,y2+10,fill = 'green', width = 5)
            compass_canvas.create_text(x1+30, y2+10, text='+60°', fill = "#ffbf18", font=('Roboto', 13))
            sm.update_compass(compass_canvas, 
                            s_y = y2+10, 
                            min_x = int(can_width*0.13)+5, max_x = int(x1+5),
                            width = can_width, height = can_height)
        
        # ECHO
        if echo_show.get() == 'Y':
            ECHO = ttkb.Frame(parent,                                   # create a frame for echo
                            height = MF_height//1.2, 
                            width = Mwidth,
                            style = 'Dsh.TFrame', 
                            relief = "solid")                                
            ECHO.grid(row = 0, column = 1)                              # place it on the 3rd frame
            ECHO.pack_propagate(0)                                      # disable resizing
            echo_label = ttkb.Label(ECHO,                               # Echo/Depth Label
                                    padding = 5, 
                                    text='DEPTH', 
                                    font=('Roboto', 10),
                                    justify = ttkb.CENTER, 
                                    bootstyle = 'success') 
            echo_label.pack()
            # Progress Bar
            bar = ttkb.Progressbar(ECHO,                                # create progress bar
                                   length=Mwidth*0.7,
                                   maximum=1000,
                                   bootstyle="warning-striped",
                                   value=100)
            bar.pack(pady=pad_distance)                                 # add padding distance from top border
            # text frame
            text_frame = ttkb.Frame(ECHO, height = MF_height//2, width = Mwidth)# create a frame to show value
            text_frame.place(x=Mwidth//2-50, y=pad_distance+60)                 # place it below progess bar
            # text 
            echo_value = 1.40                                           # intialize a value (Replace later)
            echo_value_label = ttkb.Label(text_frame,                   # create a value label
                                    padding = 5, 
                                    text= str(echo_value) + ' m', 
                                    font=('Roboto', 20, 'bold'),
                                    justify = ttkb.CENTER, 
                                    foreground = '#ffbf18',
                                    background= '#212b38') 
            echo_value_label.pack()                                     # show it

            # simulation
            sm.update_echo(ECHO,bar,echo_value_label,ttkb.CENTER)

        # add padding for each widget in the middle frame
        for widget in parent.winfo_children():
            widget.grid(padx = 10, pady = 10)
    else:
        Middle_Frame.configure(height = 0, width=DF_width)

def ViewBottomFrame(parent):
    global BtF_height, bot_show
    ResetFrame(parent)                                                         # clear the frame
    UpdateFrameStauts()
    if top_show and mid_show:   # if all widgets are selected
        BtF_height = int(DF_height * 0.3)       # Middle frame in dashboard frame height
    elif top_show and not mid_show:             # if top frame is selected but not middle frame
        BtF_height = int(DF_height * 0.35)      # Middle frame in dashboard frame height
    elif not top_show and mid_show:             # if middle frame is selected but not top frame
        BtF_height = int(DF_height * 0.5)
    else:                                       # if only middle frame is selected
        BtF_height = int(DF_height)             # Top frame in dashboard frame height
    # subsections of dashboard frame
    # setting up widget width
    wid_count = 0
    wid_count = (wid_count + 1) if speed_show.get() == 'Y' else wid_count
    wid_count = (wid_count + 1) if rpm_show.get() == 'Y' else wid_count
    wid_count = (wid_count + 1) if rudder_show.get() == 'Y' else wid_count
    # bwidth = DF_width//(1.14*wid_count+0.000001)
    if wid_count ==0 or wid_count == 1:
        bwidth = DF_width * 0.9
    elif wid_count == 2:
        bwidth = DF_width * 0.44
    else:
        bwidth = DF_width//3.45
    Bottom_Frame.configure(height = BtF_height, width=DF_width)
    if bot_show:
        # subsections of dashboard frame 
        wid_height = BtF_height // 1.2
        
        # SPEED
        if speed_show.get() == 'Y':
            SPEED = ttkb.Frame(parent,                     # create a frame for speed
                            height = wid_height, 
                            width = bwidth, 
                            style = 'Dsh.TFrame', 
                            relief = "solid")
            SPEED.grid(row = 0, column = 0)                # place it on the 1st column
            SPEED.pack_propagate(0)                        # disable resizing
            speed_label = ttkb.Label(SPEED,                # SPEED Label
                                    text='SPEED', 
                                    font=('Roboto', 10),
                                    padding = 5, 
                                    justify = ttkb.CENTER, 
                                    bootstyle = 'success') 
            speed_label.pack()                             # place it
            # setting up meter size
            if bwidth/wid_height> 1:
                metersize = int((wid_height*0.35 + bwidth*0.027))
            else:
                metersize = int((wid_height*0.175 + bwidth*0.1))
            cent = (wid_height - metersize)//25             # padding distance from top broder
            spd_frame = ttkb.Frame(SPEED,                   # create a frame for speed meter
                                   height = wid_height,
                                   width = bwidth*0.9,
                                   style='Dsh.TFrame',)
            spd_frame.pack(pady=abs(cent))                  # add padding distance
            spd_frame.propagate(0)                          # disable resizing
            spdmeter = meter(spd_frame, height= wid_height, width = bwidth*0.9,
                            meter_size = metersize, background='#212b38',
                            total_amount=180, amount_used=100,
                            label='Speed', sub_label='ms')
            # spdmeter.simu()
            sm.update_meter(spdmeter)

        # RPM
        if rpm_show.get() == 'Y':
            RPM = ttkb.Frame(parent, 
                            height = wid_height, 
                            width = bwidth, 
                            style = 'Dsh.TFrame', 
                            relief = "solid")        # create a frame for RPM
            RPM.grid(row = 0, column = 1)            # place it on the 2nd column
            RPM.pack_propagate(0)                    # disable resizing
            rpm_label = ttkb.Label(RPM,              # create RPM label Header
                                padding = 5, 
                                text='RPM', 
                                font=('Roboto', 10),
                                justify = ttkb.CENTER, 
                                bootstyle = 'success')
            rpm_label.pack()                        # place it
            if bwidth/wid_height> 1:
                metersize = int((wid_height*0.35 + bwidth*0.027))
            else:
                metersize = int((wid_height*0.175 + bwidth*0.1))
            cent = (wid_height - metersize)//25             # padding distance from top broder
            rpm_frame = ttkb.Frame(RPM,                   # create a frame for speed meter
                                   height = wid_height,
                                   width = bwidth*0.9,
                                   style='Dsh.TFrame')
            rpm_frame.pack(pady=abs(cent))                  # add padding distance
            rpm_frame.propagate(0)                          # disable resizing
            rpmmeter = meter(rpm_frame, height= wid_height, width = bwidth*0.9,
                            meter_size = metersize, background='#212b38',
                            total_amount=1150, amount_used=2600,
                            label='RPM', sub_label='rpm', active_color='#006699')
            # rpmmeter.simu()
            sm.update_meter(rpmmeter)

        # rudder
        if rudder_show.get() == 'Y':
            RUDDER = ttkb.Frame(parent,                                            # create a frame for compass
                                height = wid_height, 
                                width = bwidth, 
                                style = 'Dsh.TFrame', 
                                relief = "solid")
            RUDDER.grid(row = 0, column = 2)                                       # place it on the 3rd column
            RUDDER.pack_propagate(0)                                               # disable resizing
            RUDDER_label = ttkb.Label(RUDDER, 
                                    text='RUDDER', 
                                    font=('Roboto', 10),
                                    padding = 5, 
                                    justify = ttkb.CENTER, 
                                    bootstyle = 'success')
            RUDDER_label.pack()                                                    # place it

            Rudder_canvas = Canvas(RUDDER,                                        # create canvas for drawing
                                   width = bwidth-10, height= wid_height-40)      
            Rudder_canvas.configure(background = '#212b38')                       # set background color
            Rudder_canvas.pack()                                                  # just place canvas on the WIND frame
            #center and radius of the circle
            rud_center_x = bwidth//2
            rud_center_y = wid_height//10
            rud_r_factor = bwidth/wid_height
            if rud_r_factor > 1:
                Rud_radius = (bwidth*0.04) + (wid_height*0.35)
            else:
                Rud_radius = (bwidth*0.2) + (wid_height*0.09)
            #add the tick marks and cardinal directions
            oval_radius = Rud_radius*0.075
            for i in range(18,37):
                rud_angle = i*10*math.pi/180 #convert degrees to radian
                tick_length = 15 if i%3==0 else 6
                x11 = rud_center_x + math.cos(rud_angle) * (Rud_radius - tick_length)
                y11 = rud_center_y - math.sin(rud_angle) * (Rud_radius - tick_length)
                x21 = rud_center_x + math.cos(rud_angle) * Rud_radius
                y21 = rud_center_y - math.sin(rud_angle) * Rud_radius
                Rudder_canvas.create_line(x11, y11, x21, y21, fill = 'white', width = 3)
                if i == 18:
                    Rudder_canvas.create_text(rud_center_x + Rud_radius + 20, rud_center_y, 
                                              text="+60°", fill="white")
                elif i == 27:
                    Rudder_canvas.create_text(rud_center_x, rud_center_y + Rud_radius + 10, 
                                            text="0°", fill="white")
                elif i == 0 or i == 36 - 1:
                    Rudder_canvas.create_text(rud_center_x - Rud_radius - 20, rud_center_y,
                                              text="-60°", fill="white")
            
            Rudder_canvas.create_text(rud_center_x-Rud_radius-20,rud_center_y+110, text='P', fill='white')
            Rudder_canvas.create_text(rud_center_x+Rud_radius+20,rud_center_y+110, text='S', fill='white')
            sm.update_rudder(Rudder_canvas, oval_radius, Rud_radius, rud_center_x, rud_center_y)

        # add padding for each widget in bottom frame
        for widget in parent.winfo_children():
            widget.grid(padx = 10, pady = 10)
    else:
        Bottom_Frame.configure(height = 0, width=DF_width)

def CreateTF(): 
    '''
        This function create dashboard UI.
    '''
    ViewTopFrame(Top_Frame)
    ViewMiddleFrame(Middle_Frame)
    ViewBottomFrame(Bottom_Frame)

CreateTF()              # draw dashboard UI
root.mainloop()         # add mainloop, otherwise nth will appear