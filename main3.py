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

# Concatena as imagens horizontalmente
top_row = np.hstack((top_half, chull_top))
bottom_row = np.hstack((bottom_half, chull_bottom))

# Concatena as imagens verticalmente
final_image = np.vstack((top_row, bottom_row))

# Exiba a imagem final
plt.imshow(final_image, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

# Salve a imagem final
io.imsave('final_image.png', final_image)