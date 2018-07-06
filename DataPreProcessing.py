'''DataPreProcessing.py
~~~~~~~~~~~~
    现有数据五种表的数据读取接口

~~~~~~~~~~~~
    修改内容：
        由于前一个版本的三线窑数据提取是以’data-3days.xlsx‘文件为模板写的，与我们现在所用的三线窑数据模板有出入，故做了修改，现已可以正常
        调用

~~~~~~~~~~~~
    使用手册：
    一般调用形式为：
        from DataPreProcessing import *
        ...
        ZDataPreprocessing(i,filename).get_变量名()
    i 为表的种类，不同的表不同的种类
    filename 文件名

    应用实例：
        ZDataPreprocessing(5,'脱硫系统运行记录.xlsx').get_xist_yanghfjyl()
    以此类推
'''

# -*- coding: utf-8 -*-
import xlrd

class ZDataPreprocessing:
    '导入表格数据做接口，方便进行数据处理'
    __weilc = []
    __youlg = []
    __hegqk = []
    __yaos = []
    __yaotc = []
    __yaowc = []
    __tongt_wd = []
    __yijt_wdA = []
    __yijt_yqA = []
    __yijt_wdB = []
    __yijt_yqB = []
    __erjt_wdA = []
    __erjt_yqA = []
    __erjt_wdB = []
    __erjt_yqB = []
    __sanjt_wdA = []
    __sanjt_yqA = []
    __sanjt_wdB = []
    __sanjt_yqB = []
    __sijt_wdA = []
    __sijt_yqA = []
    __sijt_wdB = []
    __sijt_yqB = []
    __wujt_wdA = []
    __wujt_yqA = []
    __wujt_wdB = []
    __wujt_yqB = []
    __yaow_wd = []
    __fenjl_wd = []
    __fenjl_yq = []
    __yicfj = []
    __yaotyl_yq = []
    __bilj_ydyl = [] #篦冷机一段压力
    __bilj_ydS1 = []
    __bilj_ydI1 = []
    __bilj_erdS1 = []
    __bilj_erdI1 = []
    __bilj_sandS1 = []
    __bilj_sandI1 = []
    __sancf_yl = []
    __gaowfj_zs = []
    __gaowfj_dl = []


    __chumsl_KH = []  #出磨生料KH值
    __chumsl_SM = []
    __chumsl_IM = []
    __ruysl_CaO = []  #入窑生料CaO含量
    __ruysl_Fe2O3 = []
    __ruysl_KH = []
    __ruysl_SM = []
    __ruysl_IM = []
    __shul_KH = []  #孰料KH值
    __shul_SM = []
    __shul_IM = []
    __shul_K2O = []
    __shul_Na2O = []
    __shul_SO3 = []
    __ruymf_shuf = []  #入窑煤粉水分
    __ruymf_huif = []  #入窑煤粉灰分
    __ruymf_huiff = []  #入窑煤粉挥发分
    __ruymf_rez = []    #入窑煤粉热值
    __ruymf_gudt = []


    __AO5F01 = []
    __lisz = []
    __w01S01rpm = []
    __v72F01 = []
    __v82F01 = []
    __A51P01 = []
    __A51T01 = []
    __A51P02 = []
    __A52P01 = []
    __A52T01 = []
    __A52P02 = []
    __A53P01 = []
    __A53T01 = []
    __A53P02 = []
    __A54P01 = []
    __A54T01 = []
    __A54P02 = []
    __A54T02 = []
    __A55P01 = []
    __A55T01 = []
    __A56T01 = []
    __yans_W01_A01 = []
    __yans_W01_P01 = []
    __yans_W01_t01 = []
    __v91p01 = []
    __W1p01 = []
    __dianscjkfm = []
    __bilj_K02Tmax = []
    __bilj_K02SI = []
    __bilj_K02II = []
    __bilj_K01PI = []
    __bilj_K11PI = []
    __bilj_K12PI = []
    __bilj_K13PI = []
    __sancfgA58P01 = []
    __gaowfjJ01z01 = []
    __gaowfjJ02SI = []

    __weil_A01F01 = []
    __moj_M01X01  = []
    __moj_M03I01 = []
    __moj_M01P01 = []
    __moj_M01P02 = []
    __moj_M01T01 = []
    __moj_M01T02 = []
    __cufflq_S01P01 = []
    __cufflq_S01T01 = []
    __fengj_S04Z01 = []
    __fengj_S05I01 = []
    __meifc_L11T01 = []
    __meifc_L11l01 = []
    __meifc_L21T01 = []
    __meifc_L21L01 = []
    __dianscmfc_P11A01 = []
    __diansc_P11T01 = []
    __diansc_P11T02 = []
    __diansc_P11T3_T6 = []
    __meif_shuif = []
    __meif_hegqk1 = []
    __meif_xid = []
    __meif_hegqk2 = []


    __xist_yanghfjyl = []
    __xist_xunhbdl1 = []
    __xist_xunhbdl2 = []
    __xist_xunhbdl3 = []
    __xist_yal1 = []
    __xist_yal2 = []
    __xist_yew = []
    __xist_mid = []
    __xist_PH1 = []
    __xist_PH2 = []
    __jiangwq_chongxyl = []
    __jiangwq_yac = []
    __jiangwq_chongxsj = []
    __jiangwq_chongxjg = []
    __shigx_yew = []
    __shigx_liul = []
    __jiangyx_yal1 = []
    __jiangyx_yal2 = []
    __jiangyx_yew = []
    __jiangyx_mid = []
    __chusgxt_xuanlqyl = []
    __chusgxt_lvbhd = []
    __chusgxt_zhenkd = []
    __jisk_yew = []
    __gongysb_yew = []
    __gongysb_yal = []
    __rukyq_xianyl1 = []
    __rukyq_xianyl2 = []
    __rukyq_SO21  = []
    __rukyq_SO22 = []
    __chukyq_SO2nd = []
    __chukyq_Noxnd = []
    __chukyq_O2nd = []
    __chukyq_wend = []
    __chukyq_yal = []
    __chukyq_lius = []
    __chukyq_kelwnd = []
    __chukyq_shid = []
    __zhesz_SO2 = []
    __zhesz_Nox = []
    __zhesz_kelw = []

    __yuanmc_M14403F1 = []
    __yuanmc_M14404F1 = []

    __filename1 = __filename2 = __filename3 = __filename4 = __filename5 = __filename6 = ''
    __i = 0

    def __init__(self,i,filename):
        if(i == 1):
            ZDataPreprocessing.__filename1 = filename
            ZDataPreprocessing.__i = 1
        elif(i == 2):
            ZDataPreprocessing.__filename2 = filename
            ZDataPreprocessing.__i = 2
        elif(i == 3):
            ZDataPreprocessing.__filename3 = filename
            ZDataPreprocessing.__i = 3
        elif(i == 4):
            ZDataPreprocessing.__filename4 = filename
            ZDataPreprocessing.__i = 4
        elif(i == 5):
            ZDataPreprocessing.__filename5 = filename
            ZDataPreprocessing.__i = 5
        else:
            ZDataPreprocessing.__filename6 = filename
            ZDataPreprocessing.__i = 6

    def preparation(self):
        #filename = 'data-3days.xlsx'
        try:
            if(ZDataPreprocessing.__i == 1):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename1)
                ds = data.sheet_by_name('Sheet1')
                return ds
            if (ZDataPreprocessing.__i == 2):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename2)
                ds = data.sheet_by_name('表2')
                return ds
            if (ZDataPreprocessing.__i == 3):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename3)
                ds = data.sheet_by_name('Sheet1')
                return ds
            if (ZDataPreprocessing.__i == 4):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename4)
                ds = data.sheet_by_name('Sheet1')
                return ds
            if (ZDataPreprocessing.__i == 5):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename5)
                ds = data.sheet_by_name('Sheet1')
                return ds
            if (ZDataPreprocessing.__i == 6):
                data = xlrd.open_workbook(ZDataPreprocessing.__filename6)
                ds = data.sheet_by_name('Sheet1')
                return ds
        except FileNotFoundError:
            return 0

    '''
    三线窑工作表数据获取函数
    filename1数据区域
    '''
    def get_weilc(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__weilc = ds.col_values(1,3)
        return ZDataPreprocessing.__weilc
    def get_youlg(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__youlg = ds.col_values(4,3)
        return ZDataPreprocessing.__youlg
    def get_hegqk(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__hegqk = ds.col_values(5, 3)
        return ZDataPreprocessing.__hegqk
    def get_yaos(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yaos = ds.col_values(6, 3)
        return ZDataPreprocessing.__yaos
    def get_yaotc(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yaotc = ds.col_values(7, 3)
        return ZDataPreprocessing.__yaotc
    def get_yaowc(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yaowc = ds.col_values(8, 3)
        return ZDataPreprocessing.__yaowc
    def get_tongt_wd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__tongt_wd = ds.col_values(9, 3)
        return ZDataPreprocessing.__tongt_wd
    def get_yijt_wdA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yijt_wdA = ds.col_values(10, 3)
        return ZDataPreprocessing.__yijt_wdA
    def get_yijt_yqA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yijt_yqA = ds.col_values(11, 3)
        return ZDataPreprocessing.__yijt_yqA
    def get_yijt_wdB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yijt_wdB = ds.col_values(12, 3)
        return ZDataPreprocessing.__yijt_wdB
    def get_yijt_yqB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yijt_yqB = ds.col_values(13, 3)
        return ZDataPreprocessing.__yijt_yqB
    def get_erjt_wdA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__erjt_wdA = ds.col_values(14, 3)
        return ZDataPreprocessing.__erjt_wdA
    def get_erjt_yqA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__erjt_yqA = ds.col_values(15, 3)
        return ZDataPreprocessing.__erjt_yqA
    def get_erjt_wdB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__erjt_wdB = ds.col_values(16, 3)
        return ZDataPreprocessing.__erjt_wdB
    def get_erjt_yqB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__erjt_yqB = ds.col_values(17, 3)
        return ZDataPreprocessing.__erjt_yqB
    def get_sanjt_wdA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sanjt_wdA = ds.col_values(18, 3)
        return ZDataPreprocessing.__sanjt_wdA
    def get_sanjt_yqA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sanjt_yqA = ds.col_values(19, 3)
        return ZDataPreprocessing.__sanjt_yqA
    def get_sanjt_wdB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sanjt_wdB = ds.col_values(20, 3)
        return ZDataPreprocessing.__sanjt_wdB
    def get_sanjt_yqB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sanjt_yqB = ds.col_values(21, 3)
        return ZDataPreprocessing.__sanjt_yqB
    def get_sijt_wdA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sijt_wdA = ds.col_values(22, 3)
        return ZDataPreprocessing.__sijt_wdA
    def get_sijt_yqA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sijt_yqA = ds.col_values(23, 3)
        return ZDataPreprocessing.__sijt_yqA
    def get_sijt_wdB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sijt_wdB = ds.col_values(24, 3)
        return ZDataPreprocessing.__sijt_wdB
    def get_sijt_yqB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sijt_yqB = ds.col_values(25, 3)
        return ZDataPreprocessing.__sijt_yqB
    def get_wujt_wdA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__wujt_wdA = ds.col_values(26, 3)
        return ZDataPreprocessing.__wujt_wdA
    def get_wujt_yqA(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__wujt_yqA = ds.col_values(27, 3)
        return ZDataPreprocessing.__wujt_yqA
    def get_wujt_wdB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__wujt_wdB = ds.col_values(28, 3)
        return ZDataPreprocessing.__wujt_wdB
    def get_wujt_yqB(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__wujt_yqB = ds.col_values(29, 3)
        return ZDataPreprocessing.__wujt_yqB
    def get_yaow_wd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yaow_wd = ds.col_values(30, 3)
        return ZDataPreprocessing.__yaow_wd
    def get_fenjl_wd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__fenjl_wd = ds.col_values(31, 3)
        return ZDataPreprocessing.__fenjl_wd
    def get_fenjl_yq(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__fenjl_yq = ds.col_values(32, 3)
        return ZDataPreprocessing.__fenjl_yq
    def get_yicfj(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yicfj = ds.col_values(33, 3)
        return ZDataPreprocessing.__yicfj
    def get_yaotyl_yq(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yaotyl_yq = ds.col_values(34, 3)
        return ZDataPreprocessing.__yaotyl_yq
    def get_bilj_ydyl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_ydyl = ds.col_values(35, 3)
        return ZDataPreprocessing.__bilj_ydyl
    def get_bilj_ydS1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_ydS1 = ds.col_values(36, 3)
        return ZDataPreprocessing.__bilj_ydS1
    def get_bilj_ydI1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_ydI1 = ds.col_values(37, 3)
        return ZDataPreprocessing.__bilj_ydI1
    def get_bilj_erdS1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_erdS1 = ds.col_values(38, 3)
        return ZDataPreprocessing.__bilj_erdS1
    def get_bilj_erdI1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_erdI1 = ds.col_values(39, 3)
        return ZDataPreprocessing.__bilj_erdI1
    def get_bilj_sandS1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_sandS1 = ds.col_values(40,3)
        return ZDataPreprocessing.__bilj_sandS1
    def get_bilj_sandI1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_sandI1 = ds.col_values(41, 3)
        return ZDataPreprocessing.__bilj_sandI1
    def get_sancf_yl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sancf_yl = ds.col_values(42, 3)
        return ZDataPreprocessing.__sancf_yl
    def get_gaowfj_zs(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gaowfj_zs = ds.col_values(43, 3)
        return ZDataPreprocessing.__gaowfj_zs
    def get_gaowfj_dl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gaowfj_dl = ds.col_values(44, 3)
        return ZDataPreprocessing.__gaowfj_dl

    '''
    物料质量表的数据获取函数
    filename2数据区域
    '''
    def get_chumsl_KH(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chumsl_KH = ds.col_values(1, 2)
        return ZDataPreprocessing.__chumsl_KH
    def get_chumsl_SM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chumsl_SM = ds.col_values(2, 2)
        return ZDataPreprocessing.__chumsl_SM
    def get_chumsl_IM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chumsl_IM = ds.col_values(3, 2)
        return ZDataPreprocessing.__chumsl_IM
    def get_ruysl_CaO(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruysl_CaO = ds.col_values(4, 2)
        return ZDataPreprocessing.__ruysl_CaO
    def get_ruysl_Fe2O3(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruysl_Fe2O3 = ds.col_values(5, 2)
        return ZDataPreprocessing.__ruysl_Fe2O3
    def get_ruysl_KH(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruysl_KH = ds.col_values(6, 2)
        return ZDataPreprocessing.__ruysl_KH
    def get_ruysl_SM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruysl_SM = ds.col_values(7, 2)
        return ZDataPreprocessing.__ruysl_SM
    def get_ruysl_IM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruysl_IM = ds.col_values(8, 2)
        return ZDataPreprocessing.__ruysl_IM
    def get_shul_KH(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_KH = ds.col_values(9, 2)
        return ZDataPreprocessing.__shul_KH
    def get_shul_SM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_SM = ds.col_values(10, 2)
        return ZDataPreprocessing.__shul_SM
    def get_shul_IM(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_IM = ds.col_values(11, 2)
        return ZDataPreprocessing.__shul_IM
    def get_shul_K2O(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_K2O = ds.col_values(12, 2)
        return ZDataPreprocessing.__shul_K2O
    def get_shul_Na2O(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_Na2O = ds.col_values(13, 2)
        return ZDataPreprocessing.__shul_Na2O
    def get_shul_SO3(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shul_SO3 = ds.col_values(14, 2)
        return ZDataPreprocessing.__shul_SO3
    def get_ruymf_shuf(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruymf_shuf = ds.col_values(15, 2)
        return ZDataPreprocessing.__ruymf_shuf
    def get_ruymf_huif(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruymf_huif = ds.col_values(16, 2)
        return ZDataPreprocessing.__ruymf_huif
    def get_ruymf_huiff(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruymf_huiff = ds.col_values(17, 2)
        return ZDataPreprocessing.__ruymf_huiff
    def get_ruymf_rez(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruymf_rez = ds.col_values(18, 2)
        return ZDataPreprocessing.__ruymf_rez
    def get_ruymf_gudt(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__ruymf_gudt = ds.col_values(19,2)
        return ZDataPreprocessing.__ruymf_gudt

    '''
       一线窑操作数据表获取函数
       filename3数据区域
    '''
    def get_AO5F01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__AO5F01 = ds.col_values(1, 3)
        return ZDataPreprocessing.__AO5F01
    def get_lisz(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__lisz = ds.col_values(4, 3)
        return ZDataPreprocessing.__lisz
    def get_youlg1(self):          #一线窑中游离钙的数据
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__youlg = ds.col_values(5,3)
        return ZDataPreprocessing.__youlg
    def get_w01S01rpm(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__w01S01rpm = ds.col_values(7, 3)
        return ZDataPreprocessing.__w01S01rpm
    def get_v72F01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__v72F01 = ds.col_values(8, 3)
        return ZDataPreprocessing.__v72F01
    def get_v82F01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__v82F01 = ds.col_values(9, 3)
        return ZDataPreprocessing.__v82F01
    def get_tongt_wd1(self):        #一线窑筒体温度数据
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__tongt_wd = ds.col_values(10, 3)
        return ZDataPreprocessing.__tongt_wd
    def get_A51P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A51P01 = ds.col_values(11,3)
        return ZDataPreprocessing.__A51P01
    def get_A51T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A51T01 = ds.col_values(12,3)
        return ZDataPreprocessing.__A51T01
    def get_A51P02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A51P02 = ds.col_values(13,3)
        return ZDataPreprocessing.__A51P02
    def get_A52P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A52P01 = ds.col_values(14,3)
        return ZDataPreprocessing.__A52P01
    def get_A52T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A52T01 = ds.col_values(15,3)
        return ZDataPreprocessing.__A52T01
    def get_A52P02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A52P02 = ds.col_values(16,3)
        return ZDataPreprocessing.__A52P02
    def get_A53P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A53P01 = ds.col_values(17,3)
        return ZDataPreprocessing.__A53P01
    def get_A53T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A53T01 = ds.col_values(18,3)
        return ZDataPreprocessing.__A53T01
    def get_A53P02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A53P02 = ds.col_values(19,3)
        return ZDataPreprocessing.__A53P02
    def get_A54P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A54P01 = ds.col_values(20,3)
        return ZDataPreprocessing.__A54P01
    def get_A54T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A54T01 = ds.col_values(21,3)
        return ZDataPreprocessing.__A54T01
    def get_A54P02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A54P02 = ds.col_values(22,3)
        return ZDataPreprocessing.__A54P02
    def get_A54T02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A54T02 = ds.col_values(23,3)
        return ZDataPreprocessing.__A54T02
    def get_A55P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A55P01 = ds.col_values(24,3)
        return ZDataPreprocessing.__A55P01
    def get_A55T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A55T01 = ds.col_values(25,3)
        return ZDataPreprocessing.__A55T01
    def get_A56T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__A56T01 = ds.col_values(26,3)
        return ZDataPreprocessing.__A56T01
    def get_yans_W01_A01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yans_W01_A01 = ds.col_values(27,3)
        return ZDataPreprocessing.__yans_W01_A01
    def get_yans_W01_P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yans_W01_P01 = ds.col_values(28,3)
        return ZDataPreprocessing.__yans_W01_P01
    def get_yans_W01_t01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__yans_W01_t01 = ds.col_values(29,3)
        return ZDataPreprocessing.__yans_W01_t01
    def get_v91p01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__v91p01 = ds.col_values(30,3)
        return ZDataPreprocessing.__v91p01
    def get_W1p01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__W1p01 = ds.col_values(31,3)
        return ZDataPreprocessing.__W1p01
    def get_dianscjkfm(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__dianscjkfm = ds.col_values(32,3)
        return ZDataPreprocessing.__dianscjkfm
    def get_bilj_K02Tmax(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K02Tmax = ds.col_values(33,3)
        return ZDataPreprocessing.__bilj_K02Tmax
    def get_bilj_K02SI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K02SI = ds.col_values(34,3)
        return ZDataPreprocessing.__bilj_K02SI
    def get_bilj_K02II(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K02II = ds.col_values(35,3)
        return ZDataPreprocessing.__bilj_K02II
    def get_bilj_K01PI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K01PI = ds.col_values(36,3)
        return ZDataPreprocessing.__bilj_K01PI
    def get_bilj_K11PI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K11PI = ds.col_values(37,3)
        return ZDataPreprocessing.__bilj_K11PI
    def get_bilj_K12PI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K12PI = ds.col_values(38,3)
        return ZDataPreprocessing.__bilj_K12PI
    def get_bilj_K13PI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__bilj_K13PI = ds.col_values(39,3)
        return ZDataPreprocessing.__bilj_K13PI
    def get_sancfgA58P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__sancfgA58P01 = ds.col_values(40,3)
        return ZDataPreprocessing.__sancfgA58P01
    def get_gaowfjJ01z01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gaowfjJ01z01 = ds.col_values(41,3)
        return ZDataPreprocessing.__gaowfjJ01z01
    def get_gaowfjJ02SI(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gaowfjJ02SI = ds.col_values(42,3)
        return ZDataPreprocessing.__gaowfjJ02SI

    '''
           煤磨系统操作数据表获取函数
           filename4数据区域
        '''
    def get_weil_A01F01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__weil_A01F01 = ds.col_values(1,2)
        return ZDataPreprocessing.__weil_A01F01
    def get_moj_M01X01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M01X01 = ds.col_values(2, 2)
        return ZDataPreprocessing.__moj_M01X01
    def get_moj_M03I01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M03I01 = ds.col_values(3, 2)
        return ZDataPreprocessing.__moj_M03I01
    def get_moj_M01P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M01P01 = ds.col_values(4, 2)
        return ZDataPreprocessing.__moj_M01P01
    def get_moj_M01P02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M01P02 = ds.col_values(5, 2)
        return ZDataPreprocessing.__moj_M01P02
    def get_moj_M01T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M01T01 = ds.col_values(6, 2)
        return ZDataPreprocessing.__moj_M01T01
    def get_moj_M01T02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__moj_M01T02 = ds.col_values(7, 2)
        return ZDataPreprocessing.__moj_M01T02
    def get_cufflq_S01P01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__cufflq_S01P01 = ds.col_values(8, 2)
        return ZDataPreprocessing.__cufflq_S01P01
    def get_cufflq_S01T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__cufflq_S01T01 = ds.col_values(9, 2)
        return ZDataPreprocessing.__cufflq_S01T01
    def get_fengj_S04Z01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__fengj_S04Z01 = ds.col_values(10, 2)
        return ZDataPreprocessing.__fengj_S04Z01
    def get_fengj_S05I01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__fengj_S05I01 = ds.col_values(11, 2)
        return ZDataPreprocessing.__fengj_S05I01
    def get_meifc_L11T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meifc_L11T01 = ds.col_values(12, 2)
        return ZDataPreprocessing.__meifc_L11T01
    def get_meifc_L11l01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meifc_L11l01 = ds.col_values(13, 2)
        return ZDataPreprocessing.__meifc_L11l01
    def get_meifc_L21T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meifc_L21T01 = ds.col_values(14, 2)
        return ZDataPreprocessing.__meifc_L21T01
    def get_meifc_L21L01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meifc_L21L01 = ds.col_values(15, 2)
        return ZDataPreprocessing.__meifc_L21L01
    def get_dianscmfc_P11A01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__dianscmfc_P11A01 = ds.col_values(16, 2)
        return ZDataPreprocessing.__dianscmfc_P11A01
    def get_diansc_P11T01(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__diansc_P11T01 = ds.col_values(17, 2)
        return ZDataPreprocessing.__diansc_P11T01
    def get_diansc_P11T02(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__diansc_P11T02 = ds.col_values(18, 2)
        return ZDataPreprocessing.__diansc_P11T02
    def get_diansc_P11T3_T6(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__diansc_P11T3_T6 = ds.col_values(19, 2)
        return ZDataPreprocessing.__diansc_P11T3_T6
    def get_meif_shuif(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meif_shuif = ds.col_values(20, 2)
        return ZDataPreprocessing.__meif_shuif
    def get_meif_hegqk1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meif_hegqk1 = ds.col_values(21, 2)
        return ZDataPreprocessing.__meif_hegqk1
    def get_meif_xid(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meif_xid = ds.col_values(22, 2)
        return ZDataPreprocessing.__meif_xid
    def get_meif_hegqk2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__meif_hegqk2 = ds.col_values(23, 2)
        return ZDataPreprocessing.__meif_hegqk2

    '''
        脱硫系统操作数据表获取函数
        filename5数据区域
        '''
    def get_xist_yanghfjyl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_yanghfjyl = ds.col_values(1, 2)
        return ZDataPreprocessing.__xist_yanghfjyl
    def get_xist_xunhbdl1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_xunhbdl1 = ds.col_values(2, 2)
        return ZDataPreprocessing.__xist_xunhbdl1
    def get_xist_xunhbdl2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_xunhbdl2 = ds.col_values(3, 2)
        return ZDataPreprocessing.__xist_xunhbdl2
    def get_xist_xunhbdl3(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_xunhbdl3 = ds.col_values(4, 2)
        return ZDataPreprocessing.__xist_xunhbdl3
    def get_xist_yal1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_yal1 = ds.col_values(5, 2)
        return ZDataPreprocessing.__xist_yal1
    def get_xist_yal2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_yal2 = ds.col_values(6, 2)
        return ZDataPreprocessing.__xist_yal2
    def get_xist_yew(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_yew = ds.col_values(7, 2)
        return ZDataPreprocessing.__xist_yew
    def get_xist_mid(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_mid = ds.col_values(8, 2)
        return ZDataPreprocessing.__xist_mid
    def get_xist_PH1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_PH1 = ds.col_values(9, 2)
        return ZDataPreprocessing.__xist_PH1
    def get_xist_PH2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__xist_PH2 = ds.col_values(10, 2)
        return ZDataPreprocessing.__xist_PH2
    def get_jiangwq_chongxyl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangwq_chongxyl = ds.col_values(11, 2)
        return ZDataPreprocessing.__jiangwq_chongxyl
    def get_jiangwq_yac(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangwq_yac = ds.col_values(12, 2)
        return ZDataPreprocessing.__jiangwq_yac
    def get_jiangwq_chongxsj(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangwq_chongxsj = ds.col_values(13, 2)
        return ZDataPreprocessing.__jiangwq_chongxsj
    def get_jiangwq_chongxjg(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangwq_chongxjg = ds.col_values(14, 2)
        return ZDataPreprocessing.__jiangwq_chongxjg
    def get_shigx_yew(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shigx_yew = ds.col_values(15, 2)
        return ZDataPreprocessing.__shigx_yew
    def get_shigx_liul(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__shigx_liul = ds.col_values(16, 2)
        return ZDataPreprocessing.__shigx_liul
    def get_jiangyx_yal1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangyx_yal1 = ds.col_values(17, 2)
        return ZDataPreprocessing.__jiangyx_yal1
    def get_jiangyx_yal2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangyx_yal2 = ds.col_values(18, 2)
        return ZDataPreprocessing.__jiangyx_yal2
    def get_jiangyx_yew(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangyx_yew = ds.col_values(19, 2)
        return ZDataPreprocessing.__jiangyx_yew
    def get_jiangyx_mid(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jiangyx_mid = ds.col_values(20, 2)
        return ZDataPreprocessing.__jiangyx_mid
    def get_chusgxt_xuanlqyl(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chusgxt_xuanlqyl = ds.col_values(21, 2)
        return ZDataPreprocessing.__chusgxt_xuanlqyl
    def get_chusgxt_lvbhd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chusgxt_lvbhd = ds.col_values(22, 2)
        return ZDataPreprocessing.__chusgxt_lvbhd
    def get_chusgxt_zhenkd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chusgxt_zhenkd = ds.col_values(23, 2)
        return ZDataPreprocessing.__chusgxt_zhenkd
    def get_jisk_yew(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__jisk_yew = ds.col_values(24, 2)
        return ZDataPreprocessing.__jisk_yew
    def get_gongysb_yew(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gongysb_yew = ds.col_values(25, 2)
        return ZDataPreprocessing.__gongysb_yew
    def get_gongysb_yal(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__gongysb_yal = ds.col_values(26, 2)
        return ZDataPreprocessing.__gongysb_yal
    def get_rukyq_xianyl1(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__rukyq_xianyl1 = ds.col_values(27, 2)
        return ZDataPreprocessing.__rukyq_xianyl1
    def get_rukyq_xianyl2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__rukyq_xianyl2 = ds.col_values(28, 2)
        return ZDataPreprocessing.__rukyq_xianyl2
    def get_rukyq_SO21(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__rukyq_SO21 = ds.col_values(29, 2)
        return ZDataPreprocessing.__rukyq_SO21
    def get_rukyq_SO22(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__rukyq_SO22 = ds.col_values(30, 2)
        return ZDataPreprocessing.__rukyq_SO22
    def get_chukyq_SO2nd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_SO2nd = ds.col_values(31, 2)
        return ZDataPreprocessing.__chukyq_SO2nd
    def get_chukyq_Noxnd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_Noxnd = ds.col_values(32, 2)
        return ZDataPreprocessing.__chukyq_Noxnd
    def get_chukyq_O2nd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_O2nd = ds.col_values(33, 2)
        return ZDataPreprocessing.__chukyq_O2nd
    def get_chukyq_wend(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_wend = ds.col_values(34, 2)
        return ZDataPreprocessing.__chukyq_wend
    def get_chukyq_yal(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_yal = ds.col_values(35, 2)
        return ZDataPreprocessing.__chukyq_yal
    def get_chukyq_lius(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_lius = ds.col_values(36, 2)
        return ZDataPreprocessing.__chukyq_lius
    def get_chukyq_kelwnd(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_kelwnd = ds.col_values(37, 2)
        return ZDataPreprocessing.__chukyq_kelwnd
    def get_chukyq_shid(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__chukyq_shid = ds.col_values(38, 2)
        return ZDataPreprocessing.__chukyq_shid
    def get_zhesz_SO2(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__zhesz_SO2 = ds.col_values(39, 2)
        return ZDataPreprocessing.__zhesz_SO2
    def get_zhesz_Nox(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__zhesz_Nox = ds.col_values(40, 2)
        return ZDataPreprocessing.__zhesz_Nox
    def get_zhesz_kelw(self):
        ds = ZDataPreprocessing.preparation(self)
        ZDataPreprocessing.__zhesz_kelw = ds.col_values(41, 2)
        return ZDataPreprocessing.__zhesz_kelw



class HDataPreProcessing:

    def preparation(self):
        filename = 'data-3days.xlsx'
        data = xlrd.open_workbook(filename)
        ds = data.sheet_by_name('Sheet1')
        return ds

    def get_Data(self):     #获取横向数据，统一存放在一个变量中
        ds = HDataPreProcessing().preparation()
        result = []
        for i in range(72):
            a = []
            for j in range(2,46):
                a.append(ds.cell_value(i+3,j))
            result.append(a)
        return result
