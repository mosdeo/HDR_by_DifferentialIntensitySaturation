import cv2 as cv
import numpy as np

def local_correlation_of_intensity_saturation(s, v):
    s_mean = s.mean()
    v_mean = v.mean()
    corr = np.zeros_like(v).astype(np.float64)
    for i in range(2, v.shape[0]-2):
        for j in range(2, v.shape[1]-2):
            v_block = v[i-2:i+3, j-2:j+3] - v_mean
            s_block = s[i-2:i+3, j-2:j+3] - s_mean
            cov_xy = np.sum(v_block * s_block)
            var_x = np.sum(v_block**2)
            var_y = np.sum(s_block**2)
            corr[i, j] = cov_xy / np.sqrt(var_x * var_y)
    return corr

# if __name__ == "__main__":
#     # Load the image
#     img = cv.imread('sample.jpeg')
#     corr = local_correlation_of_intensity_saturation(img)
#     cv.imshow('corr', corr)
#     cv.waitKey(0)
#     cv.destroyAllWindows()