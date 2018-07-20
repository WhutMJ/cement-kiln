import xlrd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from Tools import *
import matplotlib.pyplot as plt


def linear_model():
    filename = '三线总表.xlsx'
    workfile = xlrd.open_workbook(filename)
    readsheet = workfile.sheet_by_name('Sheet3')
    data_x_index = [10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 26, 27, 29, 39, 40, 66]
    data_x = []
    for index in data_x_index:
        data = readsheet.col_values(index, 1)
        data_x.append(data)
    #   print(data_x)
    data_x = Delete_blank_more(data_x)
    data_y = data_x[len(data_x_index) - 1]
    data_x = data_x[:len(data_x_index)-1]
    data_x = list(map(list, zip(*data_x)))
    print(data_x)
    #  print(len(data_x[1]), len(data_x[2]))
    clf = LinearRegression()
    train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.05, random_state=62)
    clf.fit(train_x, train_y)
    print(clf.coef_)
    predict_y = clf.predict(test_x)
    print(test_y)
    print(predict_y)
    x = [i for i in range(len(test_y))]
    plt.plot(x, test_y, color='r')
    plt.plot(x, predict_y, color='b')
    plt.show()


if __name__ == '__main__':
    linear_model()