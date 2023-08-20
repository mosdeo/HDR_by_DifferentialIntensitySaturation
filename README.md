# **HDR_by_DifferentialIntensitySaturation**

主要是復現這篇論文

Nakai, Keita, Yoshikatsu Hoshi, and Akira Taguchi. "Color image contrast enhacement method based on differential intensity/saturation gray-levels histograms."  *2013 International Symposium on Intelligent Signal Processing and Communication Systems* . IEEE, 2013.

---

第一步：先復現一個最簡單常用的 Histogram equalization。HE.py

關鍵：0~255 的 CDF 映射表

---

第二步：再復現使用到空間＆亮度訊息的 Differential intensity histogram equalization。DIHE.py

關鍵：差分量直方圖

---

第三步：再復現使用到空間＆飽和度訊息的 Differential saturation histogram equalization。DSHE.py

關鍵：Local correlation of saturation and intensity

---

第四步：再復現使用到空間＆亮度＆飽和度訊息的 The DHE for color images (DHECI)。DHECI.py


