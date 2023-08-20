import numpy as np

# CDF (Cumulative Distribution Function)
def cdf(hist):
    cdf = np.cumsum(hist)
    cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min()) * 255
    cdf = cdf.astype(np.uint8)
    return cdf