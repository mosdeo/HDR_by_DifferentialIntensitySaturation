import numpy as np
import time

# img must be a single channel image
def diff2d(img):
    if len(img.shape) != 2:
        raise Exception('The input image must be a single channel image.')
    start_time = time.time()
    
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

    print('diff2d: {} seconds'.format(time.time() - start_time))
    return diff_img

def diff2d_vectorlize(img):
    if len(img.shape) != 2:
        raise Exception('The input image must be a single channel image.')
    start_time = time.time()
    
    # 垂直 & 水平方向的差分
    dHorizontally = np.zeros_like(img).astype(np.int64)
    dVertically = np.zeros_like(img).astype(np.int64)

    # 外面補一圈 0
    dHorizontally = np.pad(dHorizontally, ((1, 1), (1, 1)), 'constant', constant_values=0)
    dVertically = np.pad(dVertically, ((1, 1), (1, 1)), 'constant', constant_values=0)

    # eq. 1
    dHorizontally[0:-2, 0:-2] += img
    dHorizontally[0:-2, 1:-1] += 2*img
    dHorizontally[0:-2, 2:] += img
    dHorizontally[2:, 0:-2] -= img
    dHorizontally[2:, 1:-1] -= 2*img
    dHorizontally[2:, 2:] -= img

    dVertically[0:-2, 0:-2] += img
    dVertically[1:-1, 0:-2] += 2*img
    dVertically[2:, 0:-2] += img
    dVertically[0:-2, 2:] -= img
    dVertically[1:-1, 2:] -= 2*img
    dVertically[2:, 2:] -= img
    
    # differential img-levels of the input image
    diff_img = np.sqrt(dHorizontally**2 + dVertically**2).astype(np.int64)
    diff_img = diff_img[1:-1, 1:-1] # 去掉外面補的一圈 0

    print('diff2d_vectorlize: {} seconds'.format(time.time() - start_time))
    return diff_img