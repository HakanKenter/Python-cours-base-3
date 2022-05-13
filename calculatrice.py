# -*- utf-8: python -*-

import tkinter as tk

root = tk.Tk()
root.title("Calculatrice")

e = tk.Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

button_1 = tk.Button(root, text="1", padx=40, pady=20)
button_2 = tk.Button(root, text="2", padx=40, pady=20)
button_3 = tk.Button(root, text="3", padx=40, pady=20)
button_4 = tk.Button(root, text="4", padx=40, pady=20)
button_5 = tk.Button(root, text="5", padx=40, pady=20)
button_6 = tk.Button(root, text="6", padx=40, pady=20)
button_7 = tk.Button(root, text="7", padx=40, pady=20)
button_8 = tk.Button(root, text="8", padx=40, pady=20)
button_9 = tk.Button(root, text="9", padx=40, pady=20)
button_0 = tk.Button(root, text="0", padx=40, pady=20)
button_c = tk.Button(root, text="C", padx=40, pady=20)
button_plus = tk.Button(root, text="+", padx=40, pady=20)
button_moin = tk.Button(root, text="-", padx=40, pady=20)
button_division = tk.Button(root, text="/", padx=40, pady=20)
button_e = tk.Button(root, text="=", padx=40, pady=20)

button_1.grid()

root.mainloop()
