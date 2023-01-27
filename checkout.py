import tkinter as tk
import random
from Server.db import Check_out
def Check_Out():
    window2 = tk.Tk()
    window2.geometry("500x500")
    l_to_c_out = tk.Label(window2, text="Or Check-Out a customer")
    l_to_c_out.pack()
    c_out_name_entry = tk.Entry(window2, width=40)
    c_out_name_entry.pack()
    c_out_name_entry.insert(0, 'Full Name')
    c_out_room_entry = tk.Entry(window2)
    c_out_room_entry.pack()
    c_out_room_entry.insert(0, 'Room No.')
    def check_out():
        name = c_out_name_entry.get()
        room = int(c_out_room_entry.get())
        Check_Out(room, name)
        popup = tk.Tk()
        label1 = tk.Label(popup, text="Customer succesfully checked-out")
        label1.pack()
        b1 = tk.Button(popup, text="Okay", command = popup.destroy)
        b1.pack()
        popup.mainloop()
    check_out = tk.Button(window2, text="Check-Out", command=check_out)
    check_out.pack()

    btn2 = tk.Button(window2, text="Back to home", command=window2.destroy)
    btn2.pack()
    window2.mainloop()
