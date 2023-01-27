import tkinter as tk
import random
from Server.db import Check_in

v_room_type = ""

def CheckIn():
    window = tk.Tk()
    window.geometry("750x600")


    
    l = tk.Label(window, text = "Check-In a customer")
    vis_name_entry = tk.Entry(window, width=40)
    vis_name_entry.insert(0, 'Full Name')
    v_room_type = tk.Entry(window, width=20)
    v_room_type.insert(0, "Room Type")

    x = 0
    extend = 0
    def callback3(selection):
        global v_room_type
        v_room_type = selection


        
        

    def out():
        name = vis_name_entry.get()
        print(v_room_type)
        x = Check_in(name, v_room_type)
        l2.configure(text = name + v_room_type)
        
    t = tk.StringVar(window)
    OPTIONS_ROOM_TYPE = [
        "SEA FACING",
        "POOL VIEW",
        "GARDEN VIEW",
        "SUITE", 
    ]
    r_t = tk.StringVar(window)
    r_t.set("room type")
    room_type = tk.OptionMenu(window, r_t,*OPTIONS_ROOM_TYPE, command=callback3)

    l2 = tk.Label(window, text="")
    print(x)
    tk.Label(window, text="").pack()
    l.pack()
    tk.Label(window, text="").pack()
    vis_name_entry.pack()

    tk.Label(window, text="").pack()
    room_type.pack()
    tk.Label(window, text="").pack()

    l2.pack()

    submit = tk.Button(window, text="Submit", command=out)
    submit.pack()

    btn = tk.Button(window, text="Back to home", command=window.destroy)
    btn.pack()

    window.mainloop()
