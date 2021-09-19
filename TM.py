import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

full_image = rgb2gray(img.imread("full_image.png"))
sub_image = rgb2gray(img.imread("sub_image.png"))

full_w,full_h = full_image.shape[:2]
sub_w,sub_h = sub_image.shape[:2]

print(full_w,full_h)
print(sub_w,sub_h)

winW = 0
found = False
while winW < full_w - sub_w and found == False:
    winH = 0
    while winH < full_h - sub_h:
        window = full_image[winW:winW+sub_w, winH:winH+sub_h]
        if ssim(sub_image, window) > 0.80:
            found = True
            print("found", ssim(sub_image, window))
            plt.imshow(window)
            break
        winH += 2
    winW += 2