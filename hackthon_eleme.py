
import os
import commands
from hackthon_eleme_data_structure import *
from hackthon_eleme_data_loading import *
from hackthon_eleme_data_joining import *
from hackthon_eleme_feature_engineering import *
# import xgboost as xgb



def splitData(data_file_path, train_file_path, test_file_path):
    os.popen('cat {0} |'.format(data_file_path) +
             "awk '{if(NR%5==1) print $0}'" +
             '> {0}'.format(test_file_path)
             )
    os.popen('cat {0} |'.format(data_file_path) +
             "awk '{if(NR%5!=1) print $0}'" +
             '> {0}'.format(train_file_path)
             )


def trainTest(configuration):
    # dtrain = xgb.DMatrix('/Users/hideto/Desktop/output.txt')
    # dtest = xgb.DMatrix('/Users/hideto/Desktop/e_data.txt.test')
    # # specify parameters via map
    # param = {'bst:max_depth': 2, 'bst:eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
    # param['nthread'] = 4
    # param['eval_metric'] = 'auc'
    # num_round = 2
    # evallist = [(dtrain, 'eval'), (dtrain, 'train')]
    # bst = xgb.train(param, dtrain, num_round, evallist)
    # make prediction
    # preds = bst.predict(dtest)
    output = os.popen('/Users/hideto/Project/xgboost/xgboost /Users/hideto/Project/model_eleme/{0}.conf'.format(configuration))
    print output.read()


def predict(configuration, model_in):
    output = os.popen('/Users/hideto/Project/xgboost/xgboost /Users/hideto/Project/model_eleme/{0}.conf task=pred model_in="{1}"'.format(configuration, model_in))
    print output.read()

if __name__ == '__main__':

    file_path_prefix = '/Users/hideto/Downloads/E_data/'
    output_prefix = '/Users/hideto/Desktop/'

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

    # job.joinData()

    # # traing clk
    # oneHot(output_file_clk, output_file_clk_feat_eng, feat_map_file)
    # splitData(output_file_clk_feat_eng,
    #           train_file_path=train_file_path+'clk',
    #           test_file_path=test_file_path+'clk')
    # trainTest(configuration='configuration_clk')

    # traing buy
    oneHot(output_file_buy, output_file_buy_feat_eng, feat_map_file)
    splitData(output_file_clk_feat_eng,
              train_file_path=train_file_path + 'buy',
              test_file_path=test_file_path + 'buy')
    trainTest(configuration='configuration_buy')


    # # predict nxt
    # oneHot(output_file_nxt, output_file_nxt_feat_eng, feat_map_file)
    # predict(configuration='configuration_clk',
    #         model_in='clk_mdl.model')
    # predict(configuration='configuration_buy',
    #         model_in='buy_mdl.model')

    # clk_pre = []
    # with open('pred_clk.txt', 'r') as fi:
    #     for line in fi:
    #         if float(line.rstrip())<0.5:
    #             prob = '0'
    #         else:
    #             prob = '1'
    #         clk_pre.append(prob)
    # buy_pre = []
    # with open('pred_buy.txt', 'r') as fi:
    #     for line in fi:
    #         if float(line.rstrip()) < 0.5:
    #             prob = '0'
    #         else:
    #             prob = '1'
    #         buy_pre.append(prob)
    #
    # with open(file_nxt_eco_info_path, 'r') as fi:
    #     i = 0
    #     for line in fi:
    #         log_id = line.rstrip().split('\t')[0]
    #         print log_id + '\t' + clk_pre[i] + '\t' + buy_pre[i]
