import random 
import math
import datetime

# create a function to draw the triangle
def triangle(angle, center_x, center_y, radius, tri_size, canvas, tri):  
            # convert degrees to radians
            angle = angle * math.pi / 180  
            # calculate the coordinates of the triangle
            tri_x = center_x + math.cos(angle) * (radius + 20)
            tri_y = center_y - math.sin(angle) * (radius + 20)
            tri_points_new = [
            tri_x + tri_size * math.cos(angle + math.pi/2),
            tri_y - tri_size * math.sin(angle + math.pi/2),
            tri_x + tri_size * math.cos(angle - math.pi/2),
            tri_y - tri_size * math.sin(angle - math.pi/2),
            tri_x - tri_size * math.cos(angle),
            tri_y + tri_size * math.sin(angle)
            ]
            # draw the triangle
            canvas.coords(tri,tri_points_new)

def update_wind_direction_speed(frame, center_x, center_y, radius, tri_size, canvas, tri, Direction, Speed):
            # generate a random angle between 0 and 360 degrees
            angle = random.randint(0, 360)
            dangle = 450 - angle 
            triangle(dangle, center_x, center_y, radius, tri_size, canvas, tri)  # call the triangle() function with the random angle
            if dangle == 0 or angle == 360:
               wind_direction = 'N'
            elif 0 < angle < 90:
                wind_direction = 'NE'
            elif angle == 90:
                wind_direction = 'E'
            elif 90 < angle < 180:
                wind_direction = 'SE'
            elif angle == 180:
                wind_direction = 'S'
            elif 180 < angle < 270:
                wind_direction = 'SW'
            elif angle == 270:
                wind_direction = 'W'
            elif 270 < angle < 360:
                wind_direction = 'NW'
            canvas.itemconfig(Direction, 
                                    text=f"Direction: {int(angle)}° {wind_direction}", 
                                    fill = "#ffbf18", font=('Roboto', 10, 'bold'))
            # wind speed
            wind_speed = random.randint(0, 150)
            canvas.itemconfig(Speed, 
                                    text=f"Speed: {wind_speed} Kn", 
                                    fill = "#ffbf18", font=('Roboto', 10, 'bold'))
            frame.after(5000, update_wind_direction_speed, frame, center_x, center_y, radius, tri_size, canvas, tri, Direction, Speed) 

def update_gyro(frame, center_x, center_y, radius, tri_size, canvas, tri, label):
            # generate a random angle between 0 and 360 degrees
            angle = random.randint(0,360)
            dangle = 450-angle
            triangle(dangle, center_x, center_y, radius, tri_size, canvas, tri)  # call the triangle() function with the random angle
            canvas.itemconfig(label, 
                              text=f"{abs(angle)}°", 
                              fill = "#ffbf18", font=('Roboto', 10))
            # wind speed
            frame.after(5000, update_gyro, frame, center_x, center_y, radius, tri_size, canvas, tri, label) 

def update_datetime(frame, mydate, mytime, position):
            # get current date and time
            date_time = datetime.datetime.now()                                     
            mydate.config(text = date_time.strftime('%x'))
            mytime.config(text = date_time.strftime('%X'))
            # five seconds delay
            frame.after(1000, update_datetime, frame, mydate, mytime, position)
    
def update_gps(frame, label, position):
            # generate random gps
            gps_value =(str(random.randint(0,360))+'° '+str(round(random.random()*10,2))+"'"+' N'+'\n'
                        +str(random.randint(0,360))+'° '+str(round(random.random()*10,3))+"'"+' W')
            label.config(text= gps_value,
                         padding = 1, 
                         font=('Roboto', 20, 'bold'),
                         justify = position,
                         foreground = '#ffbf18',
                         background= '#212b38')
            # five seconds delay
            frame.after(5000, update_gps, frame, label, position)

def update_sog(frame, label, position):
            # generate random kn
            sog_value =str(round(random.randint(0,20) + random.random(),1))
            label.config(text= sog_value+'kn',
                         padding = 1, 
                         font=('Roboto', 16, 'bold'),
                         justify = position,
                         wraplength = 120,
                         foreground = '#ffbf18',
                         background= '#212b38')
            # five seconds delay
            frame.after(5000, update_sog, frame, label, position)

def update_COG(frame, label, position):
            # generate random kn
            COG_value =str(random.randint(50,200))
            label.config(text= COG_value+'°',
                         padding = 1, 
                         font=('Roboto', 16, 'bold'),
                         justify = position,
                         wraplength = 120,
                         foreground = '#ffbf18',
                         background= '#212b38')
            # five seconds delay
            frame.after(5000, update_COG, frame, label, position)

def delete_arrow(canvas, s_y, min_x, max_x, width, height, tag):
    canvas.delete(tag[0])
    canvas.delete(tag[1])
    update_compass(canvas, s_y, min_x, max_x, width, height)

def update_compass(canvas, s_y, min_x, max_x, width, height):
    rudder_val = random.randint(-60,60)
    slope = 120/(max_x - min_x)
    x_point = (rudder_val +60)/slope + min_x
    if width/height >1:
        h = height * 0.15
        w = width * 0.02
    else:
        h = height * 0.035
        w = width * 0.05
    canvas.create_polygon((x_point, s_y, 
                           x_point-w, s_y+h,
                           x_point+w, s_y+h,
                           x_point, s_y),fill="#ffbf18", outline="#ffbf18", width = 2,
                           tags = 'arrow')
    canvas.create_text((min_x+max_x)*0.495, s_y+h+15, text=str(rudder_val)+'°', fill = "#ffbf18", font=('Roboto', 13),tags='deg')
    canvas.after(5000, delete_arrow, canvas, s_y, min_x, max_x, width, height, ['arrow','deg'])

def delete_needle(canvas, width, radius, center_x, center_y, tags):
    for tag in tags:
        canvas.delete(tag)
    update_rudder(canvas, width, radius, center_x, center_y)

def update_rudder(canvas, width, radius, center_x, center_y):
    rudder_value = random.randint(-60,60)
    dangle = 1.5*(rudder_value + 60) + 180
    rangle = dangle * math.pi/180
    tri_x = center_x + math.cos(rangle) * (radius - 20)
    tri_y = center_y - math.sin(rangle) * (radius - 20)
    tan_x1 = center_x + math.cos(rangle+1.8) * (radius-10) * 0.05 + width/10
    tan_y1 = center_y - math.sin(rangle+1.8) * (radius-10) * 0.05 + width/10
    tan_x2 = center_x + math.cos(rangle-1.8) * (radius-10) * 0.05 + width/10
    tan_y2 = center_y - math.sin(rangle-1.8) * (radius-10) * 0.05 + width/10
    # canvas.create_line(center_x,center_y, tri_x, tri_y)
    tri_points = [tri_x, tri_y,
                  tan_x1, tan_y1,
                  tan_x2, tan_y2]
    canvas.create_polygon(tri_points, fill="#ffbf18", outline="white", width = 2, tags='needle')
    canvas.create_oval(center_x-width, center_y-width, center_x+width, center_y+width,fill='white', tags='oval')
    canvas.create_text(center_x, center_y+radius+30,
                       text = str(rudder_value)+'°', fill="#ffbf18", font=('Roboto', 15), tags='label')
    canvas.after(5000, delete_needle, canvas, width, radius, center_x, center_y, ['needle','oval','label'])

def update_echo(frame, widget, label, position):
    # generate random speed
    echo_value = random.randint(0, 600)
    label.config(text= str(echo_value) + ' m',
                justify = position,)
    widget.config(value=echo_value)
    # widget.setvar(name='value', value=echo_value)
    # use after method to delay the execute of 5 seconds 
    frame.after(5000, update_echo, frame, widget, label, position)

def update_meter(meter):
    val = random.randint(1,meter.total_amount)
    meter.set_amount_used(val)
    meter.master.after(5000, update_meter, meter)