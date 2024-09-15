import matplotlib.pyplot as plt
from skimage.morphology import convex_hull_image
from skimage import io, img_as_float
from skimage.util import invert

#specify the path to image file
image_path = 'images/2.png'

# read the image from the file
img = io.imread(image_path, as_gray=True)

#invert the image
# img = invert(img)

# Ensure the image is binary (black and white)
# image = img > 0

#comput the convex hull
chull = convex_hull_image(img)

# display the results
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].set_title('Original Picture')
ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_axis_off()

ax[1].set_title('Trransformed Picture')
ax[1].imshow(chull, cmap=plt.cm.gray)
ax[1].set_axis_off()

plt.tight_layout()
plt.show()
