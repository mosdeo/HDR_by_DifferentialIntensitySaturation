import cv2 as cv
import numpy as np
from cdf import cdf

def he_intensity(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # 計算各階亮度出現次數
    hist = np.zeros(256).astype(np.int64)
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            hist[hsv[i, j, 2]] += 1

    # 計算映射函數
    cdf_v = cdf(hist)

    # 原圖映射到新圖
    img_he = np.zeros_like(hsv).astype(np.uint8)
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            img_he[i, j, 2] = cdf_v[hsv[i, j, 2]]
            img_he[i, j, 1] = hsv[i, j, 1]
            img_he[i, j, 0] = hsv[i, j, 0]

    img_he = cv.cvtColor(img_he, cv.COLOR_HSV2BGR)
    return img_he

def he_intensity_and_saturation(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # 計算各階亮度出現次數
    # 計算各階飽和度出現次數
    hist_v = np.zeros(256).astype(np.int64)
    hist_s = np.zeros(256).astype(np.int64)
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            hist_v[hsv[i, j, 2]] += 1
            hist_s[hsv[i, j, 1]] += 1
    
    # 計算映射函數
    cdf_v = cdf(hist_v)
    cdf_s = cdf(hist_s)

    # 將累積分布函數映射到原圖
    img_he = np.zeros_like(hsv).astype(np.uint8)
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            img_he[i, j, 2] = cdf_v[hsv[i, j, 2]]
            img_he[i, j, 1] = cdf_s[hsv[i, j, 1]]
            img_he[i, j, 0] = hsv[i, j, 0]

    img_he = cv.cvtColor(img_he, cv.COLOR_HSV2BGR)
    return img_he

if __name__ == "__main__":
    # Load the image
    img = cv.imread('sample.jpeg')
    img_he = he_intensity(img)
    img_he_s = he_intensity_and_saturation(img)
    
    cv.imshow('img', img)
    cv.imshow('img_he', img_he)
    cv.imshow('img_he_s', img_he_s)

    cv.waitKey(0)