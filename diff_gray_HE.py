import cv2 as cv
import numpy as np
from diff2D import diff2D

# THE DIFFERENTIAL GRAY-LEVELS HISTOGRAM EQUALIZATION

def diff_graylevel_hist(single_channel_img):
    # differential gray-levels of the input image
    diff_img = diff2D(single_channel_img)
    
    # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    differential_histogram = np.zeros(diff_img.max()+1)
    for i in range(single_channel_img.shape[0]):
        for j in range(single_channel_img.shape[1]):
            differential_histogram[diff_img[i, j]] += 1

    return diff_img, differential_histogram

def Transformation(diff_img, differential_histogram):
    differential_histogram = differential_histogram.astype(np.int64)

    # 計算映射函數
    c_r = np.zeros(len(differential_histogram))
    for i in range(len(differential_histogram)):
        c_r[i] = np.sum(differential_histogram[:i+1]) / np.sum(differential_histogram[:256])
    c_r = (c_r * 255).astype(np.uint8)

    # 差分圖映射到新圖
    output = np.zeros_like(diff_img, dtype=np.uint8)
    for i in range(diff_img.shape[0]):
        for j in range(diff_img.shape[1]):
            output[i, j] = c_r[diff_img[i, j]]

    return output

def DHE(img):
    # to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    diff_img, differential_histogram = diff_graylevel_hist(hsv[:, :, 2])

    # Plot the differential gray-level histogram
    import matplotlib.pyplot as plt
    plt.bar(np.arange(len(differential_histogram)), differential_histogram)
    # 不要暫停
    plt.show(block=False)

    output = Transformation(diff_img, differential_histogram)
    return output

if __name__ == "__main__":
    # Load the image
    img = cv.imread('sample.jpeg')
    # img = cv.GaussianBlur(img, (7, 7), 0)
    img_dhe = DHE(img)

    # Show the image
    cv.imshow('img', img)
    cv.imshow('img_dhe', img_dhe)
    cv.waitKey(0)