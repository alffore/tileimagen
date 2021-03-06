"""
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagenes/90665.jpeg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    print(histr)
    print(type(histr))
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
