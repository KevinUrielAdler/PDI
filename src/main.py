from utils import leer_bmp, guardar_imagen, obtener_histograma, graficar_histograma
from manejoHistograma import expansion_histograma, contraccion_histograma, ecualizar_histograma_exp


def main(img):
    img_path = "./img/"+img+".bmp"
    pixeles_rgb, pixeles_grises, img_en_grises = leer_bmp(img_path)

    # Histograma original
    histograma = obtener_histograma(pixeles_grises, pixeles_rgb, img_en_grises)
    graficar_histograma(histograma)

    # Expansion del histograma
    pixeles_exp, pixeles_exp_color = expansion_histograma(
        pixeles_grises, pixeles_rgb, img_en_grises)
    # Histograma expandido
    histograma = obtener_histograma(
        pixeles_exp, pixeles_exp_color, img_en_grises)
    graficar_histograma(histograma, "expandida")
    # Guardar imagen
    if img_en_grises:
        guardar_imagen(pixeles_exp, img+" exp.bmp")
    else:
        guardar_imagen(pixeles_exp_color, img+" exp.bmp")

    # Contracción del histograma
    pixeles_contr, pixeles_contr_color = contraccion_histograma(
        pixeles_grises, pixeles_rgb, img_en_grises)
    # Histograma contraido
    histograma = obtener_histograma(
        pixeles_contr, pixeles_contr_color, img_en_grises)
    graficar_histograma(histograma, "contraida")
    # Guardar imagen
    if img_en_grises:
        guardar_imagen(pixeles_contr, img+" contr.bmp")
    else:
        guardar_imagen(pixeles_contr_color, img+" contr.bmp")

    # Ecualización del histograma
    pixeles_ecualizados, pixeles_ecualizados_color = ecualizar_histograma_exp(
        pixeles_grises, pixeles_rgb, img_en_grises)
    # Histograma ecualizado
    histograma = obtener_histograma(
        pixeles_ecualizados, pixeles_ecualizados_color, img_en_grises)
    graficar_histograma(histograma, "ecualizada")
    # Guardar imagen
    if img_en_grises:
        guardar_imagen(pixeles_ecualizados, img+" ecualizada.bmp")
    else:
        guardar_imagen(pixeles_ecualizados_color, img+" ecualizada.bmp")


if __name__ == "__main__":
    lista_imagenes = ["Bosque 1", "Bosque 2", "Bosque 3",
                      "Bosque 4", "Bosque 5", "Bosque 6", "Bosque 7"]

    for i in lista_imagenes:
        main(i)
