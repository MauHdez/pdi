from Tkinter import *
from PIL import ImageTk, Image
import utils

def main():
    w = Tk()
    w.title("filtros")
    w.geometry("1280x720")
    w.configure(background='grey')

    menu_bar = Menu(w)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label = "Cargar imagen.")
    file_menu.add_command(label = "Guardar imagen.")
    file_menu.add_command(label = "Salir.", command = w.quit)

    menu_bar.add_cascade(label="File", menu=file_menu)

    w.config(menu=menu_bar)



    path = 'image.jpg'

    img = ImageTk.PhotoImage(Image.open(path))

    panel = Label(w, image=img)
    panel2 = Label(w, image=img)

    panel.pack(side = "left")

    panel2.pack(side = "right")

    w.mainloop()


if __name__ == '__main__':
    main()
