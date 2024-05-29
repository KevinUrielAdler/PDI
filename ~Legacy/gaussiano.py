import cv2
from matplotlib import pyplot as plt

def filtro_gausiano(imagen, tamaño_ventana, sigma):
    # Aplicar el filtro gaussiano utilizando la función cv2.GaussianBlur
    imagen_filtrada = cv2.GaussianBlur(imagen, (tamaño_ventana, tamaño_ventana), sigma)
    return imagen_filtrada

# Cargar la imagen
imagen = cv2.imread('areaderiesgo.jpeg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print("Error al cargar la imagen.")
    exit()

# Definir el tamaño de la ventana (debe ser impar, por ejemplo, 5x5)
tamaño_ventana = 5

# Definir el sigma para el filtro gaussiano
sigma = 1.0

# Aplicar el filtro gausiano
imagen_filtrada = filtro_gausiano(imagen, tamaño_ventana, sigma)

# Guardar la imagen filtrada
cv2.imwrite('imagen_filtrada_gausiano.jpg', imagen_filtrada)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(imagen, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Imagen Filtrada (Gaussiano)')
plt.imshow(imagen_filtrada, cmap='gray')
plt.show()
