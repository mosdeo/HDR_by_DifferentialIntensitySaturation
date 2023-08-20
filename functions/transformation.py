import numpy as np
import matplotlib.pyplot as plt

def transformation(someone_color_plane , differential_histogram):
    differential_histogram = differential_histogram.astype(np.int64)

    # 計算映射轉移函數, eq. 3
    c_r = np.cumsum(differential_histogram) / np.sum(differential_histogram[:256])
    # plt.plot(255 * c_r)
    # plt.show(block=False)

    t_r = (255 * c_r).astype(np.uint8) # 論文中寫的

    # # Re-bins c_r to [0, 255] # 好像應該是這樣的
    # t_r = np.zeros(256, dtype=np.int32)
    # for i in range(256):
    #     idx_ceiling = int(np.ceil(i * len(c_r) / 256))
    #     idx_floor = int(np.floor(i * len(c_r) / 256))
    #     t_r[i] = 255 * (c_r[idx_ceiling] + c_r[idx_floor]) / 2 / c_r.max()
    # plt.plot(t_r)
    # plt.show(block=False)
    
    # 差分圖映射到新圖
    transferred_plane = np.zeros_like(someone_color_plane, dtype=np.uint8)
    for i in range(someone_color_plane.shape[0]):
        for j in range(someone_color_plane.shape[1]):
            # if someone_color_plane[i, j] > 255:
            #     someone_color_plane[i, j] = 255
            #     print(someone_color_plane[i, j])
            transferred_plane[i, j] = t_r[someone_color_plane[i, j]]

    return transferred_plane