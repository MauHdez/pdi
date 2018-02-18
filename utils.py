import cv2
from Tkinter import *
from PIL import ImageTk, Image
import numpy as np
import filters
# import matplotlib.pyplot as plt

FILE_OPTIONS = ['Cargar imagen', 'Guardar imagen', 'Salir']
FILTER_OPTIONS = ['Escala de grises', 'Rojo', 'Verde', 'Azul', 'Brillo', 'Alto contraste']

def read_image(path = 'images/image3.jpg'):
    img = cv2.imread(path)
    return img

def swap_rgb(img = None):
    if img.any():
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return None

def cv2_to_PIL(cv2_img):
    if cv2_img.any():
        cv2_img = swap_rgb(cv2_img)
        cv2_img = Image.fromarray(cv2_img)
        cv2_img = ImageTk.PhotoImage(cv2_img)
    return cv2_img

def toImage(cv2_img):
    if cv2_img.any():
        cv2_img = swap_rgb(cv2_img)
        cv2_img = Image.fromarray(cv2_img)
    return cv2_img

def toCV2(pil_image):
    pil_image = pil_image.convert('RGB')
    open_cv_image = np.array(pil_image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image

def rgb_component_aux():

    ret_value = {}
    r = IntVar()
    g = IntVar()
    b = IntVar()

    def get_rgb():
        root = Toplevel()
        root.wm_title("Componente RGB")
        red = Scale(root, from_=-126,to=127, orient="horizontal",
                    label="Rojo", variable=r)
        red.pack()
        green = Scale(root, from_=-126,to=127, orient="horizontal",
                    label="Verde", variable=g)
        green.pack()
        blue = Scale(root, from_=-126,to=127, orient="horizontal",
                    label="Azul", variable=b)
        blue.pack()
        button = Button(root, text="Aceptar", command=lambda : aux(r,g,b,root))
        button.pack()
        mainloop()


    def aux(r, g, b,root):
        ret_value = {'r':r.get(),'g':g.get(),'b':b.get()}
        root.destroy()
        return ret_value

    get_rgb()

# def open_image():
#     return filedialog.askopenfilename()
