import cv2
import numpy as np
from matplotlib import pyplot as plt

def filtro_mediana(imagen, tamaño_ventana):
    # Aplicar el filtro de mediana utilizando la función cv2.medianBlur
    imagen_filtrada = cv2.medianBlur(imagen, tamaño_ventana)
    return imagen_filtrada

def filtro_minimo(imagen, tamaño_ventana):
    # Aplicar el filtro de mínimo utilizando la función cv2.erode
    kernel = np.ones((tamaño_ventana, tamaño_ventana), np.uint8)
    imagen_filtrada = cv2.erode(imagen, kernel)
    return imagen_filtrada

def filtro_maximo(imagen, tamaño_ventana):
    # Aplicar el filtro de máximo utilizando la función cv2.dilate
    kernel = np.ones((tamaño_ventana, tamaño_ventana), np.uint8)
    imagen_filtrada = cv2.dilate(imagen, kernel)
    return imagen_filtrada

# Cargar la imagen
imagen = cv2.imread('AreasVerdes.png', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print("Error al cargar la imagen.")
    exit()

# Definir el tamaño de la ventana (por ejemplo, 3x3)
tamaño_ventana = 3

# Aplicar los filtros no lineales
imagen_mediana = filtro_mediana(imagen, tamaño_ventana)
imagen_minimo = filtro_minimo(imagen, tamaño_ventana)
imagen_maximo = filtro_maximo(imagen, tamaño_ventana)

# Guardar las imágenes filtradas
cv2.imwrite('imagen_mediana.jpg', imagen_mediana)
cv2.imwrite('imagen_minimo.jpg', imagen_minimo)
cv2.imwrite('imagen_maximo.jpg', imagen_maximo)

# Mostrar la imagen original y las imágenes filtradas
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.title('Imagen Original')
plt.imshow(imagen, cmap='gray')
plt.subplot(2, 2, 2)
plt.title('Imagen Filtrada (Mediana)')
plt.imshow(imagen_mediana, cmap='gray')
plt.subplot(2, 2, 3)
plt.title('Imagen Filtrada (Mínimo)')
plt.imshow(imagen_minimo, cmap='gray')
plt.subplot(2, 2, 4)
plt.title('Imagen Filtrada (Máximo)')
plt.imshow(imagen_maximo, cmap='gray')
plt.show()
