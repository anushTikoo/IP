import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

resized_img = cv2.resize(img_rgb, (200, 200))
plt.imshow(resized_img)
plt.title("Resized Image (200x200)")
plt.axis('off')
plt.savefig("images/output_resized.png")
plt.close()
# ----

pil_img = Image.open('images/panda.jpeg')

rotated_img = pil_img.rotate(45)
rotated_img.save("images/output_rotated.png")

flipped_img = pil_img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_img.save("images/output_flipped.png")
# ----

cropped_img = img_rgb[50:200, 50:200]
plt.imshow(cropped_img)
plt.title("Cropped Image")
plt.axis('off')
plt.savefig("images/output_cropped.png")
plt.close()
# ----
