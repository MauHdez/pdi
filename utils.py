import cv2
# import numpy as np
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
