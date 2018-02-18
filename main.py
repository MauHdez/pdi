from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image
import utils
import filters

original_PIL = None
original_CV2 = None
panel2 = None

def reload_filtered_img(w, filter_to_apply, extras):

    fil = getattr(filters, filter_to_apply)
    filtered_img = fil(original_img = original_CV2, extras = extras)
    if filtered_img.any():
        filtered_img = utils.cv2_to_PIL(filtered_img)
        panel2.configure(image=filtered_img)
        panel2.image = filtered_img

def load_image(w):
    try:
        f = askopenfilename()
        original_img = utils.read_image(f)

        global original_CV2
        original_CV2 = original_img


        original_img = utils.cv2_to_PIL(original_img)

        global original_PIL
        original_PIL = original_img



        panel = Label(w, image=original_img)
        panel.pack(side="left")
    except TypeError as e:
        return

def main():

    w = Tk()
    w.title("filtros")
    w.geometry("1280x720")
    w.configure(background='gray')

    global panel2
    panel2 = Label(w)
    panel2.pack(side='right')

    menu_bar = Menu(w)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label = "Cargar imagen.", command=lambda : load_image(w))
    file_menu.add_command(label = "Guardar imagen.")
    file_menu.add_command(label = "Salir.", command = w.quit)

    menu_bar.add_cascade(label="File", menu=file_menu)

    filters_menu = Menu(menu_bar, tearoff=0)
    filters_menu.add_command(label = "Escala de grises.",
                             command = lambda : reload_filtered_img(w,
                                                            "grey_scale", {}))
    filters_menu.add_command(label = "Brillo.",
                             command = lambda : reload_filtered_img(w,
                                            "brightness", {"brightness":127}))
    filters_menu.add_command(label = "Rojo",
                             command = lambda : reload_filtered_img(w,
                                            "one_channel", {'channel':'R'}))
    filters_menu.add_command(label = "Verde",
                             command = lambda : reload_filtered_img(w,
                                                "one_channel", {'channel':'G'}))
    filters_menu.add_command(label = "Azul",
                             command = lambda : reload_filtered_img(w,
                                                "one_channel", {'channel':'B'}))
    filters_menu.add_command(label = "Alto contraste",
                             command = lambda : reload_filtered_img(w,
                                            "high_contrast", {'morsa':True}))
    filters_menu.add_command(label = "Alto contraste no morsa",
                             command = lambda : reload_filtered_img(w,
                                                        "high_contrast", {}))
    filters_menu.add_command(label = "Inveso",
                             command = lambda : reload_filtered_img(w,
                                                                "inverse", {}))
    filters_menu.add_command(label = "Mosaico",
                             command = lambda : reload_filtered_img(w,
                                                        "mosaico", {'size':25}))
    filters_menu.add_command(label = "Componente RGB",
                             command = lambda : reload_filtered_img(w,
                                                "rgb_component", {}))

    menu_bar.add_cascade(label="Filtros", menu=filters_menu)

    w.config(menu=menu_bar)

    w.mainloop()


if __name__ == '__main__':
    main()
