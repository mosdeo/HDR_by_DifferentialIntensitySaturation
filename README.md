# **HDR_by_DifferentialIntensitySaturation**

進度：在暗光夜景有比較好的效果，但是原論文樣本上[[1]](pictures/result_bridge.jpg.png)[[2]](pictures/result_cherryblossom.jpg.png)並未復現出來。

DSHE: Differential saturation histogram equalization

![result_myself_nightshot](pictures/result_myself_nightshot.jpeg.png)

主要是復現這篇論文

Nakai, Keita, Yoshikatsu Hoshi, and Akira Taguchi. "Color image contrast enhacement method based on differential intensity/saturation gray-levels histograms."  *2013 International Symposium on Intelligent Signal Processing and Communication Systems* . IEEE, 2013.

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

第四步：再復現使用到空間＆亮度＆飽和度訊息的 The DHE for color images (DHECI)。DHECI.py
