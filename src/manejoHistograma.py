import numpy as np


def expansion_histograma(pixeles_grises: np.array, pixeles_rgb: np.array, img_en_grises: bool, max: int = 255, min: int = 0) -> tuple:
    """Función que expande el histograma de una imagen

    Parameters
    ----------
    pixeles_grises : np.array
        Pixeles de la imagen en escala de grises
    pixeles_rgb : np.array
        Pixeles de la imagen a color
    img_en_grises : bool
        Indica si la imagen es a color o en escala de grises
    max : int, optional
        Máximo valor deseado de los pixeles, by default 255
    min : int, optional
        Mínimo valor deseado de los pixeles, by default 0

    Returns
    -------
    tuple
        pixeles_expandidos_grises: np.array
            Pixeles de la imagen en escala de grises con el histograma expandido
        pixeles_expandidos_rgb: np.array
            Pixeles de la imagen a color con el histograma expandido
    """
    pixeles_expandidos_grises = np.zeros(pixeles_grises.shape, dtype=np.uint8)
    # Valor mínimo y máximo de los pixeles en escala de grises
    min_img = np.min(pixeles_grises)
    max_img = np.max(pixeles_grises)
    # Se expande el histograma (Pixeles en escala de grises)
    for i in range(pixeles_grises.shape[0]):
        for j in range(pixeles_grises.shape[1]):
            pixeles_expandidos_grises[i][j] = (
                (pixeles_grises[i][j] - min_img)/(max_img - min_img)) * (max - min) + min
    # Si la imagen es en escala de grises, la función termina aquí
    if img_en_grises:
        return pixeles_expandidos_grises, pixeles_rgb

    pixeles_expandidos_rgb = np.zeros(pixeles_rgb.shape, dtype=np.uint8)
    # Listas con los valores mínimos y máximos de los pixeles por canal de color
    min_img = [np.min(pixeles_rgb[:, :, 0]), np.min(
        pixeles_rgb[:, :, 1]), np.min(pixeles_rgb[:, :, 2])]
    max_img = [np.max(pixeles_rgb[:, :, 0]), np.max(
        pixeles_rgb[:, :, 1]), np.max(pixeles_rgb[:, :, 2])]
    # Se expande el histograma (Pixeles a color)
    for i in range(pixeles_rgb.shape[0]):
        for j in range(pixeles_rgb.shape[1]):
            pixeles_expandidos_rgb[i][j][0] = (
                (pixeles_rgb[i][j][0] - min_img[0])/(max_img[0] - min_img[0])) * (max - min) + min
            pixeles_expandidos_rgb[i][j][1] = (
                (pixeles_rgb[i][j][1] - min_img[1])/(max_img[1] - min_img[1])) * (max - min) + min
            pixeles_expandidos_rgb[i][j][2] = (
                (pixeles_rgb[i][j][2] - min_img[2])/(max_img[2] - min_img[2])) * (max - min) + min

    return pixeles_expandidos_grises, pixeles_expandidos_rgb


def contraccion_histograma(pixeles_grises: np.array, pixeles_rgb: np.array, img_en_grises: bool, max: int = 85, min: int = 170) -> tuple:
    """Función que contrae el histograma de una imagen

    Parameters
    ----------
    pixeles_grises : np.array
        Pixeles de la imagen en escala de grises
    pixeles_rgb : np.array
        Pixeles de la imagen a color
    img_en_grises : bool
        Indica si la imagen es a color o en escala de grises
    max : int, optional
        Máximo valor deseado de los pixeles, by default 85
    min : int, optional
        Mínimo valor deseado de los pixeles, by default 170

    Returns
    -------
    tuple
        pixeles_contraidos_grises: np.array
            Pixeles de la imagen en escala de grises con el histograma expandido
        pixeles_contraidos_rgb: np.array
            Pixeles de la imagen a color con el histograma expandido
    """
    pixeles_contraidos_grises = np.zeros(pixeles_grises.shape, dtype=np.uint8)
    # Valor mínimo y máximo de los pixeles en escala de grises
    min_img = np.min(pixeles_grises)
    max_img = np.max(pixeles_grises)
    # Se contrae el histograma (Pixeles en escala de grises)
    for i in range(pixeles_grises.shape[0]):
        for j in range(pixeles_grises.shape[1]):
            pixeles_contraidos_grises[i][j] = (
                (max - min) / (max_img - min_img)) * (pixeles_grises[i][j] - min_img) + min
    # Si la imagen es en escala de grises, la función termina aquí
    if img_en_grises:
        return pixeles_contraidos_grises, pixeles_rgb

    pixeles_contraidos_rgb = np.zeros(pixeles_rgb.shape, dtype=np.uint8)
    # Listas con los valores mínimos y máximos de los pixeles por canal de color
    min_img = [np.min(pixeles_rgb[:, :, 0]), np.min(
        pixeles_rgb[:, :, 1]), np.min(pixeles_rgb[:, :, 2])]
    max_img = [np.max(pixeles_rgb[:, :, 0]), np.max(
        pixeles_rgb[:, :, 1]), np.max(pixeles_rgb[:, :, 2])]
    # Se contrae el histograma (Pixeles a color)
    for i in range(pixeles_rgb.shape[0]):
        for j in range(pixeles_rgb.shape[1]):
            pixeles_contraidos_rgb[i][j][0] = (
                (max - min) / (max_img[0] - min_img[0])) * (pixeles_rgb[i][j][0] - min_img[0]) + min
            pixeles_contraidos_rgb[i][j][1] = (
                (max - min) / (max_img[1] - min_img[1])) * (pixeles_rgb[i][j][1] - min_img[1]) + min
            pixeles_contraidos_rgb[i][j][2] = (
                (max - min) / (max_img[2] - min_img[2])) * (pixeles_rgb[i][j][2] - min_img[2]) + min

    return pixeles_contraidos_grises, pixeles_contraidos_rgb


def ecualizar_histograma_exp(pixeles_grises: np.array, pixeles_rgb: np.array, img_en_grises: bool, alpha: int = 0.01) -> tuple:
    """Función que ecualiza el histograma de una imagen

    Parameters
    ----------
    pixeles_grises : np.array
        Pixeles de la imagen en escala de grises
    pixeles_rgb : np.array
        Pixeles de la imagen a color
    img_en_grises : bool
        Indica si la imagen es a color o en escala de grises
    alpha : int, optional
        Parámetro de la ecualización, by default 0.01

    Returns
    -------
    tuple
        pixeles_ecualizados_grises: np.array
            Pixeles de la imagen en escala de grises con el histograma ecualizado
        pixeles_ecualizados_rgb: np.array
            Pixeles de la imagen a color con el histograma ecualizado
    """
    pixeles_ecualizados_grises = np.zeros(pixeles_grises.shape, dtype=np.uint8)

    # Parámetros de la ecualización
    max_img = np.max(pixeles_grises)
    c = 255/(np.exp(alpha*max_img)-1)
    # Se ecualiza el histograma (Pixeles en escala de grises)
    for i in range(pixeles_grises.shape[0]):
        for j in range(pixeles_grises.shape[1]):
            pixeles_ecualizados_grises[i][j] = c * \
                (np.exp(alpha * pixeles_grises[i][j])-1)
            # Se ajustan los valores de los pixeles
            if pixeles_ecualizados_grises[i][j] > 255:
                pixeles_ecualizados_grises[i][j] = 255
            if pixeles_ecualizados_grises[i][j] < 0:
                pixeles_ecualizados_grises[i][j] = 0
    # Si la imagen es en escala de grises, la función termina aquí
    if img_en_grises:
        return pixeles_ecualizados_grises, pixeles_rgb

    pixeles_ecualizados_rgb = np.zeros(pixeles_rgb.shape, dtype=np.uint8)
    # Listas con los parámetros de la ecualización por canal de color
    max_img = [np.max(pixeles_rgb[:, :, 0]), np.max(
        pixeles_rgb[:, :, 1]), np.max(pixeles_rgb[:, :, 2])]
    c = [255/(np.exp(alpha*max_img[0])-1), 255 /
         (np.exp(alpha*max_img[1])-1), 255/(np.exp(alpha*max_img[2])-1)]
    # Se ecualiza el histograma (Pixeles a color)
    for i in range(pixeles_rgb.shape[0]):
        for j in range(pixeles_rgb.shape[1]):
            pixeles_ecualizados_rgb[i][j][0] = c[0] * \
                (np.exp(alpha * pixeles_rgb[i][j][0])-1)
            pixeles_ecualizados_rgb[i][j][1] = c[1] * \
                (np.exp(alpha * pixeles_rgb[i][j][1])-1)
            pixeles_ecualizados_rgb[i][j][2] = c[2] * \
                (np.exp(alpha * pixeles_rgb[i][j][2])-1)
            # Se ajustan los valores de los pixeles
            if pixeles_ecualizados_rgb[i][j][0] > 255:
                pixeles_ecualizados_rgb[i][j][0] = 255
            if pixeles_ecualizados_rgb[i][j][0] < 0:
                pixeles_ecualizados_rgb[i][j][0] = 0

            if pixeles_ecualizados_rgb[i][j][1] > 255:
                pixeles_ecualizados_rgb[i][j][1] = 255
            if pixeles_ecualizados_rgb[i][j][1] < 0:
                pixeles_ecualizados_rgb[i][j][1] = 0

            if pixeles_ecualizados_rgb[i][j][2] > 255:
                pixeles_ecualizados_rgb[i][j][2] = 255
            if pixeles_ecualizados_rgb[i][j][2] < 0:
                pixeles_ecualizados_rgb[i][j][2] = 0

    return pixeles_ecualizados_grises, pixeles_ecualizados_rgb


def umbralizar_imagen(pixeles_grises, umbral):
    pixeles_umbralizados_grises = np.zeros(
        pixeles_grises.shape, dtype=np.uint8)

    for i in range(pixeles_grises.shape[0]):
        for j in range(pixeles_grises.shape[1]):
            pixeles_umbralizados_grises[i][j] = 0 if pixeles_grises[i][j] < umbral else 255

    return pixeles_umbralizados_grises
