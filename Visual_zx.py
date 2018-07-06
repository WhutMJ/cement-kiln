'''Visual.py
~~~~~~~~~~~~
version-1_1_1:将饼状图的参数修改为一个

提供将数据转换为折线图、柱状图、饼状图的函数


'''

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

myfont = fm.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=14)
matplotlib.rcParams["axes.unicode_minus"] = False
class Visual:
    def Show(self,x=[],y=[]):
        ymin, ymax = min(y), max(y)
        dy = ymax - ymin
        fig1=plt.figure('折线图')
        ax = plt.subplot(111)
        ax.plot(x, y, linewidth=3, color='r', marker='o',
                markerfacecolor='blue', markersize=5)
        if len(x)>20:
            xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
            xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
            ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
            ax.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        else:
            xmajorLocator = MultipleLocator(1)
            ax.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax.grid(True)  # 网格
        ax.set_ylim([ymin - dy / 2, ymax + dy / 2])

        fig2=plt.figure('柱状图')
        ax2 = plt.subplot(111)
        ax2.bar(x, y, alpha=0.5, color="b")
        if len(x)>20:
            xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为5的倍数
            xminorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为1的倍数
            ax2.xaxis.set_major_locator(xmajorLocator)  # 主刻度
            ax2.xaxis.set_minor_locator(xminorLocator)  # 次刻度
        else:
            xmajorLocator = MultipleLocator(1)
            ax2.xaxis.set_major_locator(xmajorLocator)  # 主刻度
        ax2.grid(True)  # 网格
        ax2.set_ylim([ymin - dy / 2, ymax + dy / 2])

        plt.show()

    def Show_bz(self,data = []):
        # x为各类所占比例，y为各类名
        x = []
        y = []
        length = len(data)
        y = list(set(data))
        for i in set(data):
            x.append(data.count(i)/length)
        plt.title("饼状图", fontproperties=myfont)

        # 画饼状图
        patches, l_text, p_text = plt.pie(x, labels=y, autopct="%1.1f%%", shadow=True,
                                          startangle=90)
        for text in l_text:
            text.set_fontproperties(myfont)
        plt.axis("equal")

        plt.show()

