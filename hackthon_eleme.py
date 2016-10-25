
import os
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


# def trainTest():
#     dtrain = xgb.DMatrix('/Users/hideto/Desktop/e_data.txt.train')
#     dtest = xgb.DMatrix('/Users/hideto/Desktop/e_data.txt.test')
#     # specify parameters via map
#     param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
#     num_round = 2
#     bst = xgb.train(param, dtrain, num_round)
#     # make prediction
#     preds = bst.predict(dtest)

def predict():
    pass

if __name__ == '__main__':
    file_his_eco_env_path = '/Users/hideto/Downloads/E_data/his_eco_env.txt'
    file_his_eco_info_path = '/Users/hideto/Downloads/E_data/his_eco_info.txt'
    file_order_info_path = '/Users/hideto/Downloads/E_data/his_order_info.txt'
    file_rst_info_path = '/Users/hideto/Downloads/E_data/rst_info.txt'
    file_nxt_eco_env_path = '/Users/hideto/Downloads/E_data/next_eco_env.txt'
    file_nxt_eco_info_path = '/Users/hideto/Downloads/E_data/next_eco_info.txt'
    output_file = '/Users/hideto/Desktop/output.txt'
    output_file_feat_eng = '/Users/hideto/Desktop/output_feat_eng.txt'
    output_file_nxt = '/Users/hideto/Desktop/output_nxt.txt'
    output_file_nxt_feat_eng = '/Users/hideto/Desktop/output_nxt_feat_eng.txt'
    feat_map_file = '/Users/hideto/Desktop/feat_map_file.txt'
    train_file_path = '/Users/hideto/Desktop/e_data.txt.train'
    test_file_path = '/Users/hideto/Desktop/e_data.txt.test'
    job = DataJoining(file_his_eco_env_path,
                      file_his_eco_info_path,
                      file_order_info_path,
                      file_rst_info_path,
                      file_nxt_eco_env_path,
                      file_nxt_eco_info_path,
                      output_file,
                      output_file_nxt)

    # job.joinData()
    # oneHot(output_file, output_file_feat_eng, feat_map_file)
    # splitData(output_file_feat_eng, train_file_path, test_file_path)
    # trainTest()
    oneHot(output_file_nxt, output_file_nxt_feat_eng, feat_map_file)