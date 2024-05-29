from utils import leer_bmp, guardar_imagen, obtener_histograma, graficar_histograma
from manejoHistograma import expansion_histograma, contraccion_histograma, ecualizar_histograma_exp, umbralizar_imagen
from filtros import max_filter, mean_filter, kirsch_edge_detection
from operaciones import multiplicacion


def mascara(img):
    img_path = "./img/"+img+".bmp"
    pixeles_rgb, pixeles_grises, img_en_grises = leer_bmp(img_path)

    # Ecualización del histograma
    # pixeles_ecualizados, pixeles_ecualizados_rgb = ecualizar_histograma_exp(
    #     pixeles_grises, pixeles_rgb, img_en_grises)

    # Filtro máximo
    # pixeles_max = max_filter(pixeles_ecualizados, 7)

    # Filtro de Kirsch
    pixeles_kirsch = kirsch_edge_detection(pixeles_grises)

    # Filtro de la media
    pixeles_media = mean_filter(pixeles_kirsch, 3)

    # Umbralizado
    pixeles_umbralizados = umbralizar_imagen(pixeles_media, 127)

    # Filtro de la media
    pixeles_media = mean_filter(pixeles_umbralizados, 3)

    # Umbralizado
    pixeles_umbralizados = umbralizar_imagen(pixeles_media, 127)

    pixeles_finales = pixeles_umbralizados
    pixeles_finales_rgb = 1

    # Guardar imagen
    if img_en_grises:
        guardar_imagen(pixeles_finales, img+" procesada.bmp")
    else:
        guardar_imagen(pixeles_finales_rgb, img+" procesada.bmp")


def pasto(img):
    img_path_1 = "./img/"+img+".bmp"
    img_path_2 = "./img/"+img+" procesada.bmp"

    pixeles_rgb_1, pixeles_grises_1, img_en_grises_1 = leer_bmp(img_path_1)
    pixeles_rgb_2, pixeles_grises_2, img_en_grises_2 = leer_bmp(img_path_2)

    multi = multiplicacion(pixeles_grises_1, pixeles_grises_2)
    multi = 255 - multi

    guardar_imagen(multi, img+" pasto.bmp")


if __name__ == "__main__":
    lista_imagenes = ["Bosque 1", "Bosque 2", "Bosque 3",
                      "Bosque 4", "Bosque 5", "Bosque 6", "Bosque 7"]

    # mascara(lista_imagenes[1])
    # pasto(lista_imagenes[1])
    for i in lista_imagenes:
        mascara(i)
        pasto(i)
