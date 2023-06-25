import tkinter as tk
import ttkbootstrap as ttkb

MSG = '''
    Thank for using Navis. Navis is a Python GUI application that displays the value
of sensors of a ship. You can customize the list of sensors that are shown on the
dashboard. If you are interested in Navis or find a new bug, you can contact us from
these email addresses.

linyaungzin99@gmail.com
kaungheinhtetycc@gmail.com
aungzawhtetko@gmail.com

Thanks again!'''

def menu(root):
    menubar = tk.Menu(root)          # create Menubar

    # add file menu
    file = tk.Menu(menubar, font=('Roboto',13), tearoff=0)
    menubar.add_cascade(label='File', menu=file, font=('Roboto',13))
    file.add_command(label ='Exit', command = root.destroy)
    
    # Adding Help Menu
    help_ = tk.Menu(menubar, tearoff = 0, font=('Roboto',13))
    menubar.add_cascade(label = 'Help', menu = help_)
    help_.add_command(label ='About Navis', command= lambda: About(root))

    return menubar

def About(root):
    # subwindow = tk.Tk(screenName='About Navis')
    subwindow = tk.Toplevel(root)
    subwindow.geometry('600x300')
    subwindow.configure(background = '#212b38')
    header_frame = ttkb.Frame(subwindow, height=30, width=600)
    header_frame.pack(padx=10,pady=10)
    header_frame.pack_propagate(0)
    header = ttkb.Label(header_frame, text='About Navis',
                        font=("Times", 16, 'bold'))
    header.pack()

    msg_frame = ttkb.Frame(subwindow, height=275, width=600)
    msg_frame.pack(padx=10,pady=10)
    msg_frame.pack_propagate(0)
    msg_label = ttkb.Label(msg_frame,
                           text=MSG,
                           font=('Arial', 12),
                           wraplength=600)
    msg_label.pack()
    subwindow.mainloop()