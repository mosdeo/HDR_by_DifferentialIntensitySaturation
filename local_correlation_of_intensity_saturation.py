import cv2 as cv
import numpy as np

def local_correlation_of_intensity_saturation(s, v):
    avg_saturation = np.mean(s)
    avg_intensity = np.mean(v)

    corr = np.zeros_like(v).astype(np.float64)
    for i in range(2, v.shape[0]-2):
        for j in range(2, v.shape[1]-2):
            cov_xy = np.sum((v[i-2:i+3, j-2:j+3] - avg_intensity) * (s[i-2:i+3, j-2:j+3] - avg_saturation)) / 25
            var_x = np.sum((v[i-2:i+3, j-2:j+3] - avg_intensity)**2) / 25
            var_y = np.sum((s[i-2:i+3, j-2:j+3] - avg_saturation)**2) / 25
            corr[i, j] = cov_xy / np.sqrt(var_x * var_y)
            # corr[i, j] = np.sum((v[i-2:i+3, j-2:j+3] - avg_intensity) * (s[i-2:i+3, j-2:j+3] - avg_saturation)) / np.sqrt(np.sum((v[i-2:i+3, j-2:j+3] - avg_intensity)**2) * np.sum((s[i-2:i+3, j-2:j+3] - avg_saturation)**2))
    
    return corr

# if __name__ == "__main__":
#     # Load the image
#     img = cv.imread('sample.jpeg')
#     corr = local_correlation_of_intensity_saturation(img)
#     cv.imshow('corr', corr)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
