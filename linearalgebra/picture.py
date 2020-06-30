from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('pic.jpg')
img_data = np.array(img)
print(img_data)
print(img_data.shape)
# img.show()

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
