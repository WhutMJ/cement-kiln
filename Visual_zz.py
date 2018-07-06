from DataPreProcessing import *
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import math

myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)
matplotlib.rcParams["axes.unicode_minus"] = False
xmajorLocator   = MultipleLocator(5) #将x主刻度标签设置为5的倍数
xminorLocator   = MultipleLocator(1) #将x轴次刻度标签设置为1的倍数
barwidth=0.35#柱状图的宽度

class Visual_zz:
    def show_tongt_wd(self):
        y = DataPreprocessing().get_tongt_wd()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y,alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy/2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('筒体温度/℃', fontproperties=myfont)
        title('筒体温度变化情况\n', fontproperties=myfont)
        show()




    def show_weilc(self):
        y = DataPreprocessing().get_weilc()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('喂料秤', fontproperties=myfont)
        title('喂料秤变化情况\n', fontproperties=myfont)
        show()

    def show_youlg(self):
        y = DataPreprocessing().get_youlg()
        ymin, ymax = min(y), max(y)#由于部分数据缺失导致报错
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('游离钙', fontproperties=myfont)
        title('游离钙变化情况\n', fontproperties=myfont)
        show()

    def show_yaosu(self):
        y = DataPreprocessing().get_yaosu()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('窑速', fontproperties=myfont)
        title('窑速变化情况\n', fontproperties=myfont)
        show()

    def show_yaotc(self):
        y = DataPreprocessing().get_yaotc()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('窑头秤', fontproperties=myfont)
        title('窑头秤变化情况\n', fontproperties=myfont)
        show()

    def show_yaowc(self):
        y = DataPreprocessing().get_yaowc()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('窑尾秤', fontproperties=myfont)
        title('窑尾秤变化情况\n', fontproperties=myfont)
        show()

    def show_yijt_wd(self):
        y1 = DataPreprocessing().get_yijt_wdA()
        y2 = DataPreprocessing().get_yijt_wdB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("一级筒A、B温度变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B温度', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_yijt_yq(self):
        y1 = DataPreprocessing().get_yijt_yqA()
        y2 = DataPreprocessing().get_yijt_yqB()
        ymin, ymax = min(y1+y2), max(y1+y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("一级筒A、B压强变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)

        index=np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B压强', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_erjt_wd(self):
        y1 = DataPreprocessing().get_erjt_wdA()
        y2 = DataPreprocessing().get_erjt_wdB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("二级筒A、B温度变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B温度', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_erjt_yq(self):
        y1 = DataPreprocessing().get_erjt_yqA()
        y2 = DataPreprocessing().get_erjt_yqB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("二级筒A、B压强变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B压强', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_sanjt_wd(self):
        y1 = DataPreprocessing().get_sanjt_wdA()
        y2 = DataPreprocessing().get_sanjt_wdB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("三级筒A、B温度变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B温度', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_sanjt_yq(self):
        y1 = DataPreprocessing().get_sanjt_yqA()
        y2 = DataPreprocessing().get_sanjt_yqB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("三级筒A、B压强变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B压强', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_sijt_wd(self):
        y1 = DataPreprocessing().get_sijt_wdA()
        y2 = DataPreprocessing().get_sijt_wdB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("四级筒A、B温度变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B温度', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_sijt_yq(self):
        y1 = DataPreprocessing().get_sijt_yqA()
        y2 = DataPreprocessing().get_sijt_yqB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("四级筒A、B压强变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B压强', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_wujt_wd(self):
        y1 = DataPreprocessing().get_wujt_wdA()
        y2 = DataPreprocessing().get_wujt_wdB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("五级筒A、B温度变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B温度', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_wujt_yq(self):
        y1 = DataPreprocessing().get_wujt_yqA()
        y2 = DataPreprocessing().get_wujt_yqB()
        ymin, ymax = min(y1 + y2), max(y1 + y2)
        dy = ymax - ymin
        x = range(0, 72)

        plt.figure(figsize=(7, 4), dpi=140)
        plt.title("五级筒A、B压强变化情况", fontproperties=myfont)
        plt.grid(True)

        ax_1 = plt.subplot(111)
        index = np.arange(len(x))
        ax_1.bar(index, y1, width=barwidth, alpha=0.5, color="b", label="A")
        ax_1.bar(index + barwidth, y2, width=barwidth, alpha=0.5, color="r", label="B")
        ax_1.legend(loc="upper left", prop=myfont, shadow=True)
        ax_1.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax_1.set_ylabel('A/B压强', fontproperties=myfont)

        ax_1.set_xlabel('time/h', fontproperties=myfont)
        ax_1.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax_1.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        plt.show()
    def show_yaow_wd(self):
        y = DataPreprocessing().get_yaow_wd()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('窑尾温度', fontproperties=myfont)
        title('窑尾温度变化情况\n', fontproperties=myfont)
        show()

    def show_fenjl_wd(self):
        y = DataPreprocessing().get_fenjl_wd()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('分解炉温度', fontproperties=myfont)
        title('分解炉温度变化情况\n', fontproperties=myfont)
        show()

    def show_fenjl_yq(self):
        y = DataPreprocessing().get_fenjl_yq()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('分解炉压强', fontproperties=myfont)
        title('分解炉压强变化情况\n', fontproperties=myfont)
        show()

    def show_yicfj(self):
        y = DataPreprocessing().get_yicfj()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('一次风机', fontproperties=myfont)
        title('一次风机变化情况\n', fontproperties=myfont)
        show()

    def show_yaotyl_yq(self):
        y = DataPreprocessing().get_yaotyl_yq()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('窑头压力', fontproperties=myfont)
        title('窑头压力变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_ydyl(self):
        y = DataPreprocessing().get_bilj_ydyl()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机一段压力', fontproperties=myfont)
        title('篦冷机一段压力变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_ydS1(self):
        y = DataPreprocessing().get_bilj_ydS1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机一段S1', fontproperties=myfont)
        title('篦冷机一段S1变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_ydI1(self):
        y = DataPreprocessing().get_bilj_ydI1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机一段I1', fontproperties=myfont)
        title('篦冷机一段I1变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_erdS1(self):
        y = DataPreprocessing().get_bilj_erdS1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机二段S1', fontproperties=myfont)
        title('篦冷机二段S1变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_erdI1(self):
        y = DataPreprocessing().get_bilj_erdI1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机二段I1', fontproperties=myfont)
        title('篦冷机二段I1变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_sdS1(self):
        y = DataPreprocessing().get_bilj_sdS1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机三段S1', fontproperties=myfont)
        title('篦冷机三段S1变化情况\n', fontproperties=myfont)
        show()

    def show_bilj_sdI1(self):
        y = DataPreprocessing().get_bilj_sdI1()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('篦冷机三段I1', fontproperties=myfont)
        title('篦冷机三段I1变化情况\n', fontproperties=myfont)
        show()

    def show_sancf_yl(self):
        y = DataPreprocessing().get_sancf_yl()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('三次风压力', fontproperties=myfont)
        title('三次风压力变化情况\n', fontproperties=myfont)
        show()

    def show_gaowfj_zs(self):
        y = DataPreprocessing().get_gaowfj_zs()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('高温风机转速', fontproperties=myfont)
        title('高温风机转速变化情况\n', fontproperties=myfont)
        show()

    def show_gaowfj_dl(self):
        y = DataPreprocessing().get_gaowfj_dl()
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        x = range(0, 72)
        ax = subplot(111)
        ax.bar(x, y, alpha=0.5, color="b")
        ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])
        ax.set_xlabel('time/h')
        ax.set_ylabel('高温风机电流', fontproperties=myfont)
        title('高温风机电流变化情况\n', fontproperties=myfont)
        show()

Visual_zz().show_erjt_yq()
