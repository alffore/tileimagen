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
import argparse
import glob
import pickle

import utiles_bd as ubd
import utiles_img as uimg
import utiles_html as uhtml
import utiles_archivos as uarch

tHILOS = 4

tamxPx = 0
tamyPx = 0

aHistogramas = []
aImagenes = []


def procesaImagen(hilo):
    global aImagenes
    global tHILOS

    datosimg = {}

    for index in range(hilo, len(aImagenes), tHILOS):
        img = uimg.recuperaImagenSIC(aImagenes[index][0])
        datosimg['id'] = aImagenes[index][0]
        datosimg['histo'] = uimg.analizaHisto(img)
        datosimg['shape'] = img.shape
        uarch.guardaDI(datosimg)
        print(hilo, index, aImagenes[index])
    return


def comparaHistogramas(dimg):
    uimg.ajusteTam()
    return


if __name__ == '__main__':
    start = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--imagen", required=True, help='Imagen origen')
    ap.add_argument("-cx", "--cortex", required=True, help='partes X')
    ap.add_argument("-cy", "--cortey", required=True, help='partes Y')
    ap.add_argument("-o", "--output", required=True, help='Archivo de salida del html')
    ap.add_argument("-c", "--cachedir", required=False, help="Ruta de path del cache", default='./cache/')

    args = vars(ap.parse_args())

    archivo_target = args['imagen']
    uimg.cargaImagen(archivo_target)

    proc_list = []

    aImagenes = ubd.recuperaTodasImgSIC()
    print(f'total imagenes {len(aImagenes)}')

    with multiprocessing.Manager() as manager:

        for i in range(tHILOS):
            p = multiprocessing.Process(target=procesaImagen, args=(i,))
            p.start()
            proc_list.append(p)

        for p in proc_list:
            p.join()

    print(f'Termino en {round(time.perf_counter() - start, 2)} segundos')
