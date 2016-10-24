from hackthon_eleme_data_structure import *

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
                data_with_featname_arr = []
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
