import matplotlib.pyplot as plt
from skimage.morphology import convex_hull_image
from skimage import io, img_as_float, util
import numpy as np

#specify the path to image file
image_path = 'images/4.jpg'

# Leia a imagem externa
image = io.imread(image_path, as_gray=True)

# Divide a imagem horizontalmente
height, width = image.shape
half_height = height // 2
top_half = image[:half_height, :]
bottom_half = image[half_height:, :]

# inverter a imagem para tornar os objetos brancos
# top_half = util.invert(top_half)
# bottom_half = util.invert(bottom_half)

# Compute a envoltória convexa
chull_top = convex_hull_image(top_half)
chull_bottom = convex_hull_image(bottom_half)

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# ax[0].set_title('Imagem original (top)')
ax[0].imshow(top_half, cmap=plt.cm.gray)
ax[0].set_axis_off()

# ax[1].set_title('Imagem transformada (top)')
ax[1].imshow(chull_top, cmap=plt.cm.gray)
ax[1].set_axis_off()

# ax[2].set_title('Imagem original (bottom)')
ax[2].imshow(bottom_half, cmap=plt.cm.gray)
ax[2].set_axis_off()

# ax[3].set_title('Imagem transformada (bottom)')
ax[3].imshow(chull_bottom, cmap=plt.cm.gray)
ax[3].set_axis_off()

plt.tight_layout()
plt.show()