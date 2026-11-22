import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
if img is None:
    img = np.full((256, 256, 3), 180, dtype=np.uint8)
    cv2.circle(img, (128, 128), 60, (50, 50, 50), -1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Image shape:", img.shape, "| Data type:", img.dtype)
# ----

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(img_rgb, (200, 200))
# ----

rotated_img = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
flipped_img = cv2.flip(img_rgb, 1)
cropped_img = img_rgb[50:200, 50:200]
inverted_img = 255 - img_rgb
# ----

titles = ["Original", "Grayscale", "Resized (200x200)", "Rotated 90°", "Flipped", "Cropped", "Inverted"]
images = [img_rgb, gray_img, resized_img, rotated_img, flipped_img, cropped_img, inverted_img]

plt.figure(figsize=(14, 6))
for i in range(len(images)):
    plt.subplot(2, 4, i + 1)
    cmap = "gray" if len(images[i].shape) == 2 else None
    plt.imshow(images[i], cmap=cmap)
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
# ----
