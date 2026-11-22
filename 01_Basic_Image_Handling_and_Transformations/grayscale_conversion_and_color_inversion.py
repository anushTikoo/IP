import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.savefig("images/output_grayscale.png")
plt.close()
# ----

inverted_img = 255 - img_rgb
plt.imshow(inverted_img)
plt.title("Inverted Image")
plt.axis('off')
plt.savefig("images/output_inverted.png")
plt.close()

cv2.imwrite('images/gray_output.jpeg', gray_img)
print("Processed image saved as gray_output.jpeg")
# ----
