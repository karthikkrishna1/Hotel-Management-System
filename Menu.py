import tkinter as tk
import random
window = tk.Tk()
window.geometry("750x600")

root = tk.Tk()
tk.geometry("500x500")

Hotel = tk.Label(text = "Hotel")
l = tk.Label(text = "Check-In a customer")
vis_name_entry = tk.Entry(width=40)
vis_name_entry.insert(0, 'Full Name')
win = "check-in"
v_room_type = ""

x = 0
extend = 0

if win == "check-in":

    def callback3(selection):
        global v_room_type
        v_room_type = selection
        print(v_room_type)


        
        

    def out():
        l2.configure()
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

    out = tk.Button(window, text="Out", command= out)
    Hotel.pack()
    tk.Label(window, text="").pack()
    l.pack()
    tk.Label(window, text="").pack()
    vis_name_entry.pack()

    tk.Label(window, text="").pack()
    room_type.pack()
    tk.Label(window, text="").pack()

    l2.pack()
    def change():
        global win
        win = "check-out"
    btn = tk.Button(window, text="Or check-out a customer", command=change)
    btn.pack()
else:
    l_to_c_out = tk.Label(window, text="Or Check-Out a customer")
    l_to_c_out.pack()
    c_out_name_entry = tk.Entry(width=40)
    c_out_name_entry.pack()
    c_out_name_entry.insert(0, 'Full Name')
    c_out_room_entry = tk.Entry()
    c_out_room_entry.pack()
    c_out_room_entry.insert(0, 'Room No.')
    def check_out():
        name = c_out_name_entry.get()
        room = int(c_out_room_entry.get())
        #Karthik db stuff here

        popup = tk.Tk()
        label1 = tk.Label(popup, text="Customer succesfully checked-out")
        label1.pack()
        b1 = tk.Button(popup, text="Okay", command = popup.destroy)
        b1.pack()
        popup.mainloop()
    check_out = tk.Button(window, text="Check-Out", command=check_out)
    check_out.pack()
    def change1():
        win = "check-in"
    btn2 = tk.Button(window, text="Check-In", command=change1)
    btn2.pack()
window.mainloop()