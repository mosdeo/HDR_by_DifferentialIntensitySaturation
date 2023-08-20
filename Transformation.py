import numpy as np

def Transformation(diff_img, differential_histogram):
    differential_histogram = differential_histogram.astype(np.int64)

    # 計算映射轉移函數, eq. 3
    c_r = np.cumsum(differential_histogram) / np.sum(differential_histogram[:256])
    t_r = (c_r * 255).astype(np.uint8)

    # 差分圖映射到新圖
    output = np.zeros_like(diff_img, dtype=np.uint8)
    for i in range(diff_img.shape[0]):
        for j in range(diff_img.shape[1]):
            if diff_img[i, j] > 255:
                diff_img[i, j] = 255
                print(diff_img[i, j])
            output[i, j] = t_r[diff_img[i, j]]

    return output