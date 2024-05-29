import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
from PIL import Image

# Función para aplicar el filtro máximo


def max_filter(image, kernel_size=3):
    # Obtener dimensiones de la imagen
    height, width = image.shape

    # Crear una matriz para almacenar la imagen filtrada
    filtered_image = np.zeros((height, width), dtype=np.uint8)

    # Calcular el radio del kernel (asumiendo que el kernel es cuadrado)
    kernel_radius = kernel_size // 2

    # Aplicar el filtro máximo manualmente
    for y in range(kernel_radius, height - kernel_radius):
        for x in range(kernel_radius, width - kernel_radius):
            # Extraer la región del kernel de la imagen
            region = image[y - kernel_radius:y + kernel_radius + 1,
                           x - kernel_radius:x + kernel_radius + 1]
            # Calcular el máximo valor en la región del kernel y asignarlo al píxel central
            filtered_image[y, x] = np.max(region)

    return filtered_image


def mean_filter(image, kernel_size=3):
    # Obtener dimensiones de la imagen
    height, width = image.shape

    # Crear una matriz para almacenar la imagen filtrada
    filtered_image = np.zeros((height, width), dtype=np.uint8)

    # Calcular el radio del kernel (asumiendo que el kernel es cuadrado)
    kernel_radius = kernel_size // 2

    # Aplicar el filtro máximo manualmente
    for y in range(kernel_radius, height - kernel_radius):
        for x in range(kernel_radius, width - kernel_radius):
            # Extraer la región del kernel de la imagen
            region = image[y - kernel_radius:y + kernel_radius + 1,
                           x - kernel_radius:x + kernel_radius + 1]
            # Calcular el máximo valor en la región del kernel y asignarlo al píxel central
            filtered_image[y, x] = np.mean(region)

    return filtered_image


# # Mostrar la imagen original y las imágenes filtradas en subplots
# plt.figure(figsize=(15, 5))

# plt.subplot(1, 3, 1)
# plt.imshow(image, cmap='gray')
# plt.title('Original')
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(filtered_image_3, cmap='gray')
# plt.title('Filtro Maximo 3x3')
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(filtered_image_7, cmap='gray')
# plt.title('Filtro Maximo 7x7')
# plt.axis('off')

# plt.show()

# def rgb_to_gray(image):
#     # Convertir la imagen a escala de grises
#     return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)


def kirsch_edge_detection(image):
    # Definir las máscaras de Kirsch
    masks = [
        np.array([[-3, -3,  5], [-3,  0,  5], [-3, -3,  5]]),  # Norte (N)
        np.array([[-3,  5,  5], [-3,  0,  5], [-3, -3, -3]]),  # Noreste (NE)
        np.array([[5,  5,  5], [-3,  0, -3], [-3, -3, -3]]),  # Este (E)
        np.array([[5,  5, -3], [5,  0, -3], [-3, -3, -3]]),  # Sureste (SE)
        np.array([[5, -3, -3], [5,  0, -3], [5, -3, -3]]),  # Sur (S)
        np.array([[-3, -3, -3], [5,  0, -3], [5,  5, -3]]),  # Suroeste (SW)
        np.array([[-3, -3, -3], [-3,  0, -3], [5,  5,  5]]),  # Oeste (O)
        np.array([[-3, -3, -3], [-3,  0,  5], [-3,  5,  5]])   # Noroeste (NW)
    ]

    # Obtener las dimensiones de la imagen
    height = image.shape[0]
    width = image.shape[1]

    # Crear una matriz para almacenar los bordes detectados
    edge_image = np.zeros((height, width), dtype=np.uint8)

    # Aplicar cada una de las máscaras de Kirsch
    for mask in masks:
        # Convolucionar la imagen con la máscara
        convolution = np.abs(convolve(image, mask)).astype(np.uint8)
        # Actualizar la imagen de bordes usando el máximo valor absoluto
        np.maximum(edge_image, convolution, edge_image)

    return edge_image


def convolve(image, mask):
    # Obtener las dimensiones de la imagen y la máscara
    height, width = image.shape
    m_height, m_width = mask.shape

    # Calcular el tamaño del borde para asegurarse de que no se desborde
    border = m_height // 2

    # Crear una matriz para almacenar el resultado de la convolución
    result = np.zeros((height, width), dtype=np.int32)

    # Aplicar la convolución
    for y in range(border, height - border):
        for x in range(border, width - border):
            # Obtener la región de la imagen que se convoluciona con la máscara
            region = image[y - border:y + border +
                           1, x - border:x + border + 1]
            # Realizar la convolución y sumar los resultados
            result[y, x] = np.sum(region * mask)

    return result


# # Cargar la imagen
# image = load_image("img1.jpeg")

# # Aplicar el filtro de Kirsch
# edges = kirsch_edge_detection(image)

# # Mostrar la imagen original, la imagen en escala de grises y la imagen con bordes detectados
# plt.figure(figsize=(15, 5))

# plt.subplot(1, 3, 1)
# plt.imshow(image)
# plt.title('Original')
# plt.axis('off')

# plt.subplot(1, 3, 2)
# plt.imshow(rgb_to_gray(image), cmap='gray')
# plt.title('Escala de Grises')
# plt.axis('off')

# plt.subplot(1, 3, 3)
# plt.imshow(edges, cmap='gray')
# plt.title('Filtro de Kirsch')
# plt.axis('off')

# plt.show()
