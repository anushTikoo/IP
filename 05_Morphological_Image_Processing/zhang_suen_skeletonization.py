import numpy as np
import matplotlib.pyplot as plt
# ----

img = np.zeros((100, 100), dtype=np.uint8)
img[20:80, 45:55] = 1
img[45:55, 20:80] = 1
# ----

def zhang_suen_thinning(image):
    skeleton = image.copy()
    h, w = skeleton.shape

    while True:
        to_delete = []
        # Step 1
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if skeleton[i, j] == 0:
                    continue
                p = [skeleton[i - 1, j], skeleton[i - 1, j + 1], skeleton[i, j + 1], skeleton[i + 1, j + 1],
                     skeleton[i + 1, j], skeleton[i + 1, j - 1], skeleton[i, j - 1], skeleton[i - 1, j - 1]]
                b = sum(p)
                a = sum((p[k] == 0 and p[(k + 1) % 8] == 1) for k in range(8))
                if 2 <= b <= 6 and a == 1 and (p[0] * p[2] * p[4] == 0) and (p[2] * p[4] * p[6] == 0):
                    to_delete.append((i, j))
        for i, j in to_delete:
            skeleton[i, j] = 0
        changed = len(to_delete) > 0

        # Step 2
        to_delete = []
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if skeleton[i, j] == 0:
                    continue
                p = [skeleton[i - 1, j], skeleton[i - 1, j + 1], skeleton[i, j + 1], skeleton[i + 1, j + 1],
                     skeleton[i + 1, j], skeleton[i + 1, j - 1], skeleton[i, j - 1], skeleton[i - 1, j - 1]]
                b = sum(p)
                a = sum((p[k] == 0 and p[(k + 1) % 8] == 1) for k in range(8))
                if 2 <= b <= 6 and a == 1 and (p[0] * p[2] * p[6] == 0) and (p[0] * p[4] * p[6] == 0):
                    to_delete.append((i, j))
        for i, j in to_delete:
            skeleton[i, j] = 0
        changed = changed or (len(to_delete) > 0)

        if not changed:
            break
    return skeleton

skeleton = zhang_suen_thinning(img)
# ----

plt.figure(figsize=(8, 4))
plt.subplot(121); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original Shape\"); plt.axis(\"off\")
plt.subplot(122); plt.imshow(skeleton, cmap=\"gray\"); plt.title(\"Zhang-Suen Skeleton\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n