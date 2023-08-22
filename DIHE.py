import cv2 as cv
import numpy as np
from functions.diff2d import diff2d_vectorlize as diff2d
from functions.transformation import transformation
from functions.display_effect import display_effect

# THE DIFFERENTIAL INTENSITY HISTOGRAM EQUALIZATION

def DIHE(img):
    # to HSV
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    diff_img = diff2d(v)

     # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    # 不要用 np.histogram_bin_edges, 因為會有小數點
    diff_intensity_hist = np.bincount(diff_img.flatten(), minlength=diff_img.max()+1)

    # import matplotlib.pyplot as plt
    # # size 750*250
    # plt.figure(figsize=(7.5, 2.5))
    # plt.plot(diff_intensity_hist, color='b')
    # plt.show()

    transferred_v = transformation(v, diff_intensity_hist)
    return cv.cvtColor(cv.merge([h, s, transferred_v]), cv.COLOR_HSV2BGR)

if __name__ == "__main__":
    # Load the image
    folder = 'samples/'
    samples = ['myself_nightshot.jpeg', 'bridge.jpg', 'cherryblossom.jpg']

    for sample in samples:
        img = cv.imread(folder + sample)
        img_DIHE = DIHE(img)
        # cv.imshow('img, {}'.format(sample), img)
        # cv.imshow('DIHE, {}'.format(sample), img_DIHE)

        # # 合併顯示，左右對照
        # img_concat = np.concatenate((img, img_DIHE), axis=1)
        # cv.imshow('Original VS DSIE, {}'.format(sample), img_concat)

        display_effect(img, img_DIHE, sample)
        cv.waitKey(1)
    # cv.waitKey(0)