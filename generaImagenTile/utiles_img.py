import requests
import cv2
import numpy as np


def analizaHisto(imagen):
    """
    Analiza el histograma de imagenes
    :param imagen:
    :return:
    """
    hist = cv2.calcHist([imagen], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist


def recuperaImagenSIC(id):
    """
    Función que recupera una imagen del SIC via su URL en Internet
    :param id:
    :return:
    """
    url = f'http://sic.gob.mx/images/{id}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        file = open(f'/tmp/{id}', "wb")
        file.write(response.content)
        file.close()
        return cv2.cvtColor(cv2.imread(f'/tmp/{id}'), cv2.COLOR_BGR2RGB)
    return None


def ajusteTam(imagen, tamx, tamy):
    """

    :param imagen:
    :param tamx:
    :param tamy:
    :return:
    """
    return


def seccionaImagen(imagen, partesx, partesy):
    """
    Función que fracciona una imagen regresa arreglo de fragmentos con histogramas
    :param imagen:
    :param partesx:
    :param partesy:
    :return:
    """
    return


def cargaImagen(archivo):
    """

    :param archivo:
    :return:
    """
    imagen = cv2.imread(archivo)
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
