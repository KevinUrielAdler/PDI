import cv2
import numpy as np
from matplotlib import pyplot as plt


imagenEntrada='CALLEBASURA.jpg' 
imagenSalida= imagenEntrada.replace('.jpg', '_Filtro_Media.jpg')

def filtro_media(imagen, tamaño_ventana):
    # Aplicar el filtro de media utilizando la función cv2.blur
    imagen_filtrada = cv2.blur(imagen, (tamaño_ventana, tamaño_ventana))
    return imagen_filtrada

# Cargar la imagen
imagen = cv2.imread(imagenEntrada, cv2.IMREAD_GRAYSCALE)

# Definir el tamaño de la ventana (por ejemplo, 3x3)
tamaño_ventana = 3

# Aplicar el filtro de media
imagen_filtrada = filtro_media(imagen, tamaño_ventana)

# Guardar la imagen filtrada
cv2.imwrite(imagenSalida, imagen_filtrada)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(imagen, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Imagen Filtrada (Media)')
plt.imshow(imagen_filtrada, cmap='gray')
plt.show()
