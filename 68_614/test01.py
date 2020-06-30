import os
from PIL import Image
import matplotlib.pyplot as plt

plt.ion()
for i in os.listdir("image"):
    img = Image.open(os.path.join("image/",i))#join将两个路径拼接在一起
    plt.cla()
    plt.imshow(img)
    plt.pause(1)
plt.ioff()
plt.show()