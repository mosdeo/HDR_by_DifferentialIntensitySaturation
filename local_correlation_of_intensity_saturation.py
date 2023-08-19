import cv2 as cv
import numpy as np

def local_correlation_of_intensity_saturation(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    avg_intensity = np.mean(hsv[:, :, 2])
    avg_saturation = np.mean(hsv[:, :, 1])

    corr = np.zeros_like(hsv[:, :, 2]).astype(np.float64)
    for i in range(2, hsv.shape[0]-2):
        for j in range(2, hsv.shape[1]-2):
            cov_xy = np.sum((hsv[i-2:i+3, j-2:j+3, 2] - avg_intensity) * (hsv[i-2:i+3, j-2:j+3, 1] - avg_saturation)) / 25
            var_x = np.sum((hsv[i-2:i+3, j-2:j+3, 2] - avg_intensity)**2) / 25
            var_y = np.sum((hsv[i-2:i+3, j-2:j+3, 1] - avg_saturation)**2) / 25
            corr[i, j] = cov_xy / np.sqrt(var_x * var_y)
            # corr[i, j] = np.sum((hsv[i-2:i+3, j-2:j+3, 2] - avg_intensity) * (hsv[i-2:i+3, j-2:j+3, 1] - avg_saturation)) / np.sqrt(np.sum((hsv[i-2:i+3, j-2:j+3, 2] - avg_intensity)**2) * np.sum((hsv[i-2:i+3, j-2:j+3, 1] - avg_saturation)**2))
    
    return corr

# if __name__ == "__main__":
#     # Load the image
#     img = cv.imread('sample.jpeg')
#     corr = local_correlation_of_intensity_saturation(img)
#     cv.imshow('corr', corr)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
