import matplotlib.pyplot as plt
import cv2 as cv

def display_effect(img_before, img_after, title):
    # 合併顯示
    # 左上：原圖
    # 右上：處理過的
    # 左下：原圖的直方圖
    # 右下：處理過的直方圖
    fig, ax = plt.subplots(2, 2)
    fig.set_size_inches(12, 7)
    fig.suptitle(title)
    ax[0, 0].imshow(cv.cvtColor(img_before, cv.COLOR_BGR2RGB))
    ax[0, 0].set_title('Before image')
    ax[0, 1].imshow(cv.cvtColor(img_after, cv.COLOR_BGR2RGB))
    ax[0, 1].set_title('After image')
    ax[1, 0].hist(cv.cvtColor(img_before, cv.COLOR_BGR2GRAY).flatten(), bins=256)
    ax[1, 0].set_title('Before histogram')
    ax[1, 1].hist(cv.cvtColor(img_after, cv.COLOR_BGR2GRAY).flatten(), bins=256)
    ax[1, 1].set_title('After histograms')
    # plt.show()
    plt.show(block=False)
    # Save the figure
    plt.savefig('pictures/result_{}.png'.format(title))
    # plt.pause(0.1)
    plt.close()
    # release memory
    fig.clf()