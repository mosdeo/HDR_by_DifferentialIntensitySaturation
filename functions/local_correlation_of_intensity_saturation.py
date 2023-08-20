import numpy as np
import time

def local_correlation_of_intensity_saturation(s, v):
    start_time = time.time()
    # Gobally mean
    # s_mean = s.mean()
    # v_mean = v.mean()
    # 論文裡特別寫了是「local mean of intensity and saturation」
    # 所以這邊修改成每一圈都要重新計算平均值
    s = s.astype(np.float64)
    v = v.astype(np.float64)
    corr = np.zeros_like(v).astype(np.float64)
    for i in range(2, v.shape[0]-2):
        for j in range(2, v.shape[1]-2):
            # v_block = v[i-2:i+3, j-2:j+3] - v_mean
            # s_block = s[i-2:i+3, j-2:j+3] - s_mean
            v_block = v[i-2:i+3, j-2:j+3]
            s_block = s[i-2:i+3, j-2:j+3]
            v_block -= v_block.mean()
            s_block -= s_block.mean()
            cov_xy = np.sum(v_block * s_block)
            var_x = np.sum(v_block**2)
            var_y = np.sum(s_block**2)
            corr[i, j] = cov_xy / np.sqrt(var_x * var_y)
    print('local_correlation_of_intensity_saturation: {} seconds'.format(time.time() - start_time))
    return corr

# TODO: NumPy Vectorlize Acceleration

def local_correlation_of_intensity_saturation_vectorlize(s, v):
    start_time = time.time()
    s = s.astype(np.float64)
    v = v.astype(np.float64)

    around25_v = np.zeros((v.shape[0]+4, v.shape[1]+4, 25), dtype=np.float64)
    around25_s = np.zeros((s.shape[0]+4, s.shape[1]+4, 25), dtype=np.float64)
    
    around25_v[0:-4, 0:-4, 0] = v
    around25_v[0:-4, 1:-3, 1] = v
    around25_v[0:-4, 2:-2, 2] = v
    around25_v[0:-4, 3:-1, 3] = v
    around25_v[0:-4, 4:, 4] = v
    around25_v[1:-3, 0:-4, 5] = v
    around25_v[1:-3, 1:-3, 6] = v
    around25_v[1:-3, 2:-2, 7] = v
    around25_v[1:-3, 3:-1, 8] = v
    around25_v[1:-3, 4:, 9] = v
    around25_v[2:-2, 0:-4, 10] = v
    around25_v[2:-2, 1:-3, 11] = v
    around25_v[2:-2, 2:-2, 12] = v
    around25_v[2:-2, 3:-1, 13] = v
    around25_v[2:-2, 4:, 14] = v
    around25_v[3:-1, 0:-4, 15] = v
    around25_v[3:-1, 1:-3, 16] = v
    around25_v[3:-1, 2:-2, 17] = v
    around25_v[3:-1, 3:-1, 18] = v
    around25_v[3:-1, 4:, 19] = v
    around25_v[4:, 0:-4, 20] = v
    around25_v[4:, 1:-3, 21] = v
    around25_v[4:, 2:-2, 22] = v
    around25_v[4:, 3:-1, 23] = v
    around25_v[4:, 4:, 24] = v

    around25_s[0:-4, 0:-4, 0] = s
    around25_s[0:-4, 1:-3, 1] = s
    around25_s[0:-4, 2:-2, 2] = s
    around25_s[0:-4, 3:-1, 3] = s
    around25_s[0:-4, 4:, 4] = s
    around25_s[1:-3, 0:-4, 5] = s
    around25_s[1:-3, 1:-3, 6] = s
    around25_s[1:-3, 2:-2, 7] = s
    around25_s[1:-3, 3:-1, 8] = s
    around25_s[1:-3, 4:, 9] = s
    around25_s[2:-2, 0:-4, 10] = s
    around25_s[2:-2, 1:-3, 11] = s
    around25_s[2:-2, 2:-2, 12] = s
    around25_s[2:-2, 3:-1, 13] = s
    around25_s[2:-2, 4:, 14] = s
    around25_s[3:-1, 0:-4, 15] = s
    around25_s[3:-1, 1:-3, 16] = s
    around25_s[3:-1, 2:-2, 17] = s
    around25_s[3:-1, 3:-1, 18] = s
    around25_s[3:-1, 4:, 19] = s
    around25_s[4:, 0:-4, 20] = s
    around25_s[4:, 1:-3, 21] = s
    around25_s[4:, 2:-2, 22] = s
    around25_s[4:, 3:-1, 23] = s
    around25_s[4:, 4:, 24] = s

    around25_v_mean = np.mean(around25_v, axis=2)
    around25_s_mean = np.mean(around25_s, axis=2)

    around25_v -= around25_v_mean[:, :, np.newaxis]
    around25_s -= around25_s_mean[:, :, np.newaxis]

    around25_cov_xy = np.sum(around25_v * around25_s, axis=2)
    around25_var_x = np.sum(around25_v**2, axis=2)
    around25_var_y = np.sum(around25_s**2, axis=2)

    around25_corr = around25_cov_xy / np.sqrt(around25_var_x * around25_var_y)

    print('local_correlation_of_intensity_saturation_vectorlize: {} seconds'.format(time.time() - start_time))
    return around25_corr[2:-2, 2:-2]

# if __name__ == "__main__":
#     # Load the image
#     img = cv.imread('sample.jpeg')
#     corr = local_correlation_of_intensity_saturation(img)
#     cv.imshow('corr', corr)
#     cv.waitKey(0)
#     cv.destroyAllWindows()