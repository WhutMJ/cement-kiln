# -*- coding: utf-8 -*-
from DataPreProcessing import *
import Tools
import math
class xuanft:       #旋风桶设备的预测
    def Diagnosis(self):
        wdcha1 = wdcha2 = wdcha3 = wdcha4 = []
        for i in range(72):
            wdcha1.append(ZDataPreprocessing().get_wujt_yqB()[i] - ZDataPreprocessing().get_sijt_yqB()[i])
            wdcha2.append(ZDataPreprocessing().get_sijt_yqB()[i] - ZDataPreprocessing().get_sanjt_yqB()[i])
            wdcha3.append(ZDataPreprocessing().get_sanjt_yqB()[i] - ZDataPreprocessing().get_erjt_yqB()[i])
            wdcha4.append(ZDataPreprocessing().get_erjt_yqB()[i] - ZDataPreprocessing().get_yijt_yqB()[i])
            a = [wdcha1[i],wdcha2[i],wdcha3[i],wdcha4[i]]
            Average = Tools.tongjl().Average(a)          #计算差值的平均值
            Biaozc = Tools.tongjl().Biaozc(a)           #计算差值的标准差
            b = []
            for x in a :
                b.append(abs(x-Average))
            print(Biaozc)
            if (max(b)/Biaozc>3):
                print(b.index(max(b)))
            else:
                print("正常")

xuanft().Diagnosis()