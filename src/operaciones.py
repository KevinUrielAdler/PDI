import numpy as np


def multiplicacion(imagen1, imagen2):
    # Verificar que ambas imágenes tengan las mismas dimensiones
    if imagen1.shape != imagen2.shape:
        raise ValueError(
            "Las dimensiones de las dos imágenes deben ser iguales.")

    multiplicacion = np.zeros(imagen1.shape, dtype=np.uint32)

    # Realizar la multiplicación elemento a elemento
    multiplicacion = np.multiply(imagen1, imagen2)

    # Saturar los valores para que estén en el rango [0, 255]
    resultado = np.clip(multiplicacion, 0, 255)

    multiplicacionuint8 = resultado.astype(np.uint8)

    return multiplicacionuint8


def invertir(imagen):
    return 255 - imagen
