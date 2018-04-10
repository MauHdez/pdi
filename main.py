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

        # if original_CV2 is not None:
        #     original_CV2 = None
        #     original_PIL = None

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
    w.configure(background='white')

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

    # Filtros de la tarea 1
    tarea_uno_menu = Menu(filters_menu)

    tarea_uno_menu.add_command(label = "Escala de grises.",
                             command = lambda : reload_filtered_img(w,
                                                            "grey_scale", {}))
    tarea_uno_menu.add_command(label = "Brillo.",
                             command = lambda : reload_filtered_img(w,
                                            "brightness", {"brightness":127}))
    tarea_uno_menu.add_command(label = "Rojo",
                             command = lambda : reload_filtered_img(w,
                                            "one_channel", {'channel':'R'}))
    tarea_uno_menu.add_command(label = "Verde",
                             command = lambda : reload_filtered_img(w,
                                                "one_channel", {'channel':'G'}))
    tarea_uno_menu.add_command(label = "Azul",
                             command = lambda : reload_filtered_img(w,
                                                "one_channel", {'channel':'B'}))
    tarea_uno_menu.add_command(label = "Alto contraste",
                             command = lambda : reload_filtered_img(w,
                                            "high_contrast", {'morsa':True}))
    tarea_uno_menu.add_command(label = "Alto contraste no morsa",
                             command = lambda : reload_filtered_img(w,
                                                        "high_contrast", {}))
    tarea_uno_menu.add_command(label = "Inveso",
                             command = lambda : reload_filtered_img(w,
                                                                "inverse", {}))
    tarea_uno_menu.add_command(label = "Mosaico",
                             command = lambda : reload_filtered_img(w,
                                                        "mosaico", {'size':10}))
    tarea_uno_menu.add_command(label = "Componente RGB",
                             command = lambda : reload_filtered_img(w,
                                                "rgb_component", {}))

    # Filtro de la tarea 3
    tarea_tres_menu = Menu(filters_menu)


    tarea_tres_menu.add_command(label = "Quitar marca de agua",
                             command = lambda : reload_filtered_img(w,
                                                "quitar_marca_de_agua", {}))

    # Filtros tarea 4
    tarea_cuatro_menu = Menu(filters_menu)

    tarea_cuatro_menu.add_command(label = "M a color",
                             command = lambda : reload_filtered_img(w,
                                                "m_a_color", {}))
    # Filtros tarea 4
    tarea_cinco_menu = Menu(filters_menu)

    tarea_cinco_menu.add_command(label = "AT&T",
                             command = lambda : reload_filtered_img(w,
                                                "att", {}))


    filters_menu.add_cascade(label="Tarea 1", menu=tarea_uno_menu)
    filters_menu.add_cascade(label="Tarea 3", menu=tarea_tres_menu)
    filters_menu.add_cascade(label="Tarea 4", menu=tarea_cuatro_menu)

    menu_bar.add_cascade(label="Filtros", menu=filters_menu)

    w.config(menu=menu_bar)

    w.mainloop()


if __name__ == '__main__':
    main()
