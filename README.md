# **HDR_by_DifferentialIntensitySaturation**

主要是復現這篇論文

Nakai, Keita, Yoshikatsu Hoshi, and Akira Taguchi. "Color image contrast enhacement method based on differential intensity/saturation gray-levels histograms."  *2013 International Symposium on Intelligent Signal Processing and Communication Systems* . IEEE, 2013.

---

第一步：先復現一個最簡單常用的 Histogram equalization。normal_HE.py

0~255 的 CDF 映射表是關鍵。

---

第一步：再復現使用到空間訊息的 Differential gray-levels histogram equalization。diff_gray_HE.py
