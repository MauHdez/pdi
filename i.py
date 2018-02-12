import Tkinter as tk
from PIL import ImageTk, Image
import time


root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("images/image.jpg"))
panel = tk.Label(root)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open('images/image3.jpg'))
    panel.configure(image=img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()
