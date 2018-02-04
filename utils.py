import cv2
# import numpy as np
# import matplotlib.pyplot as plt

FILE_OPTIONS = ['Cargar imagen', 'Guardar imagen', 'Salir']
FILTER_OPTIONS = ['Escala de grises', 'Rojo', 'Verde', 'Azul', 'Brillo', 'Alto contraste']

def read_image(path = 'image.jpg'):
    img = cv2.imread(path)
    return img
