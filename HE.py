import cv2 as cv
import numpy as np
from functions.cdf import cdf

def he_intensity(img):
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    
    # 計算各階亮度出現次數
    hist = np.zeros(256).astype(np.int64)
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            hist[v[i, j]] += 1

    # 計算映射函數
    cdf_v = cdf(hist)

    # 畫出累積分布函數
    # import matplotlib.pyplot as plt
    # # size 750*250
    # plt.figure(figsize=(7.5, 2.5))
    # plt.plot(cdf_v, color='b')
    # plt.show()

    # 原圖映射到新圖
    img_he = np.zeros_like(img).astype(np.uint8)
    for i in range(img_he.shape[0]):
        for j in range(img_he.shape[1]):
            img_he[i, j, 2] = cdf_v[v[i, j]]
            img_he[i, j, 1] = s[i, j]
            img_he[i, j, 0] = h[i, j]

    img_he = cv.cvtColor(img_he, cv.COLOR_HSV2BGR)
    return img_he

def he_bgr(img):
    b, g, r = cv.split(img)
    
    # 計算各階亮度出現次數
    hist_b = np.zeros(256).astype(np.int64)
    hist_g = np.zeros(256).astype(np.int64)
    hist_r = np.zeros(256).astype(np.int64)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist_b[b[i, j]] += 1
            hist_g[g[i, j]] += 1
            hist_r[r[i, j]] += 1

    # 計算映射函數
    cdf_b = cdf(hist_b)
    cdf_g = cdf(hist_g)
    cdf_r = cdf(hist_r)

    # 原圖映射到新圖
    img_he_bgr = np.zeros_like(img).astype(np.uint8)
    for i in range(img_he_bgr.shape[0]):
        for j in range(img_he_bgr.shape[1]):
            img_he_bgr[i, j, 0] = cdf_b[b[i, j]]
            img_he_bgr[i, j, 1] = cdf_g[g[i, j]]
            img_he_bgr[i, j, 2] = cdf_r[r[i, j]]

    return img_he_bgr

def he_intensity_and_saturation(img):
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    
    # 計算各階亮度出現次數
    # 計算各階飽和度出現次數
    hist_v = np.zeros(256).astype(np.int64)
    hist_s = np.zeros(256).astype(np.int64)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist_v[v[i, j]] += 1
            hist_s[s[i, j]] += 1
    
    # 計算映射函數
    cdf_v = cdf(hist_v)
    cdf_s = cdf(hist_s)

    # 將累積分布函數映射到原圖
    img_he = np.zeros_like(img).astype(np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_he[i, j, 0] = h[i, j]
            img_he[i, j, 1] = cdf_s[s[i, j]]
            img_he[i, j, 2] = cdf_v[v[i, j]]

    img_he = cv.cvtColor(img_he, cv.COLOR_HSV2BGR)
    return img_he

if __name__ == "__main__":
    # Load the image
    img = cv.imread('samples/myself_nightshot.jpeg')
    # img = cv.imread('samples/bridge.jpg')
    # img = cv.imread('samples/cherryblossom.jpg')
    img_he = he_intensity(img)
    img_he_s = he_intensity_and_saturation(img)
    img_he_bgr = he_bgr(img)
    
    cv.imshow('img', img)
    cv.imshow('img_he', img_he)
    cv.imshow('img_he_s', img_he_s)
    cv.imshow('img_he_bgr', img_he_bgr)

    cv.waitKey(0)