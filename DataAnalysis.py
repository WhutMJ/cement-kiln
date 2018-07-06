  """
#数据分析库1_2
-----------------------
    做了cart,knn,层次聚类，random_forest算法的接口（在第二个类MLAlgorithm中）
    做了naive_bayes,adaboost,bagging算法的对具体问题的实现，暂未编写接口
"""


# -*- coding: utf-8 -*-
import xlrd
from sklearn.naive_bayes import GaussianNB
import xlwt
import numpy as np
from DataPreProcessing import *
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals.six import StringIO
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cluster import AgglomerativeClustering     #层次聚类
import pydotplus
import pickle


class DataAnalysis: #实例
    __static_a = []
    __static_ds_x_train = []
    __static_ds_y_train = []
    __static_ds_x_test = []
    __static_ds_y_test = []

    def __init__(self):
        DataAnalysis.__static_ds_y_test = [DataAnalysis.__static_a for i in range(48)]
        DataAnalysis.__static_ds_y_train = [DataAnalysis.__static_a for i in range(24)]

    def preparation(self):
        filename = 'data-3days.xlsx'
        data = xlrd.open_workbook(filename)
        ds = data.sheet_by_name('Sheet1')
        line = [8, 10, 13, 17, 21, 29, 31, 32, 33, 37, 38, 39, 40, 41, 42]
        a = []
        Rawdataset = [a for x in range(len(line))]
        for i in range(0, len(line)):
            Rawdataset[i] = ds.col_values(line[i], 3)
        for i in range(len(Rawdataset[0])):
            if Rawdataset[0][i] < 14:
                Rawdataset[0][i] = 1
            else:
                Rawdataset[0][i] = 2
        # Rawdataset是每一列数据的集合
        # print (Rawdataset)
        datasetx = [a for y in range(72)]
        datasety = []
        for j in range(72):
            datasetx[j] = [Rawdataset[i][j] for i in range(1, len(Rawdataset))]
            datasety.append(Rawdataset[0][j])
            print(datasetx[j])

        DataAnalysis.__static_ds_x_train = datasetx[:24]
        DataAnalysis.__static_ds_y_train = datasety[:24]
        print(DataAnalysis.__static_ds_y_train)
        DataAnalysis.__static_ds_x_test = datasetx[24:]
        DataAnalysis.__static_ds_y_test = datasety[24:]


    def Naive_bayes(self):
        DataAnalysis().preparation()
        nb = GaussianNB()
        nb.fit(DataAnalysis.__static_ds_x_train, DataAnalysis.__static_ds_y_train)
        ds_y_predict = nb.predict(DataAnalysis.__static_ds_x_test)
        score1 = nb.score(DataAnalysis.__static_ds_x_train, DataAnalysis.__static_ds_y_train)
        score2 = nb.score(DataAnalysis.__static_ds_x_test, DataAnalysis.__static_ds_y_test)
        print('预测=', ds_y_predict)
        print('测试=', DataAnalysis.__static_ds_y_test)
        print('训练数据准确率=', score1)
        print('测试数据准确率=', score2)
        return ds_y_predict

    def Adaboost(self):
        DataAnalysis().preparation()
        bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                                 algorithm="SAMME", n_estimators=50, learning_rate=0.6)
        bdt.fit(DataAnalysis.__static_ds_x_train, DataAnalysis.__static_ds_y_train)
        z = bdt.predict(DataAnalysis.__static_ds_x_test)
        score = bdt.score(DataAnalysis.__static_ds_x_test, DataAnalysis.__static_ds_y_test)
        print(z)
        print(score)

    def Bagging(self):
        DataAnalysis().preparation()
        Bag = BaggingClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                                n_estimators=100,max_samples=0.5,max_features=0.5)
        Bag.fit(DataAnalysis.__static_ds_x_train, DataAnalysis.__static_ds_y_train)
        z = Bag.predict(DataAnalysis.__static_ds_x_test)
        score = Bag.score(DataAnalysis.__static_ds_x_test, DataAnalysis.__static_ds_y_test)
        print(z)
        print(score)

class MLAlgorithm:              #机器学习方法类
    def CART(self,datasetX):#datasetX为多维数组，其中最后一列是分类结果即labels
        '''datasetX 例子：datasetX=[['vhigh','vhigh',2,2,'small','low','unacc'],
                                    ['vhigh','vhigh',2,2,'small','med','good'],
                                    ['vhigh','vhigh',2,2,'small','high','unacc'],
                                    ['vhigh','vhigh',2,2,'med','low','vgood']]'''
        data = []
        labels = []
        rowDict = {}  # data需要是字典形式，因为之后需要使用DictVectorizer()修改字符串数据类型，以便符合DecisionTreeClassifier()
        for row in datasetX:
            count = 0
            for i in range(len(row)):
                count+=1
                col='column'+'%d'%count
                rowDict[col] = row[i]
            data.append(rowDict)
            labels.append(row[-1])  # 分割数据，将label与data分开
        x = np.array(data)
        labels = np.array(labels)
        y = np.zeros(labels.shape)  # 初始label全为0

        y[labels == 'vgood'] = 1  # 当label等于这三种属性的话，设置为1。
        y[labels == 'good'] = 1
        y[labels == 'acc'] = 1

        vec = DictVectorizer()  # 转换字符串数据类型
        dx = vec.fit_transform(x).toarray()
        # print(dx[:5])#调试用
        # print(vec.get_feature_names())

        clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=7, min_samples_split=20,
                                          min_samples_leaf=10)  # CART算法，使用Gini作为标准

        clf = clf.fit(dx, y)  # 导入数据
        print(clf)
        with open("tree.dot", 'w') as f:
            f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)  # 输出结果至文件
            print(vec.get_feature_names(),f)
        dot_data = StringIO()
        tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=dot_data)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_pdf("tree.pdf")

    def Random_forest_train(self,iris_train_X,iris_train_Y,n_estimators):
        #clf = RandomForestClassifier(n_estimators=10)  #此为随机森林分类器
        clf= ExtraTreesClassifier(n_estimators)         #此为极端森林分类器，更强
        clf.fit(iris_train_X,iris_train_Y)
        with open("random_forest.pkl", "wb") as file:  # 将分类器保存进文件
            pickle.dump(clf, file)
    def Random_forest_predict(self,iris_test_X):
        with open("random_forest.pkl", "rb")  as file:  # 从文件中读取分类器
            clf = pickle.load(file)
        y_pre = clf.predict(iris_test_X)
        return y_pre

    def KNN_train(self,iris_train_X,iris_train_Y,n_neighbors=2):
       clf= KNeighborsClassifier(n_neighbors)
       clf.fit(iris_train_X, iris_train_Y)
       with open ("knn.pkl","wb") as file:   #将分类器保存进文件
            pickle.dump(clf,file)
    def KNN_predict(self,iris_test_X):
        with open("knn.pkl","rb")  as file:  #从文件中读取分类器
            clf = pickle.load(file)
        iris_Y_pred = clf.predict(iris_test_X)
        return iris_Y_pred

    def K_means_train(self, datasetX = [], k=1):
        clf = KMeans(n_clusters=k)    #clf为分类器
        s = clf.fit(datasetX)
        with open ("k_means.pkl","wb") as file:   #将分类器保存进文件
            pickle.dump(clf,file)
        return clf
    def K_means_predict(self, datasetX = []):
        with open("k_means.pkl","rb")  as file:  #从文件中读取分类器
            clf = pickle.load(file)
        y_pre = clf.predict(datasetX)
        return y_pre

    def Hierarchical_train(self,iris,n_clusters):
       #clf = AgglomerativeClustering(n_clusters=n_clusters, affinity="precomputed", linkage='average')
       clf = AgglomerativeClustering(n_clusters=n_clusters)
       clf.fit(iris)
       with open("hierarchical.pkl", "wb") as file:  # 将分类器保存进文件
           pickle.dump(clf, file)
    def Hierarchical_predict(self,predict_X):
        with open("hierarchical.pkl", "rb") as file:  # 将分类器保存进文件
            clf = pickle.load(file)
        pre_Y = clf.fit_predict(predict_X)
        return pre_Y
