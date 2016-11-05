
import os
import sys
import commands
from hackthon_eleme_data_structure import *
from hackthon_eleme_data_loading import *
from hackthon_eleme_data_joining import *
from hackthon_eleme_feature_engineering import *

# DEFINE MACRO
USER_CLK_THRESHOLD = 0.10
USER_BUY_THRESHOLD = 0.05



def splitData(data_file_path, train_file_path, test_file_path):
    with open(data_file_path, 'r') as fi:
        with open(train_file_path, 'w') as fo1:
            with open(test_file_path, 'w') as fo2:
                for line in fi:
                    elements = line.rstrip().split('\t')
                    day_no = int(elements[11].split(':')[1])
                    if day_no > 120:
                        fo2.write(line)
                    else:
                        fo1.write(line)
    # os.popen('cat {0} |'.format(data_file_path) +
    #          "awk '{if(NR%5==1) print $0}'" +
    #          '> {0}'.format(test_file_path)
    #          )
    # os.popen('cat {0} |'.format(data_file_path) +
    #          "awk '{if(NR%5!=1) print $0}'" +
    #          '> {0}'.format(train_file_path)
    #          )


def trainTest(configuration):
    output = os.popen('xgboost {0}.conf '.format(configuration))



def predict(configuration, model_in, prediction_file):
    output = os.popen('xgboost {0}.conf task=pred model_in="{1}" test:data="{2}"'.format(configuration, model_in, prediction_file))



if __name__ == '__main__':

    file_path_prefix = '{0}/'.format(sys.argv[1])
    output_prefix = ''

    file_his_eco_env_path = file_path_prefix+'his_eco_env.txt'
    file_his_eco_info_path = file_path_prefix+'his_eco_info.txt'
    file_order_info_path = file_path_prefix+'his_order_info.txt'
    file_rst_info_path = file_path_prefix+'rst_info.txt'
    file_nxt_eco_env_path = file_path_prefix+'next_eco_env.txt'
    file_nxt_eco_info_path = file_path_prefix+'next_eco_info.txt'

    output_file_clk = output_prefix+'output_clk.txt'
    output_file_buy = output_prefix+'output_buy.txt'
    output_file_clk_feat_eng = output_prefix+'output_file_clk_feat_eng.txt'
    output_file_buy_feat_eng = output_prefix+'output_file_buy_feat_eng.txt'
    output_file_nxt = output_prefix+'output_nxt.txt'
    output_file_nxt_feat_eng = output_prefix+'output_nxt_feat_eng.txt'

    feat_map_file = output_prefix+'feat_map_file.txt'
    train_raw_path = output_prefix+'raw_train_data.txt'
    test_raw_path = output_prefix+'raw_test_data.txt'
    train_file_path = output_prefix+'e_data.txt.train'
    test_file_path = output_prefix+'e_data.txt.test'

    job = DataJoining(file_his_eco_env_path,
                      file_his_eco_info_path,
                      file_order_info_path,
                      file_rst_info_path,
                      file_nxt_eco_env_path,
                      file_nxt_eco_info_path,
                      output_file_clk,
                      output_file_buy,
                      output_file_nxt)

    job.joinData()

    # traing clk
    splitData(data_file_path=output_file_clk,
              train_file_path=train_raw_path,
              test_file_path=test_raw_path)
    feature_engineering(input_file=train_raw_path,
                        output_file=train_file_path + 'clk',
                        feat_map_file=feat_map_file)
    feature_engineering(input_file=test_raw_path,
                        output_file=test_file_path + 'clk',
                        feat_map_file=feat_map_file)
    trainTest(configuration='configuration_clk')

    # traing buy
    splitData(data_file_path=output_file_buy,
              train_file_path=train_raw_path,
              test_file_path=test_raw_path)
    feature_engineering(input_file=train_raw_path,
                        output_file=train_file_path + 'buy',
                        feat_map_file=feat_map_file)
    feature_engineering(input_file=test_raw_path,
                        output_file=test_file_path + 'buy',
                        feat_map_file=feat_map_file)
    trainTest(configuration='configuration_buy')

    # predict nxt
    feature_engineering(output_file_nxt, output_file_nxt_feat_eng, feat_map_file)
    predict(configuration='configuration_clk',
            model_in='clk_mdl.model',
            prediction_file=output_file_nxt_feat_eng)
    predict(configuration='configuration_buy',
            model_in='buy_mdl.model',
            prediction_file=output_file_nxt_feat_eng)


 ###############################################################################################
    clk_probabilty = []
    with open('pred_clk.txt', 'r') as fi:
        for line in fi:
            clk_probabilty.append(line.rstrip())

    buy_probabilty = []
    with open('pred_buy.txt', 'r') as fi:
        for line in fi:
            buy_probabilty.append(line.rstrip())


    clk_usr_pre_dict = {}
    with open(output_file_nxt, 'r') as fi:
        i = 0
        for line in fi:
            elements = line.rstrip().split('\t')
            user_id = elements[13]
            if clk_usr_pre_dict.has_key(user_id):
                clk_usr_pre_dict[user_id].append(float(clk_probabilty[i]))
            else:
                clk_usr_pre_dict[user_id] = []
                clk_usr_pre_dict[user_id].append(float(clk_probabilty[i]))
            clk_probabilty[i] = "{0}${1}".format(clk_probabilty[i],user_id)
            i += 1

    buy_usr_pre_dict = {}
    with open(output_file_nxt, 'r') as fi:
        i = 0
        for line in fi:
            elements = line.rstrip().split('\t')
            user_id = elements[13]
            if buy_usr_pre_dict.has_key(user_id):
                buy_usr_pre_dict[user_id].append(float(buy_probabilty[i]))
            else:
                buy_usr_pre_dict[user_id] = []
                buy_usr_pre_dict[user_id].append(float(buy_probabilty[i]))
            buy_probabilty[i] = "{0}${1}".format(buy_probabilty[i], user_id)
            i += 1

    for key in clk_usr_pre_dict.keys():
        clk_usr_pre_dict[key] = sorted(clk_usr_pre_dict[key], reverse=True)
        buy_usr_pre_dict[key] = sorted(buy_usr_pre_dict[key], reverse=True)


    clk_pre = []
    raw_data = []
    for i in range(0, len(clk_probabilty)):
        probabilty = float(clk_probabilty[i].split('$')[0])
        user_id = clk_probabilty[i].split('$')[1]
        threshold = float(clk_usr_pre_dict[user_id][int(len(clk_usr_pre_dict[user_id])*USER_CLK_THRESHOLD)])
        if probabilty > threshold:
            clk_pre.append('1')
        else:
            clk_pre.append('0')
    # with open('pred_clk.txt', 'r') as fi:
    #     for line in fi:
    #         raw_data.append(float(line.rstrip()))
    #     threshold = sorted(raw_data, reverse=True)[int(len(raw_data) * 0.05 + 0.5)]
    #     for value in raw_data:
    #         if value < threshold:
    #             prob = '0'
    #         else:
    #             prob = '1'
    #         clk_pre.append(prob)

    buy_pre = []
    raw_data = []
    for i in range(0, len(buy_probabilty)):
        probabilty = float(buy_probabilty[i].split('$')[0])
        user_id = buy_probabilty[i].split('$')[1]
        threshold = float(buy_usr_pre_dict[user_id][int(len(buy_usr_pre_dict[user_id]) * USER_BUY_THRESHOLD)])
        if probabilty > threshold:
            buy_pre.append('1')
        else:
            buy_pre.append('0')
    # with open('pred_buy.txt', 'r') as fi:
    #     for line in fi:
    #         raw_data.append(float(line.rstrip()))
    #     threshold = sorted(raw_data, reverse=True)[int(len(raw_data) * 0.001 + 0.5)]
    #     for value in raw_data:
    #         if value < threshold:
    #             prob = '0'
    #         else:
    #             prob = '1'
    #         buy_pre.append(prob)


    with open(file_nxt_eco_info_path, 'r') as fi:
        i = 0
        j = 0
        for line in fi:
            log_id = line.rstrip().split('\t')[0]
            if j == 0:
                j += 1
                continue
            print >>sys.stdout, log_id + '\t' + clk_pre[i] + '\t' + buy_pre[i]
            i += 1

    print >>sys.stderr, len(clk_usr_pre_dict.keys())
