'''
考虑各种因素
'''
from provide_data_for_gui import *
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.linear_model import RidgeCV
from sklearn import ensemble
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
import xlrd
import numpy as np
import xlwt
from Tools import *
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.externals import joblib

def data_preprocess():
    cursor = Connect()

    filename = 'new_data.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet3')
    Date = read_sheet.col_values(0, 1)
    Time = read_sheet.col_values(1, 1)
    rehao = read_sheet.col_values(65, 1)

    Index = ['youlig', 'yijitwdA', 'yijityqA', 'yaoweiwd', 'fenjielwd', 'fenjielyq', 'yaotouyl']
    Result = []
    for index in Index:
        result = []
        for date, time in zip(Date, Time):
            sql = "SELECT %s FROM all_data WHERE date = '%s' and time = '%s'"\
                    % (index, str(date), str(time))
            if index == 'youlig':
                try:
                    cursor.execute(sql)
                    x = cursor.fetchall()[0][0]
                    if x == None or x > 100:  # 去除立升重的值
                        x = ''
                    result.append(x)
                except Exception as msg:
                    print(msg)
                    return False
            else:
                try:
                    cursor.execute(sql)
                    x = cursor.fetchall()[0][0]
                    if x == None:
                        x = ''
                    result.append(x)
                except Exception as msg:
                    print(msg)
                    return False
        Result.append(result)
    Result.append(rehao)

    '''delete
    Result_ = [Date, Time]
    Result_.extend(Result)
    '''

    Result = Delete_blank_more(Result)
    rehao = [Result[-1]]
    Result = Result[:-1]
    Result = list(map(list, zip(*Result)))
    rehao = list(map(list, zip(*rehao)))
    '''
    Result = pd.DataFrame(Result)
    x = [i for i in range(len(Index))]
    column = dict(zip(x, Index))
    Result.rename(columns=column, inplace=True)
    '''
    return Result, rehao


def create_pandas():
    Result, rehao = data_preprocess()
    Result = list(map(list, zip(*Result)))
    rehao = list(map(list, zip(*rehao)))
    Result.extend(rehao)
    Result = list(map(list, zip(*Result)))
    # print(Result)
    Index = ['youlig', 'yijitwdA', 'yijityqA', 'yaoweiwd', 'fenjielwd', 'fenjielyq', 'yaotouyl']
    Index.append('rehao')
    Result = pd.DataFrame(Result)
    x = [i for i in range(len(Index))]
    column = dict(zip(x, Index))
    Result.rename(columns=column, inplace=True)
    return Result


def d_youlig():
    x, y = data_preprocess()
    x = list(map(list, zip(*x)))
    x = x[0]
    x_ = [0]
    for i in range(1, len(x)):
        x_.append(x[i] - x[i-1])
    x = [x, x_]

    data = [x[0], x[1], list(map(list, zip(*y)))[0]]

    # print(x)
    x = list(map(list, zip(*x)))

    result = [[0]]
    for i in range(1, len(y)):
        result.append([y[i][0]-y[i-1][0]])
    data.append(list(map(list, zip(*result)))[0])
    return data

    # print(x, x_, [x[0] for x in result])
    '''         #三维立体图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, x_, [x[0] for x in result])
    plt.show()
    '''

    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.05, random_state=1)
    '''
    quadratic_featurizer = PolynomialFeatures(degree=2)
    train_x = quadratic_featurizer.fit_transform(train_x)
    test_x = quadratic_featurizer.transform(test_x)
    # print(train_x)
    clf = LinearRegression()
    '''

    clf = svm.SVR(kernel='rbf', epsilon=2, C=1000)

    clf.fit(train_x, train_y)
    predict_y = clf.predict(test_x)
    show_x = [i for i in range(len(test_y))]
    # print(clf.alpha_)
    print(test_y)
    print(predict_y)
    plt.plot(show_x, predict_y, color='r')
    plt.plot(show_x, test_y, color='b')
    plt.show()


def linear_model1():
    x, y = new_data()
    x = list(map(list, zip(*x)))
    y = list(map(list, zip(*y)))
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=10)

    '''     # 简单的线性模型
    clf = LinearRegression()
    clf.fit(train_x, train_y)
    predict_y = clf.predict(test_x)
    '''

    '''     # 正则化的线性模型
    ridgecv = RidgeCV(alphas=[0.01, 0.1, 0.5, 1, 2, 5, 10, 50, 100, 1000], cv=5)
    ridgecv.fit(train_x, train_y)
    predict_y = ridgecv.predict(test_x)
    print(ridgecv.alpha_)
    '''

             # 多项式的正则化曲线
    # quadratic_featurizer = PolynomialFeatures(degree=2)

    # print(test_x)
    # print(x1)
    # train_x = quadratic_featurizer.fit_transform(train_x)
    # test_X = quadratic_featurizer.transform(test_x)
    # print(test_x)

    # print(x1)
    # x1 = quadratic_featurizer.transform(test_x)
    ridgecv = svm.SVR(kernel='rbf', epsilon=2, C=100)
    ridgecv.fit(train_x, train_y)
    predict_y = ridgecv.predict(test_x)

    for i in range(len(test_x)):
        print(test_x[i][1])
        test_x[i][0] = test_x[i][0] + 0.1
        print(test_x[i][1])
        # print(x1[i][0], test_x[i][0])

    # print(ridgecv.alpha_)

    predict_y2 = ridgecv.predict(test_x)


    '''
    clf = svm.SVR()
    clf.fit(train_x, train_y)
    predict_y = clf.predict(test_x)
    '''

    '''    # 随机森林算法 + 网格搜索
    rf0 = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=10)
    rf0.fit(train_x, train_y)
    print(rf0.oob_score_)
    predict_y = rf0.predict(test_x)
    
    param_test = {'n_estimators': list(range(10, 101, 10))}
    gsearch1 = GridSearchCV(estimator=RandomForestRegressor(min_samples_split=20,
                                                             min_samples_leaf=2,
                                                             max_depth=8,
                                                             random_state=10),
                            param_grid=param_test, scoring='roc_auc', cv=5)
    gsearch1.fit(train_x, train_y)
    print(gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_)
    '''


    # print(ridgecv.score(test_x, test_y))
    # print(accuracy_score(test_y, predict_y))
    print(predict_y2)
    print(predict_y)
    show_x = [i for i in range(len(test_y))]
    plt.plot(show_x, predict_y2, color='y')
    plt.plot(show_x, predict_y, color='r')
    plt.plot(show_x, test_y, color='b')
    plt.show()


def time_rehao():
    filename = 'new_data.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet3')
    Date = read_sheet.col_values(0, 1)
    Time = read_sheet.col_values(1, 1)
    rehao = read_sheet.col_values(65, 1)
    # print(rehao)
    x = [i for i in range(len(rehao))]
    X = list(map(list, zip(*[x[:240]])))
    Y = list(map(list, zip(*[rehao[:240]])))
    test_x = list(map(list, zip(*[x[240:244]])))
    test_y = list(map(list, zip(*[rehao[240:244]])))

    quadratic_featurizer = PolynomialFeatures(degree=2)
    X = quadratic_featurizer.fit_transform(X)
    test_x = quadratic_featurizer.transform(test_x)
    clf = Ridge(alpha=1)

    clf.fit(X, Y)
    predict_y = clf.predict(test_x)
    # print(clf.alpha_)
    print(test_y)
    print(predict_y)
    show_x = [i for i in range(len(test_y))]
    plt.plot(show_x, test_y, color='b')
    plt.plot(show_x, predict_y, color='r')
    plt.show()


def provide_data_for_song():
    result = d_youlig()
    print(result)
    result = list(map(list, zip(*result)))
    result = pd.DataFrame(result)
    result.rename(columns={0:'Date', 1:'hour', 2:'youlig', 3:'d_youlig', 4:'rehao', 5:'d_rehao'}, inplace=True)
    print(result)
    result.to_excel('test_data.xls')


def new_data():
    filename = 'new_data.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet3')
    Date = read_sheet.col_values(0, 1)
    Time = read_sheet.col_values(1, 1)
    rehao = read_sheet.col_values(65, 1)
    youlig = read_sheet.col_values(5, 1)
    yijitwd = read_sheet.col_values(10, 1)
    yijityq = read_sheet.col_values(11, 1)
    for i in range(len(youlig)):
        # print(youlig[i])
        if youlig[i] == '' or youlig[i] > 100:
            youlig[i] = ''
        if rehao[i] == 0:
            rehao[i] = ''
        if yijityq[i] != '':
            yijityq[i] = -yijityq[i]
    Result = [youlig, yijitwd, yijityq, rehao]
    Result = Delete_blank_more(Result)

    return Result[:-1], [Result[-1]]


def create_model():         # 根据相关性挑选的几个特征来预测窑系统总的热耗
    filename = 'new_data.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet2')
    data_index = [7, 8, 10, 11, 12, 13, 25, 29, 38, 39, 40, 41, 64, 65]

    data = [read_sheet.col_values(i, 1) for i in data_index]
    for i in range(len(data[-1])):
        if data[-1][i] == 0 or data[-1][i] == 7:        # 这里的7是指DIV0
            data[-1][i] = ''
    # print(data[-1])
    data = Delete_blank_more(data)
    x = list(map(list, zip(* data[:-1])))
    y = data[-1]
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=1)
    # print(train_x)
    quadratic_featurizer = PolynomialFeatures(degree=2)
    train_x = quadratic_featurizer.fit_transform(train_x)
    test_x = quadratic_featurizer.transform(test_x)
    joblib.dump(quadratic_featurizer, 'rehao_degree_2.pkl')
    clf = Ridge(alpha=3.613)
    clf.fit(train_x, train_y)
    joblib.dump(clf, 'rehao_predict.pkl')
    '''
    predict_y = clf.predict(test_x)
    show_x = [i for i in range(len(predict_y))]
    # print(clf.alpha_)
    print(mean_squared_error(test_y, predict_y))
    # print(clf.alpha_)
    plt.plot(show_x, predict_y, color='r')
    plt.plot(show_x, test_y, color='b')
    plt.show()
    '''


def Production_warning_rehao(data_x):
    feature = ['yaotouc', 'yaoweic', 'yijitwdA', 'yijityqA', 'yijitwdB', 'yijityqB', 'sijityqB',
               'wujityqB', 'bilengjedS1', 'bilengjedI1', 'bilengjsdS1', 'bilengjsdI1', 'shuliaol']

    name = get_table_name()

    data = dict(zip(name, data_x))
    train_x = []
    for i in feature:
        train_x.append(data[i])
    # print(train_x)

    Translate = joblib.load('model\\rehao_degree_2.pkl')
    train_x = Translate.transform([train_x])

    model = joblib.load('model\\rehao_predict.pkl')
    return model.predict(train_x)

'''
if __name__ == "__main__":
    create_model()
    result = Production_warning_rehao(get_by_hour('2017020606')[1])
    print(result)
'''