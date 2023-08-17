import cv2 as cv
import numpy as np

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
    d = np.sqrt(dHorizontally**2 + dVertically**2).astype(np.int64)

    # Scale the d to 0~255
    d = (d - d.min()) / (d.max() - d.min()) * 255
    d = d.astype(np.uint8)
    
    # eq. 2
    # The differential gray-level histogram
    diff_graylevel_hist = np.zeros(256).astype(np.int64)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            diff_graylevel_hist[d[i, j]] += 1
    
    return diff_graylevel_hist

def HDR_by_DifferentialIntensitySaturation(img):
    # to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # Calculate the DIHE and DSHE
    DIHE = diff_graylevel_hist(hsv[:, :, 2])
    DSHE = diff_graylevel_hist(hsv[:, :, 1])

    cv.imshow('DIHE', DIHE.astype(np.float64))
    cv.imshow('DSHE', DSHE.astype(np.float64))
    cv.waitKey(0)   

    return img

if __name__ == "__main__":
    # Load the image
    gray_img = cv.imread('sample.jpeg', cv.IMREAD_GRAYSCALE)
    DH = diff_graylevel_hist(gray_img)
    
    # Plot the differential gray-level histogram
    import matplotlib.pyplot as plt
    plt.bar(np.arange(256), DH)
    plt.show()