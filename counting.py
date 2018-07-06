'''DataPreProcessing.py
~~~~~~~~~~~~
    修改内容：
        对所有已经录入的表格进行了数据访问优化
~~~~~~~~~~~~
    计算每个数据表，每个特征的均值和方差，在统计时自动跳过空白值，计算其他值的均值与方差，没有对其填补处理

~~~~~~~~~~~~
'''

# -*- coding: utf-8 -*-
from DataPreProcessing import *
from Tools import tongjl
import xlwt
import xlrd
from Tools import *


# 计算表一各项特征的均值
def get_Average2(filename):
    index = []
    if(ZDataPreprocessing(2,filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_chumsl_KH()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_chumsl_SM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_chumsl_IM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruysl_CaO()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruysl_Fe2O3()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruysl_KH()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruysl_SM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruysl_IM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_KH()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_SM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_IM()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_K2O()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_Na2O()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_shul_SO3()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruymf_shuf()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruymf_huif()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruymf_huiff()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruymf_rez()))
    index.append(tongjl().Average(ZDataPreprocessing(2,filename).get_ruymf_gudt()))
    return index    #计算表一各项特征的均值
# 计算表一各项特征的方差
def get_Fangc2(filename):
    index = []
    if (ZDataPreprocessing(2, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_chumsl_KH()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_chumsl_SM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_chumsl_IM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruysl_CaO()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruysl_Fe2O3()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruysl_KH()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruysl_SM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruysl_IM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_KH()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_SM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_IM()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_K2O()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_Na2O()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_shul_SO3()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruymf_shuf()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruymf_huif()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruymf_huiff()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruymf_rez()))
    index.append(tongjl().Fangc(ZDataPreprocessing(2, filename).get_ruymf_gudt()))
    print(index)
    return index
# 计算表二各项特征的均值
def get_Average1(filename):
    index = []
    if (ZDataPreprocessing(1, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_weilc()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_youlg()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yaos()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yaotc()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yaowc()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_tongt_wd()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yijt_wdA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yijt_yqA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yijt_wdB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yijt_yqB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_erjt_wdA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_erjt_yqA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_erjt_wdB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_erjt_yqB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sanjt_wdA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sanjt_yqA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sanjt_wdB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sanjt_yqB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sijt_wdA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sijt_yqA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sijt_wdB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sijt_yqB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_wujt_wdA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_wujt_yqA()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_wujt_wdB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_wujt_yqB()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yaow_wd()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_fenjl_wd()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_fenjl_yq()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yicfj()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_yaotyl_yq()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_ydyl()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_ydS1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_ydI1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_erdS1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_erdI1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_sandS1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_bilj_sandI1()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_sancf_yl()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_gaowfj_zs()))
    index.append(tongjl().Average(ZDataPreprocessing(1,filename).get_gaowfj_dl()))
    print(index)
    return index
# 计算表二各项特征的方差
def get_Fangc1(filename):
    index = []
    if (ZDataPreprocessing(1, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_weilc()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_youlg()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yaos()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yaotc()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yaowc()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_tongt_wd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yijt_wdA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yijt_yqA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yijt_wdB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yijt_yqB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_erjt_wdA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_erjt_yqA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_erjt_wdB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_erjt_yqB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sanjt_wdA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sanjt_yqA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sanjt_wdB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sanjt_yqB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sijt_wdA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sijt_yqA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sijt_wdB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sijt_yqB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_wujt_wdA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_wujt_yqA()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_wujt_wdB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_wujt_yqB()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yaow_wd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_fenjl_wd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_fenjl_yq()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yicfj()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_yaotyl_yq()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_ydyl()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_ydS1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_ydI1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_erdS1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_erdI1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_sandS1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_bilj_sandI1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_sancf_yl()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_gaowfj_zs()))
    index.append(tongjl().Fangc(ZDataPreprocessing(1, filename).get_gaowfj_dl()))
    print(index)
    return index
# 计算表三各项特征的均值
def get_Average3(filename):
    index = []
    if (ZDataPreprocessing(3, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Average(ZDataPreprocessing(3,filename).get_AO5F01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_lisz()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_youlg1()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_w01S01rpm()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_v72F01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_v82F01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_tongt_wd1()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A51P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A51T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A51P02()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A52P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A52T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A52P02()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A53P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A53T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A53P02()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A54P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A54T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A54P02()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A54T02()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A55P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A55T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_A56T01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_yans_W01_A01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_yans_W01_P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_yans_W01_t01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_v91p01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_W1p01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_dianscjkfm()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K02Tmax()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K02SI()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K02II()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K01PI()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K11PI()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K12PI()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_bilj_K13PI()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_sancfgA58P01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_gaowfjJ01z01()))
    index.append(tongjl().Average(ZDataPreprocessing(3, filename).get_gaowfjJ02SI()))
    print(index)
    return index
# 计算表三各项特征的方差
def get_Fangc3(filename):
    index = []
    rawdata = []
    if (ZDataPreprocessing(3, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_AO5F01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_lisz()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_youlg1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_w01S01rpm()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_v72F01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_v82F01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_tongt_wd1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A51P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A51T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A51P02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A52P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A52T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A52P02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A53P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A53T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A53P02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A54P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A54T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A54P02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A54T02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A55P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A55T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_A56T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_yans_W01_A01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_yans_W01_P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_yans_W01_t01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_v91p01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_W1p01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_dianscjkfm()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K02Tmax()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K02SI()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K02II()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K01PI()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K11PI()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K12PI()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_bilj_K13PI()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_sancfgA58P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_gaowfjJ01z01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(3, filename).get_gaowfjJ02SI()))
    print(index)
    return index
# 计算表四各项特征的均值
def get_Average4(filename):
    index = []
    if (ZDataPreprocessing(4, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Average(ZDataPreprocessing(4,filename).get_weil_A01F01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M01X01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M03I01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M01P01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M01P02()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M01T01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_moj_M01T02()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_cufflq_S01P01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_cufflq_S01T01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_fengj_S04Z01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_fengj_S05I01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_fengj_S04Z01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_fengj_S05I01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meifc_L11T01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meifc_L11l01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meifc_L21T01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meifc_L21L01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_dianscmfc_P11A01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_diansc_P11T01()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_diansc_P11T02()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_diansc_P11T3_T6()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meif_shuif()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meif_hegqk1()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meif_xid()))
    index.append(tongjl().Average(ZDataPreprocessing(4, filename).get_meif_hegqk2()))
    print(index)
    return index
# 计算表四各项特征的方差
def get_Fangc4(filename):
    index = []
    if (ZDataPreprocessing(4, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_weil_A01F01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M01X01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M03I01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M01P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M01P02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M01T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_moj_M01T02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_cufflq_S01P01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_cufflq_S01T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_fengj_S04Z01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_fengj_S05I01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_fengj_S04Z01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_fengj_S05I01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meifc_L11T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meifc_L11l01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meifc_L21T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meifc_L21L01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_dianscmfc_P11A01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_diansc_P11T01()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_diansc_P11T02()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_diansc_P11T3_T6()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meif_shuif()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meif_hegqk1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meif_xid()))
    index.append(tongjl().Fangc(ZDataPreprocessing(4, filename).get_meif_hegqk2()))
    print(index)
    return index
# 计算表五各项特征的均值
def get_Average5(filename):
    index = []
    if (ZDataPreprocessing(5, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Average(ZDataPreprocessing(5,filename).get_xist_yanghfjyl()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_xunhbdl1()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_xunhbdl2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_xunhbdl3()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_yal1()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_yal2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_yew()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_mid()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_PH1()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_xist_PH2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangwq_chongxyl()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangwq_yac()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangwq_chongxsj()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangwq_chongxjg()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_shigx_yew()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_shigx_liul()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangyx_yal1()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangyx_yal2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangyx_yew()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jiangyx_mid()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chusgxt_xuanlqyl()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chusgxt_lvbhd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chusgxt_zhenkd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_jisk_yew()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_gongysb_yew()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_gongysb_yal()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_rukyq_xianyl1()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_rukyq_xianyl2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_rukyq_SO21()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_rukyq_SO22()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_SO2nd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_Noxnd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_O2nd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_wend()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_yal()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_lius()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_kelwnd()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_chukyq_shid()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_zhesz_SO2()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_zhesz_Nox()))
    index.append(tongjl().Average(ZDataPreprocessing(5, filename).get_zhesz_kelw()))
    print(index)
    return index
# 计算表五各项特征的方差
def get_Fangc5(filename):
    index = []
    if (ZDataPreprocessing(5, filename).preparation() == 0):
        return 'null'
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_yanghfjyl()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_xunhbdl1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_xunhbdl2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_xunhbdl3()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_yal1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_yal2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_yew()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_mid()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_PH1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_xist_PH2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangwq_chongxyl()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangwq_yac()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangwq_chongxsj()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangwq_chongxjg()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_shigx_yew()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_shigx_liul()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangyx_yal1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangyx_yal2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangyx_yew()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jiangyx_mid()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chusgxt_xuanlqyl()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chusgxt_lvbhd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chusgxt_zhenkd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_jisk_yew()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_gongysb_yew()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_gongysb_yal()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_rukyq_xianyl1()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_rukyq_xianyl2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_rukyq_SO21()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_rukyq_SO22()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_SO2nd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_Noxnd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_O2nd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_wend()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_yal()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_lius()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_kelwnd()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_chukyq_shid()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_zhesz_SO2()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_zhesz_Nox()))
    index.append(tongjl().Fangc(ZDataPreprocessing(5, filename).get_zhesz_kelw()))
    print(index)
    return index



if __name__ == '__main__':              #主函数
    filename = '一线窑操作记录20170128.xlsx'
    oldwd = xlrd.open_workbook(filename)
    sheets = oldwd.sheet_by_name('Sheet1')
    workbook = xlwt.Workbook('')
    sheet1 = workbook.add_sheet("average")
    sheet2 = workbook.add_sheet("Fangc")
    workbook.save('数值表.xls')

    i = 0
    while (filename != '一线窑操作记录20170304.xlsx'):
        print(filename)
        index1 = get_Average3(filename)
        if(index1 == 'null'):
            filename = date().DateIncreases(filename)
            continue
        index2 = get_Fangc3(filename)
        sheet1.write(i, 0, filename[filename.index(".")-8:filename.index(".")])         #书写表头，标明日期
        sheet2.write(i, 0, filename[filename.index(".")-8:filename.index(".")])
        filename = date().DateIncreases(filename)
        i = i + 1
    workbook.save('数值表.xls')
    print("Ending")
