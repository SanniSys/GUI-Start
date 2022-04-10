import tkinter as tk

# create main-window object
window = tk.Tk()
window.title("My Title")  # Set a title for main Window
window.geometry("800x400")  # Set width x height
window.minsize(width=250, height=250)  # cannot change window to below value
# window.maxsize(width=400, height=800)
# window.resizable(width=False, height=False) # changes possible depending on True/False

# label widged:
# create label in main window, bg for background fg = foreground
label_greet = tk.Label(window, text='Welcome!', bg="red")
label_greet2 = tk.Label(window, text='Welcome, my friend!', bg="green")

# Layout-manager, pack grid or place
# pack does a lot of things automatically....
label_greet.pack(fill="x")  # every object has to be added
label_greet2.pack(side="bottom", expand=True, fill="y")  # expand uses max space
# fill= "x" / "y" / "both"
# side="top"(standart) / "bottom" / "left" / "right"

# Eventloop checking for occurring events on window
window.mainloop()
