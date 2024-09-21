import numpy as np
from skimage.morphology import skeletonize
from skimage import io, measure
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage.filters import threshold_otsu


image_path = 'images/4.jpg'

# Read in the external image
image = io.imread(image_path, as_gray=True)

# Apply thresholding to convert the image to binary
thresh = threshold_otsu(image)
binary_image = image > thresh

# Find contours of the object
contours = measure.find_contours(binary_image, 0.8)

# Select the outermost contour
outer_contour = max(contours, key=len)

# Convert outer_contour to integer array
outer_contour = outer_contour.astype(int)

# Create a new image with the outer contour
contour_image = np.zeros_like(binary_image)
contour_image[outer_contour[:, 0], outer_contour[:, 1]] = 1

# Skeletonize the contour image
skeleton = (contour_image)

# Display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(binary_image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('binary image', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()