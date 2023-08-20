import cv2 as cv
import numpy as np
from diff2D import diff2D
from Transformation import Transformation

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

def DHE(img):
    # to HSV
    _, _, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    diff_img, differential_histogram = diff_graylevel_hist(v)

    # Plot the differential gray-level histogram
    import matplotlib.pyplot as plt
    plt.bar(np.arange(len(differential_histogram)), differential_histogram)
    # 不要暫停
    plt.show(block=False)

    output = Transformation(diff_img, differential_histogram)
    return output

if __name__ == "__main__":
    # Load the image
    # img = cv.imread('samples/myself_nightshot.jpeg')
    # img = cv.imread('samples/bridge.jpg')
    img = cv.imread('samples/cherryblossom.jpg')
    # img = cv.GaussianBlur(img, (7, 7), 0)
    img_dhe = DHE(img)

    # Show the image
    cv.imshow('img', img)
    cv.imshow('img_dhe', img_dhe)
    cv.waitKey(0)