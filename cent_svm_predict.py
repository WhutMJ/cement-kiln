from sklearn.externals import joblib
import xlrd
import xlwt
import numpy as np
from Tools import *
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.grid_search import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
from provide_data_for_gui import *


def create_model():
    filename = 'new_data.xlsx'
    readfile = xlrd.open_workbook(filename)
    read_sheet = readfile.sheet_by_name('Sheet2')

    rehao = read_sheet.col_values(67, 1)

    yaoweic = read_sheet.col_values(8, 1)
    wujitwdA = read_sheet.col_values(26, 1)
    wujitwdB = read_sheet.col_values(28, 1)
    yaoweiwd = read_sheet.col_values(30, 1)
    fenjielwd = read_sheet.col_values(31, 1)
    fenjielyq = read_sheet.col_values(32, 1)
    shuliao = read_sheet.col_values(64, 1)

    for i in range(len(rehao)):
        if rehao[i] == 0 or rehao[i] == 7:
            rehao[i] = ''
    # print(rehao)
    Result = Delete_blank_more([yaoweic, wujitwdA, wujitwdB, yaoweiwd, fenjielwd, fenjielyq, shuliao, rehao])
    y = Result[-1]
    Result = list(map(list, zip(* Result[:-1])))

    # print(y)

    '''
    for i in range(len(shuliao)):
        if shuliao[i] == 0:
            shuliao[i] = ''
    Result = [yaowc, rezhi, shuliao]
    rehao = []
    for i in range(len(Result[0])):
        if yaowc == '' or rezhi == '' or shuliao == '':
            rehao.append('')
        else:
            rehao.append(Result[0][i] * Result[1][i] * 29307 / (7000 * Result[2][i]))
    # print(rehao)
    writefile = xlwt.Workbook()
    writesheet = writefile.add_sheet('Sheet1')
    writefile.save('cent_svm.xls')

    for i in range(len(rehao)):
        writesheet.write(i, 0, rehao[i])

    writefile.save('cent_svm.xls')

    x = list(map(list, zip(*Result)))
    '''

    train_x, test_x, train_y, test_y = train_test_split(Result, y, test_size=0.05, random_state=10)

    '''创建模型'''
    # print(train_x)
    # print(train_y)
    # clf = svm.SVR(kernel='poly', epsilon=2, C=100)
    '''
    quadratic_featurizer = PolynomialFeatures(degree=2)
    X_train_quadratic = quadratic_featurizer.fit_transform(train_x)
    X_test_quadratic = quadratic_featurizer.transform(test_x)
    '''
    # clf = KNeighborsRegressor(n_neighbors=2)

    clf = RandomForestRegressor(n_estimators=20,
                                max_depth=13,
                                min_samples_split=10,
                                min_samples_leaf=1,
                                random_state=10,
                                max_features=4)


    '''
    param_test = {'max_features': list(range(1, 6, 1))}
    gsearch = GridSearchCV(estimator=RandomForestRegressor(n_estimators=20,
                                                           max_depth=13,
                                                           min_samples_split=10,
                                                           min_samples_leaf=1,
                                                           random_state=10),
                           param_grid=param_test,
                           cv=5,
                           scoring='neg_mean_squared_error')

    gsearch.fit(train_x, train_y)
    print(gsearch.grid_scores_, gsearch.best_params_, gsearch.best_score_)
    '''

    # clf = RidgeCV(alphas=[0.01, 0.1, 0.5, 1, 2, 5, 10, 20, 100], cv=5)

    clf.fit(train_x, train_y)
    # predict_y = clf.predict(test_x)
    joblib.dump(clf, 'cent_svm.pkl')
    '''
    show_x = [i for i in range(len(predict_y))]
    # print(clf.alpha_)
    print(test_y)
    print(predict_y)
    print(mean_squared_error(test_y, predict_y))
    plt.plot(show_x, predict_y, color='r')
    plt.plot(show_x, test_y, color='b')
    plt.show()
    '''
    '''
    param_test = {'kernel': ['linear', 'rbf'],
                  'epsilon': np.linspace(0.1, 3, 10),
                  'C': np.linspace(10, 100, 10)}

    gsearch = GridSearchCV(estimator=clf,
                           param_grid=param_test,
                           cv=5,
                           scoring='neg_mean_squared_error')

    gsearch.fit(train_x, train_y)
    print(gsearch.grid_scores_, gsearch.best_params_, gsearch.best_score_)
    '''


def Production_warning_fenjielu(data_x):
    '''
    :param data_x: 直接可以输入get_by_hour的数据部分
    :return:
    '''

    feature = ['yaoweic', 'wujitwdA', 'wujitwdB', 'yaoweiwd', 'fenjielwd', 'fenjielyq', 'shuliaol']

    name = get_table_name()

    data = dict(zip(name, data_x))
    train_x = []
    for i in feature:
        train_x.append(data[i])
    print(train_x)

    train_x = [train_x]

    model = joblib.load('model\\cent_svm.pkl')
    return model.predict(train_x)

'''
if __name__ == "__main__":
    result = predict(get_by_hour('2017020606')[1])
    print(result)
'''