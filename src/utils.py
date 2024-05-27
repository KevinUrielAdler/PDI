import numpy as np
from PIL import Image

import matplotlib.pyplot as plt


def leer_bmp(img_path: str) -> tuple:
    """Función que lee una imagen en formato bmp y obtiene sus pixeles y pixeles en escala de grises

    Parameters
    ----------
    img_path : str
        Ruta de la imagen

    Returns
    -------
    tuple
        pixeles_rgb: np.array
            Pixeles de la imagen a color
        pixeles_grises: np.array
            Pixeles de la imagen en escala de grises
        img_en_grises: bool
            Indica si la imagen es a color o en escala de grises
    """
    pixeles_rgb = Image.open(img_path)
    pixeles_rgb = np.array(pixeles_rgb)

    alto = pixeles_rgb.shape[0]
    largo = pixeles_rgb.shape[1]

    # Se calculan los pixeles en escala de grises
    pixeles_grises = np.zeros((alto, largo), dtype=np.uint8)
    for i in range(alto):
        for j in range(largo):
            pixeles_grises[i][j] = np.sum(pixeles_rgb[i][j])//3
    # Si la imagen es en escala de grises
    img_en_grises = len(pixeles_rgb.shape) == 2
    if img_en_grises:
        # Los pixeles grises son iguales a los pixeles de la imagen
        pixeles_grises = pixeles_rgb.copy()
        # Se crea una matriz de ceros para los pixeles a color
        pixeles_rgb = np.zeros((alto, largo, 3), dtype=np.uint8)

    return pixeles_rgb, pixeles_grises, img_en_grises


def guardar_imagen(pixeles: np.array, nombre: str) -> None:
    """Función que guarda una imagen en formato bmp

    Parameters
    ----------
    pixeles : np.array
        Pixeles de la imagen (En escala de grises o a color)
    nombre : str
        Nombre de la imagen
    """
    path = "./img/" + nombre
    imagen_ecualizada = Image.fromarray(pixeles)
    imagen_ecualizada.save(path)


def obtener_histograma(pixeles_grises: np.array, pixeles_rgb: np.array, img_en_grises: bool) -> np.array:
    cantidad_canales = 1 if img_en_grises else 4

    histograma = np.zeros((256, cantidad_canales), dtype=np.uint32)

    for i in range(256):
        # Se calcula el histograma para el brillo de la imagen (escala de grises)
        histograma[i][0] = np.sum(pixeles_grises == i)
        if img_en_grises:
            continue
        # Si la imagen es a color se calcula el histograma para cada canal
        histograma[i][1] = np.sum(pixeles_rgb[:, :, 0] == i)
        histograma[i][2] = np.sum(pixeles_rgb[:, :, 1] == i)
        histograma[i][3] = np.sum(pixeles_rgb[:, :, 2] == i)

    return histograma


def graficar_histograma(histograma: np.array, proceso: str = "") -> None:
    """Función que grafica el histograma de una imagen

    Parameters
    ----------
    histograma : np.array
        Histograma de la imagen
    proceso : str, optional
        Proceso al que se sometio la imagen, by default ""
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    # Se grafica el histograma para la escala de grises
    ax.plot(histograma[:, 0], color='gray', label='Grises')
    # Si la imagen es a color se grafica el histograma para cada canal
    if histograma.shape[1] == 4:
        ax.plot(histograma[:, 1], color='red', label='Rojo')
        ax.plot(histograma[:, 2], color='green', label='Verde')
        ax.plot(histograma[:, 3], color='blue', label='Azul')

    ax.set_title('Histograma de la imagen '+proceso)
    ax.set_xlabel('Intensidad de color')
    ax.set_ylabel('Frecuencia')
    ax.legend()
    plt.show()
