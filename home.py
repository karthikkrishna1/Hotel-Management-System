import tkinter as tk
import random
from checkin import CheckIn
from checkout import Check_Out


root = tk.Tk()
root.geometry("500x500")
Hotel = tk.Label(root, text = "Hotel")
Hotel.pack()
v_room_type = ""
tk.Label(root, text="").pack()
tk.Label(root, text="").pack()
tk.Label(root, text="").pack()
checkin_btn = tk.Button(root, text="Check-in a customer", command=CheckIn)
checkin_btn.pack()
tk.Label(root, text="").pack()
tk.Label(root, text="").pack()
checkout_btn = tk.Button(root, text="Check-out a customer", command=Check_Out)
checkout_btn.pack()

root.mainloop()