from Tkinter import *
from PIL import ImageTk, Image
import time


root = Tk()
w = Scale(root, from_=-126,to=127, orient="horizontal")
w.pack()
# img = ImageTk.PhotoImage(Image.open("images/image.jpg"))
# panel = tk.Label(root)
# panel.pack(side="bottom", fill="both", expand="yes")

root.mainloop()
