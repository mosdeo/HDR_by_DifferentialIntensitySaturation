import numpy as np

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