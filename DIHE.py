import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from diff2D import diff2D
from Transformation import Transformation

# THE DIFFERENTIAL INTENSITY HISTOGRAM EQUALIZATION

def DIHE(img):
    # to HSV
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))

    diff_img = diff2D(v)

     # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    # 不要用 np.histogram_bin_edges, 因為會有小數點
    diff_intensity_hist = np.bincount(diff_img.flatten(), minlength=diff_img.max()+1)

    # Plot the differential gray-level histogram

    # plt.bar(np.arange(len(diff_intensity_hist)), diff_intensity_hist)
    # # 不要暫停
    # plt.show(block=False)

    transferred_v = Transformation(v, diff_intensity_hist)
    return cv.cvtColor(cv.merge([h, s, transferred_v]), cv.COLOR_HSV2BGR)

if __name__ == "__main__":
    # Load the image
    img = cv.imread('samples/myself_nightshot.jpeg')
    # img = cv.imread('samples/bridge.jpg')
    # img = cv.imread('samples/cherryblossom.jpg')
    # img = cv.GaussianBlur(img, (7, 7), 0)
    img_DIHE = DIHE(img)

    # Show the image
    cv.imshow('img', img)
    cv.imshow('img_DIHE', img_DIHE)
    cv.waitKey(0)