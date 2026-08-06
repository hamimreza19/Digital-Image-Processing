import numpy as np
from PIL import Image

# Create a 5x5 grayscale image array
array = np.array([
    [0, 50, 100, 150, 200],
    [50, 100, 150, 200, 255],
    [100, 150, 200, 255, 200],
    [150, 200, 255, 200, 100],
    [200, 255, 200, 100, 50]
], dtype=np.uint8)

# Convert array to image
img = Image.fromarray(array)

# Save image
img.save("tiger.jpg")

# Display image
img.show()