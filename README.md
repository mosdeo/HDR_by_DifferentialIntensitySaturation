# **HDR_by_DifferentialIntensitySaturation**

![result_myself_nightshot](pictures/result_myself_nightshot.jpeg.png)

主要是復現這篇論文：

Nakai, Keita, Yoshikatsu Hoshi, and Akira Taguchi. "Color image contrast enhacement method based on differential intensity/saturation gray-levels histograms."  *2013 International Symposium on Intelligent Signal Processing and Communication Systems* . IEEE, 2013.

進度：

- 在自己拍的暗光夜景，有好的效果
- 原論文樣本上[[1]](pictures/result_bridge.jpg.png)[[2]](pictures/result_cherryblossom.jpg.png)復現的效果，並未像論文中那麼好，實際效果偏向過曝。

---

第一步：先復現一個最簡單常用的 Histogram equalization。HE.py

關鍵：0~255 的 CDF 映射表

![cdf](pictures/cdf.png)

---

第二步：再復現使用到空間＆亮度訊息的 Differential intensity histogram equalization。DIHE.py

關鍵：差分量直方圖

![diff_hist](pictures/diff_hist.png)

---

第三步：再復現使用到空間＆飽和度訊息的 Differential saturation histogram equalization。DSHE.py

關鍵：Local correlation of saturation and intensity

![local_corr](pictures/local_correlation_of_intensity_saturation.png)

---

第四步：以互補比例混合 DIHE & DSHE => The DHE for color images (DHECI)。DHECI.py

```python
# eq. 7
alpha = 0.5
diff_hist_color = alpha * diff_saturation_hist + (1 - alpha) * diff_intensity_hist
```

---

### 向量化加速：local_correlation_of_intensity_saturation.py

無向量化：

```python
def local_correlation_of_intensity_saturation(s, v):
```

向量化：

```python
def local_correlation_of_intensity_saturation_vectorlize(s, v):
```

三個樣本的時間比較：

```bash
local_correlation_of_intensity_saturation: 19.283746004104614 seconds
local_correlation_of_intensity_saturation: 2.2866947650909424 seconds
local_correlation_of_intensity_saturation: 4.0586559772491455 seconds
```

```bash
RuntimeWarning: invalid value encountered in divide
  around25_corr = around25_cov_xy / np.sqrt(around25_var_x * around25_var_y)
local_correlation_of_intensity_saturation_vectorlize: 0.6869769096374512 seconds
local_correlation_of_intensity_saturation_vectorlize: 0.06972908973693848 seconds
local_correlation_of_intensity_saturation_vectorlize: 0.1213228702545166 seconds
```

註：向量化由於統一除法，有除以 0 的 RuntimeWarning，但已用```np.nan_to_num```善後，不影響結果。

---

### 向量化加速：diff2d.py

無向量化：

```python
def diff2d(img):
```

向量化：

```python
def diff2d_vectorlize(img):
```

三個樣本的時間比較：

```bash
diff2d: 7.152828216552734 seconds
diff2d: 7.096435070037842 seconds

diff2d: 0.8262782096862793 seconds
diff2d: 0.844656229019165 seconds

diff2d: 1.5022540092468262 seconds
diff2d: 1.491786003112793 seconds
```

```bash
diff2d_vectorlize: 0.0222930908203125 seconds
diff2d_vectorlize: 0.020488739013671875 seconds

diff2d_vectorlize: 0.0023682117462158203 seconds
diff2d_vectorlize: 0.0021829605102539062 seconds

diff2d_vectorlize: 0.005584001541137695 seconds
diff2d_vectorlize: 0.004849910736083984 seconds
```
