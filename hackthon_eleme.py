
import os
import xgboost as xgb

############################# define data structure #############################
# eco_env data handler
class DataEcoEnvHandler:
    def __init__(self):
        self.data_handler = {
            'list_id': 0,
            'is_select': 1,
            'day_no': 2,
            'minutes': 3,
            'eleme_device_id': 4,
            'is_new': 5,
            'x': 6,
            'y': 7,
            'user_id': 8,
            'network_type': 9,
            'platform': 10,
            'brand': 11,
            'model': 12,
            'network_operator': 13,
            'resolution': 14,
            'channel': 15
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# eco_info data handler
class DataEcoInfoHandler:
    def __init__(self):
        self.data_handler = {
            'log_id': 0,
            'list_id': 1,
            'restaurant_id': 2,
            'sort_index': 3,
            'is_click': 4,
            'is_buy': 5,
            'is_raw_buy': 6,
            'order_id': 7
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# order info data handler
class DataOrderInfoHandler:
    def __init__(self):
        self.data_handler = {
            'day_no': 0,
            'minutes': 1,
            'order_id': 2,
            'restaurant_id': 3,
            'deliver_fee': 4,
            'is_online_paid': 5,
            'order_process_minutes': 6,
            'restaurant_num': 7,
            'address_type': 8,
            'is_valid': 9,
            'is_book': 10,
            'is_coupon': 11,
            'is_invoice': 12,
            'pindan_flag': 13,
            'x': 14,
            'y': 15,
            'bu_flag_name': 16,
            'eleme_order_total': 17,
            'total': 18,
            'cut_money': 19,
            'is_activity': 20,
            'has_new_user_subsidy': 21,
            'hongbao_amount':22,
            'receiver_deliver_fee': 23,
            'user_id': 24,
            'food_name': 25,
            'food_category': 26
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# rst info data handler
class DataRstInfoHandler:
    def __init__(self):
        self.data_handler = {
            'restaurant_id': 0,
            'primary_category': 1,
            'food_name_list': 2,
            'category_list': 3,
            'x': 4,
            'y': 5,
            'agent_fee': 6,
            'is_premium': 7,
            'address_type': 8,
            'good_rating_rate': 9,
            'has_image': 10,
            'has_food_img': 11,
            'min_deliver_amount': 12,
            'time_ensure_spent': 13,
            'is_time_ensure':14,
            'is_ka': 15,
            'is_time_ensure_discount': 16,
            'is_eleme_deliver': 17,
            'bu_flag': 18,
            'brand_name': 19,
            'service_rating': 20,
            'invoice': 21,
            'online_payment': 22,
            'public_degree': 23,
            'food_num': 24,
            'food_image_num': 25,
            'is_promotion_info': 26,
            'is_bookable': 27
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)
############################# define data structure #############################


# load all data files
class DataLoading:
    def __init__(self,
                 file_his_eco_env_path,
                 file_his_eco_info_path,
                 file_order_info_path,
                 file_rst_info_path,
                 file_nxt_eco_env_path,
                 file_nxt_eco_info_path):
        self.file_his_eco_env_path = file_his_eco_env_path
        self.file_his_eco_info_path = file_his_eco_info_path
        self.file_order_info_path = file_order_info_path
        self.file_rst_info_path = file_rst_info_path
        self.file_nxt_eco_env_path = file_nxt_eco_env_path
        self.file_nxt_eco_info_path = file_nxt_eco_info_path
        self.his_eco_env_data = {}
        self.his_eco_info_data = {}
        self.order_info_data = {}
        self.rst_info_data = {}
        self.nxt_eco_env_data = {}
        self.nxt_eco_info_data = {}
        self.data_eco_env_handler = DataEcoEnvHandler()
        self.data_eco_info_handler = DataEcoInfoHandler()
        self.data_order_info_handler = DataOrderInfoHandler()
        self.data_rst_info_handler = DataRstInfoHandler()

    def loadDataHisEcoInfo(self):
        with open(self.file_his_eco_info_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_eco_info_handler.getNameIndex('log_id')]
                self.his_eco_env_data[primary_key_log_id] = data_splited
        print 'finish loading his_eco_env.txt'

    def loadDataHisEcoEnv(self):
        with open(self.file_his_eco_env_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_eco_env_handler.getNameIndex('list_id')]
                self.his_eco_info_data[primary_key_log_id] = data_splited
        print 'finish loading his_eco_info.txt'

    def loadDataOrdInfo(self):
        with open(self.file_order_info_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_order_info_handler.getNameIndex('order_id')]
                self.order_info_data[primary_key_log_id] = data_splited
        print 'finish loading his_order_info.txt'

    def loadDataRstInfo(self):
        with open(self.file_rst_info_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_rst_info_handler.getNameIndex('restaurant_id')]
                self.rst_info_data[primary_key_log_id] = data_splited
        print 'finish loading rst_info.txt'

    def loadDataNxtEcoEnv(self):
        with open(self.file_nxt_eco_env_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_eco_env_handler.getNameIndex('list_id')]
                self.nxt_eco_env_data[primary_key_log_id] = data_splited
        print 'finish loading next_eco_info.txt'

    def loadDataNxtEcoInfo(self):
        with open(self.file_nxt_eco_info_path, 'r') as fi:
            for line in fi:
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[self.data_eco_info_handler.getNameIndex('log_id')]
                self.nxt_eco_info_data[primary_key_log_id] = data_splited
        print 'finish loading next_eco_info.txt'

    def loadData(self):
        self.loadDataHisEcoEnv()
        self.loadDataHisEcoInfo()
        self.loadDataOrdInfo()
        self.loadDataRstInfo()
        self.loadDataNxtEcoEnv()
        self.loadDataNxtEcoInfo()


class DataJoining:
    def __init__(self,
                 file_his_eco_env_path,
                 file_his_eco_info_path,
                 file_order_info_path,
                 file_rst_info_path,
                 file_nxt_eco_env_path,
                 file_nxt_eco_info_path,
                 output_file):
        self.file_his_eco_env_path = file_his_eco_env_path
        self.file_his_eco_info_path = file_his_eco_info_path
        self.file_order_info_path = file_order_info_path
        self.file_rst_info_path = file_rst_info_path
        self.file_nxt_eco_env_path = file_nxt_eco_env_path
        self.file_nxt_eco_info_path = file_nxt_eco_info_path
        self.DataLoadingClass = DataLoading(file_his_eco_env_path,
                                            file_his_eco_info_path,
                                            file_order_info_path,
                                            file_rst_info_path,
                                            file_nxt_eco_env_path,
                                            file_nxt_eco_info_path)
        self.output_file = output_file

    def joinData(self):
        self.DataLoadingClass.loadData()
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        with open(self.output_file, 'w') as fo:
            for key in self.DataLoadingClass.his_eco_info_data.keys():
                log_id = key
                # print log_id
                data_his_eco_info_arr = self.DataLoadingClass.his_eco_info_data[log_id]
                # print data_his_eco_info_arr
                list_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('list_id')]
                # print list_id
                # get his_eco_env data
                data_his_eco_env_arr = self.DataLoadingClass.his_eco_env_data[list_id]
                # print data_his_eco_env_arr
                order_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('order_id')]
                # print order_id
                # get order info data
                if order_id == '"NULL"':
                    data_order_info_arr = []
                else:
                    data_order_info_arr = self.DataLoadingClass.order_info_data[order_id]
                rst_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('restaurant_id')]
                # get restaurant info data
                data_rst_info_arr = self.DataLoadingClass.rst_info_data[rst_id]
                # join data
                is_click = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('is_click')]
                is_buy = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('is_buy')]
                data_str = ','.join(data_his_eco_info_arr) + ',' + \
                           ','.join(data_his_eco_env_arr) + ',' + \
                           ','.join(data_order_info_arr) + ',' + \
                           ','.join(data_rst_info_arr) + ',' + \
                           is_click + ',' + is_buy
                data_str = is_click + '\t' +\
                           '\t'.join(data_his_eco_info_arr) + '\t' + \
                           '\t'.join(data_his_eco_env_arr) + '\t' + \
                           '\t'.join(data_order_info_arr) + '\t' + \
                           '\t'.join(data_rst_info_arr)
                fo.write("{0}\n".format(data_str))


def splitData(data_file_path, train_file_path, test_file_path):
    os.popen('cat {0} |'.format(data_file_path) +
             "awk '{if(NR%5==1) print $0}'" +
             '> {0}'.format(test_file_path)
             )
    os.popen('cat {0} |'.format(data_file_path) +
             "awk '{if(NR%5!=1) print $0}'" +
             '> {0}'.format(train_file_path)
             )


def trainTest():
    dtrain = xgb.DMatrix('/Users/hideto/Desktop/e_data.txt.train')
    dtest = xgb.DMatrix('/Users/hideto/Desktop/e_data.txt.test')
    # specify parameters via map
    param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
    num_round = 2
    bst = xgb.train(param, dtrain, num_round)
    # make prediction
    preds = bst.predict(dtest)


if __name__ == '__main__':
    file_his_eco_env_path = '/Users/hideto/Project/ele.me/E_data/his_eco_env.txt'
    file_his_eco_info_path = '/Users/hideto/Project/ele.me/E_data/his_eco_info.txt'
    file_order_info_path = '/Users/hideto/Project/ele.me/E_data/his_order_info.txt'
    file_rst_info_path = '/Users/hideto/Project/ele.me/E_data/rst_info.txt'
    file_nxt_eco_env_path = '/Users/hideto/Project/ele.me/E_data/next_eco_env.txt'
    file_nxt_eco_info_path = '/Users/hideto/Project/ele.me/E_data/next_eco_info.txt'
    output_file = '/Users/hideto/Desktop/output.txt'
    train_file_path = '/Users/hideto/Desktop/e_data.txt.train'
    test_file_path = '/Users/hideto/Desktop/e_data.txt.test'
    job = DataJoining(file_his_eco_info_path,
                      file_his_eco_env_path,
                      file_order_info_path,
                      file_rst_info_path,
                      file_nxt_eco_env_path,
                      file_nxt_eco_info_path,
                      output_file)

    # job.joinData()
    # splitData(output_file, train_file_path, test_file_path)
    trainTest()