import matplotlib.pyplot as plt #importação da biblioteca matplotlib, é necessário que esteja instalado
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import data, img_as_float, io
from skimage.util import invert

image = io.imread('images/4.jpg')
image = img_as_float(image)
image = invert(image)

chull = convex_hull_image(image)
chull = chull.astype(np.float32) #convert to float32 for aplication example extern
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].set_title('Original Picture')
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_axis_off()

ax[1].set_title('Transformed picture')
ax[1].imshow(chull, cmap=plt.cm.gray)
ax[1].set_axis_off()

plt.tight_layout()
plt.show()