from Tkinter import *
from PIL import ImageTk, Image
import utils
import filters

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



    path = 'images/image3.jpg'

    img = ImageTk.PhotoImage(Image.open(path))

    img_cv2 = utils.read_image(path)

    panel = Label(w, image=img)

    # img2_cv2 = filters.grey_scale(img = img_cv2)
    # img2_cv2 = filters.brightness(img = img_cv2, brightness=50)
    img2_cv2 = filters.one_channel(img = img_cv2, channel = 'G')
    # img2_cv2 = filters.high_contrast(img = img_cv2)
    # img2_cv2 = filters.identity(img = img_cv2)

    img2_cv2 = utils.swap_rgb(img2_cv2)

    img2 = Image.fromarray(img2_cv2)
    img2 = ImageTk.PhotoImage(img2)

    panel2 = Label(w, image=img2)

    panel.pack(side = "left")

    panel2.pack(side = "right")

    w.mainloop()


if __name__ == '__main__':
    main()
