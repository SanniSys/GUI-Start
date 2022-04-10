import tkinter as tk

# create main-window object
window = tk.Tk()

# create label in main window
label_greet = tk.Label(window, text='Welcome!')

label_greet.pack()

window.mainloop()
