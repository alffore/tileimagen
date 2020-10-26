"""
Prueba para obtencion de histograma

"""
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt


# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = skimage.io.imread(fname=sys.argv[1], as_gray=True)


# display the image
#viewer = skimage.viewer.ImageViewer(image)
#viewer.show()

# tuple to select colors of each channel line
colors = ("r", "g", "b")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id], bins=256, range=(0, 256)
    )
    plt.plot(bin_edges[0:-1], histogram, color=c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()