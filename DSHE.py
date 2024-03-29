import cv2 as cv
import numpy as np
from functions.diff2d import diff2d_vectorlize as diff2d
from functions.transformation import transformation
from functions.display_effect import display_effect
from functions.local_correlation_of_intensity_saturation import local_correlation_of_intensity_saturation_vectorlize as local_correlation_of_intensity_saturation

# THE DIFFERENTIAL SATURATION HISTOGRAM EQUALIZATION

def DSHE(img):
    # to HSV
    h, s, v = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
    diff_img = diff2d(s)

    corr_IS = local_correlation_of_intensity_saturation(s, v)
    corr_IS = np.abs(corr_IS)
    prod_img = diff_img * corr_IS
    prod_img = prod_img.astype(np.int64)

    # Auto resize width to 750, but keep ratio, auto adjust height
    # height = int(750 * img.shape[0] / img.shape[1])
    # _corr_IS = cv.resize(corr_IS , (750, height), interpolation=cv.INTER_CUBIC)
    # # Scale to 0~255
    # _corr_IS = (_corr_IS / _corr_IS.max() * 255).astype(np.uint8)
    # cv.imshow('corr_IS', _corr_IS)
    # cv.waitKey(0)
    # cv.imwrite('pictures/local_correlation_of_intensity_saturation.png', _corr_IS)

    # eq. 2
    # The differential gray-level histogram
    # 計算各階出現次數
    # 不要用 np.histogram_bin_edges, 因為會有小數點
    diff_saturation_hist = np.bincount(prod_img.flatten(), minlength=prod_img.max()+1)
    transferred_v = transformation(v, diff_saturation_hist)
    return cv.cvtColor(cv.merge([h, s, transferred_v]), cv.COLOR_HSV2BGR)

if __name__ == "__main__":
    # Load the image
    folder = 'samples/'
    samples = ['myself_nightshot.jpeg', 'bridge.jpg', 'cherryblossom.jpg']

    for sample in samples:
        img = cv.imread(folder + sample)
        img_DSHE = DSHE(img)
        # cv.imshow('img, {}'.format(sample), img)
        # cv.imshow('DIHE, {}'.format(sample), img_DIHE)

        # # 合併顯示，左右對照
        # img_concat = np.concatenate((img, img_DSHE), axis=1)
        # cv.imshow('Original VS DSHE, {}'.format(sample), img_concat)

        display_effect(img, img_DSHE, sample)
        cv.waitKey(1)
    cv.waitKey(0)