import cv2 as cv
import numpy as np

# THE DIFFERENTIAL GRAY-LEVELS HISTOGRAM EQUALIZATION

# 計算累積分布函數
def cdf(hist):
    cdf = np.cumsum(hist)
    cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min()) * 255
    cdf = cdf.astype(np.uint8)
    return cdf

def diff_graylevel_hist(single_channel_img):
    gray = single_channel_img
    # 垂直 & 水平方向的差分
    dHorizontally = np.zeros_like(gray).astype(np.int64)
    dVertically = np.zeros_like(gray).astype(np.int64)

    # eq. 1
    for i in range(1, gray.shape[0]-1):
        for j in range(1, gray.shape[1]-1):
            dHorizontally[i, j] = gray[i+1, j+1] + 2*gray[i+1, j] + gray[i+1, j-1] - gray[i-1, j+1] - 2*gray[i-1, j] - gray[i-1, j-1]
            dVertically[i, j] = gray[i+1, j+1] + 2*gray[i, j+1] + gray[i-1, j+1] - gray[i+1, j-1] - 2*gray[i, j-1] - gray[i-1, j-1]
    
    # differential gray-levels of the input image
    diff_img = np.sqrt(dHorizontally**2 + dVertically**2).astype(np.int64)
    
    # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    differential_histogram = np.zeros(diff_img.max()+1)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            differential_histogram[diff_img[i, j]] += 1

    return diff_img, differential_histogram

def Transformation(diff_img, differential_histogram):
    differential_histogram = differential_histogram.astype(np.int64)

    # 計算映射函數
    c_r = np.zeros(len(differential_histogram))
    for i in range(len(differential_histogram)):
        c_r[i] = np.sum(differential_histogram[:i+1]) / np.sum(differential_histogram)
    c_r = (c_r * 255).astype(np.uint8)

    # 將累積分布函數映射到原圖
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
    img_dhe = DHE(img)

    # Show the image
    cv.imshow('img', img)
    cv.imshow('img_dhe', img_dhe)
    cv.waitKey(0)