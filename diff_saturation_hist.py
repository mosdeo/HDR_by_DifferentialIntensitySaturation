import cv2 as cv
import numpy as np
from diff2D import diff2D
from local_correlation_of_intensity_saturation import local_correlation_of_intensity_saturation

# THE DIFFERENTIAL GRAY-LEVELS HISTOGRAM EQUALIZATION

def diff_saturation_hist(saturation_channel, intensity_channel):
    # differential gray-levels of the input saturation_channel
    diff_img = diff2D(saturation_channel)
    corr_IS = local_correlation_of_intensity_saturation(saturation_channel, intensity_channel)
    corr_IS = np.abs(corr_IS)

    cv.imshow('corr_IS', corr_IS.astype(np.float64))

    prod_img = diff_img * corr_IS
    prod_img = prod_img.astype(np.int64)

    cv.imshow('prod_img', prod_img.astype(np.float64))
    
    # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    differential_histogram = np.zeros(diff_img.max()+1)
    for i in range(saturation_channel.shape[0]):
        for j in range(saturation_channel.shape[1]):
            differential_histogram[prod_img[i, j]] += 1

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

def DSE(img):
    # to HSV
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    diff_img, differential_histogram = diff_saturation_hist(s, v)

    # Plot the differential gray-level histogram
    import matplotlib.pyplot as plt
    plt.bar(np.arange(len(differential_histogram)), differential_histogram)
    # 不要暫停
    plt.show(block=False)

    output = Transformation(diff_img, differential_histogram)
    # Combine the h, output, v channels to an image in HSV color space
    output = cv.cvtColor(cv.merge([h, output, v]), cv.COLOR_HSV2BGR)
    return output

if __name__ == "__main__":
    # Load the image
    # img = cv.imread('samples/myself_nightshot.jpeg')
    # img = cv.imread('samples/bridge.jpg')
    img = cv.imread('samples/cherryblossom.jpg')
    # img = cv.GaussianBlur(img, (7, 7), 0)
    img_dse = DSE(img)

    # Show the image
    cv.imshow('img', img)
    cv.imshow('img_dse', img_dse)
    cv.waitKey(0)
