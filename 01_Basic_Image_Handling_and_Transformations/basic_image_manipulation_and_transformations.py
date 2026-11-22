import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.savefig("images/output_original.png")
plt.close()

print("Image shape (H, W, Channels): ", img.shape)
print("Image data type: ", img.dtype)
# ----

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.savefig("images/output_grayscale.png")
plt.close()
# ----

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

inverted_img = 255 - img_rgb
plt.imshow(inverted_img)
plt.title("Inverted Image")
plt.axis('off')
plt.savefig("images/output_inverted.png")
plt.close()

cv2.imwrite('images/gray_output.jpeg', gray_img)
print("Processed image saved as gray_output.jpeg")
# ----
