"""
Código que lee imagenes del SIC-RENIC y genera una imagen Tiles partiendo de una imagen proporcionada.

1. Lee la imagen propuesta
2. Genera la partición de la imagen
3. Recupera ids e información  de imagen SiC
4. Genera los histogramas y los va guardando en el cache (multihilos)
5. Simultaneamente va comparando con el histograma de la partición y ajusto en el mejor (detemina posición)
6. Genera un HTML con la ubicación de los thumbs


AAFR <alffore@gmail.com>
24 de octubre del 2020
"""
import multiprocessing
import time
import sys

import utiles_bd as ubd
import utiles_img as uimg
import utiles_html

tHILOS = 4

tamxPx = 0
tamyPx = 0

aHistogramas = []
aimagenes = []


def procesaImagen(hilo):
    global aimagenes

    for index in range(i, len(aimagenes), tHILOS):
        img = uimg.recuperaImagenSIC(aimagenes[index][0])
        datosimg = uimg.analizaHisto(img)
        datosimg.append(comparaHistogramas(datosimg))

    return


def comparaHistogramas(dimg):
    uimg.ajusteTam()
    return


if __name__ == '__main__':

    archivo_target = ''
    uimg.cargaImagen(archivo_target)

    proc_list = []

    aimagenes = ubd.recuperaTodasImgSIC()

    with multiprocessing.Manager() as manager:

        for i in range(tHILOS):
            p = multiprocessing.Process(target=procesaImagen, args=(i))
            p.start()
            proc_list.append(p)

        for p in proc_list:
            p.join()
