import numpy as np

# img must be a single channel image
def diff2d(img):
    if len(img.shape) != 2:
        raise Exception('The input image must be a single channel image.')
    
    # 垂直 & 水平方向的差分
    dHorizontally = np.zeros_like(img).astype(np.int64)
    dVertically = np.zeros_like(img).astype(np.int64)

    # eq. 1
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            dHorizontally[i, j] = img[i+1, j+1] + 2*img[i+1, j] + img[i+1, j-1] - img[i-1, j+1] - 2*img[i-1, j] - img[i-1, j-1]
            dVertically[i, j] = img[i+1, j+1] + 2*img[i, j+1] + img[i-1, j+1] - img[i+1, j-1] - 2*img[i, j-1] - img[i-1, j-1]
    
    # differential img-levels of the input image
    diff_img = np.sqrt(dHorizontally**2 + dVertically**2).astype(np.int64)

    return diff_img

