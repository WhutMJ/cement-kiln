"""
@author: {junmou}
integrate all models for easy invocation
"""

import tensorflow as tf
from sklearn.externals import joblib
from provide_data_for_gui import *

def predict_sanlvz(input_data):
    """
    :param input_data: dict
    :return: dict, KH, SM, IM
    """
    if None in input_data:
        return False
    path = 'sanlvz_model/'
    suffix = '.pkl'
    output_name = ['KH', 'SM', 'IM']
    # 计算KH
    kh_model_name = path + 'BayesRidge-KH' + suffix
    clf_kh = joblib.load(kh_model_name)
    predict_kh = round(clf_kh.predict(input_data)[0], 2)

    # 计算SM
    sm_model_name = path + 'Bayes-SM' + suffix
    clf_sm = joblib.load(sm_model_name)
    predict_sm = round(clf_sm.predict(input_data)[0], 2)

    # 计算IM
    predict_im = 0
    model_name = ['LinearRegression-IM', 'Bayes-IM', 'BayesRidge-IM']
    for i in range(len(model_name)):
        im_model_name = path + model_name[i] + suffix
        clf_im = joblib.load(im_model_name)
        predict_im += clf_im.predict(input_data)[0]
    predict_im /= 3
    predict_im = round(predict_im, 2)
    output = dict(zip(output_name, [predict_kh, predict_sm, predict_im]))
    return output


def add_layer(xs, input_size, output_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([input_size, output_size]))
    biases = tf.Variable(tf.zeros([1, output_size]) + 0.1)
    Wx_plus_b = tf.matmul(xs, Weights) + biases     # 神经网络得到的目标函数
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def predict_yaotou_yaowei_c(input_data):
    """
    窑头秤和窑尾秤的预测
    :param input_data:
    :return:
    """
    xs = tf.placeholder(tf.float32, [None, 6])  # 占位符
    hidden_l = add_layer(xs, 6, 5, activation_function=tf.nn.relu)
    output_l = add_layer(hidden_l, 5, 1)
    saver = tf.train.Saver(max_to_keep=1)  # 默认保存最后一代
    with tf.Session() as sess:
        model_file = tf.train.latest_checkpoint('ckpt/')
        saver.restore(sess, model_file)
        intent_prediction1 = [round(x[0], 2) for x in sess.run(output_l, feed_dict={xs: input_data})]
    with tf.Session() as sess:
        model_file = tf.train.latest_checkpoint('ckpt3/')
        saver.restore(sess, model_file)
        intent_prediction2 = [round(x[0], 2) for x in sess.run(output_l, feed_dict={xs: input_data})]
    output = dict(zip(['yaotouc', 'yaoweic'], [intent_prediction1, intent_prediction2]))
    return output


def predict_yijit(input_data):
    """
    预测一级筒各项指标
    :param input_data:
    :return:
    """
    tf.reset_default_graph()
    xs = tf.placeholder(tf.float32, [None, 2])  # 占位符
    hidden_l = add_layer(xs, 2, 5, activation_function=tf.nn.relu)
    output_l = add_layer(hidden_l, 5, 4)
    saver = tf.train.Saver(max_to_keep=1)  # 默认保存最后一代
    with tf.Session() as sess:
        model_file = tf.train.latest_checkpoint('ckpt2/')
        saver.restore(sess, model_file)
        intent_prediction = []
        for input_x in list(map(list, zip(*sess.run(output_l, feed_dict={xs: input_data})))):
            intent_prediction.append([round(x, 2) for x in input_x])
    output = dict(zip(['yijitwdA', 'yijityqA', 'yijitwdB', 'yijityqB'], intent_prediction))
    return output


def predict_for_rexiaolv(test_x):
    quadratic_featurizer = joblib.load('rexiaol_model/rexiaolv_degree_2.pkl')
    test_x = quadratic_featurizer.transform(test_x)
    # print(test_x)
    model = joblib.load('rexiaol_model/predict_for_rexiaolv.pkl')
    predict_y = model.predict(test_x)[0]
    '''
        show_x = [i for i in range(len(test_x))]
        plt.plot(show_x, predict_y, color='r')
        plt.plot(show_x, test_y, color='b')
        plt.show()
        '''
    return {'rexiaol': round(predict_y, 2)}


def predict_rehao(input_data):
    Translate = joblib.load('rehao_model/rehao_degree_2.pkl')
    train_x = Translate.transform(input_data)

    model = joblib.load('rehao_model/rehao_predict.pkl')
    output = model.predict(train_x)[0]
    return {'rehao': round(output, 2)}


def predict_youlig(input_data):
    model = joblib.load('youlig_model/RandomForest_for_youlg.pkl')
    y = model.predict_proba(input_data)
    y = list(y[0])
    y = [round(x, 4) for x in y]#
    return {'youlig': y}


def production_warning(date, time):
    """
    给外界调用的接口
    :param date: 数据的日期
    :param time: 数据的时间
    :return: 所有预测数据
    """
    data = get_by_hour(date+time)
    historical_data = get_by_fragment2('2017022310', 5)[0]
    historical_data = list(map(list, zip(*historical_data)))
    historical_data = dict(zip(data[0], historical_data))
    data = dict(zip(data[0], data[1]))
    # print(data)
    sanlvz_name = ['fenjielwd', 'fenjielyq', 'chumoslKH', 'chumoslSM', 'chumoslIM']
    yaotou_yaoweic_name = ['sanjityqA', 'sijityqA', 'erjityqB', 'yijityqB', 'wujityqA', 'yijityqA']
    yijit_name = ['yaotouc', 'yaoweic']
    rexiaol_name = ['erjityqB', 'sanjityqA', 'sanjityqB', 'sijityqA', 'wujitwdA', 'wujityqA', 'wujitwdB',
                  'bilengjedS1']
    rehao_name = ['yaotouc', 'yaoweic', 'yijitwdA', 'yijityqA', 'yijitwdB', 'yijityqB', 'sijityqB',
               'wujityqB', 'bilengjedS1', 'bilengjedI1', 'bilengjsdS1', 'bilengjsdI1', 'shuliaol']
    youlig_name = ['fenjielwd', 'fenjielyq', 'chumoslKH', 'chumoslSM', 'chumoslIM', 'shuliaoKH', 'shuliaoSM', 'shuliaoIM']

    sanlvz_input = [[data[i] for i in sanlvz_name]]
    yaotou_yaoweic_input = list(map(list, zip(*[historical_data[i] for i in yaotou_yaoweic_name])))
    yijit_input = list(map(list, zip(*[historical_data[i] for i in yijit_name])))
    rexiaol_input = [[data[i] for i in rexiaol_name]]
    rehao_input = [[data[i] for i in rehao_name]]
    youlig_input = [[data[i] for i in youlig_name]]

    # print(sanlvz_input)
    # print(yaotou_yaoweic_input)
    # print(yijit_input)

    # 调用模型
    output = []
    output.append(predict_sanlvz(sanlvz_input))
    output.append(predict_yaotou_yaowei_c(yaotou_yaoweic_input))
    output.append(predict_yijit(yijit_input))
    output.append(predict_for_rexiaolv(rexiaol_input))
    output.append(predict_rehao(rehao_input))
    output.append(predict_youlig(youlig_input))
    # print(output)

    modual_name = ['sanlvz', 'yaotou_yaoweic', 'yijit', 'rexfiaol', 'rehao', 'youlig']
    output = dict(zip(modual_name, output))
    print(output)

    # 输出真实值
    real_modual = ['yaotou_yaoweic', 'yijit', 'rehao']
    real_data1 = [historical_data['yaotouc'], historical_data['yaoweic']]
    real_data2 = [historical_data['yijitwdA'], historical_data['yijityqA'], historical_data['yijitwdB'], historical_data['yijityqB']]
    real_dict2 = dict(zip(['yijitwdA', 'yijityqA', 'yijitwdB', 'yijityqB'], real_data2))
    real_dict1 = dict(zip(['yaotouc', 'yaoweic'], real_data1))
    real_dict = dict(zip(real_modual, [real_dict1, real_dict2, historical_data['rehao']]))
    print(real_dict)
    return output, real_dict


if __name__ == "__main__":
    production_warning('20170223','10')