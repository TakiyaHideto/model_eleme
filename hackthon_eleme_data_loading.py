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

    def __del__(self):
        print 'delete DataLoading class'

    def getDataOject(self, data_class_name):
        if data_class_name == 'data_eco_env_handler':
            return self.data_eco_env_handler
        elif data_class_name == 'data_eco_info_handler':
            return self.data_eco_info_handler
        elif data_class_name == 'data_order_info_handler':
            return self.data_order_info_handler
        elif data_class_name == 'data_rst_info_handler':
            return self.data_rst_info_handler
        else:
            print "wrong data object handler name"
            exit(1)

    def getDataFilePath(self, data_file_name):
        if data_file_name == 'file_his_eco_env_path':
            return self.file_his_eco_env_path
        elif data_file_name == 'file_his_eco_info_path':
            return self.file_his_eco_info_path
        elif data_file_name == 'file_order_info_path':
            return self.file_order_info_path
        elif data_file_name == 'file_rst_info_path':
            return self.file_rst_info_path
        elif data_file_name == 'file_nxt_eco_env_path':
            return self.file_nxt_eco_env_path
        elif data_file_name == 'file_nxt_eco_info_path':
            return self.file_nxt_eco_info_path
        else:
            print "wrong data file name"
            exit(1)

    def getDataStruct(self, data_file_name):
        if data_file_name == 'file_his_eco_env_path':
            return self.his_eco_env_data
        elif data_file_name == 'file_his_eco_info_path':
            return self.his_eco_info_data
        elif data_file_name == 'file_order_info_path':
            return self.order_info_data
        elif data_file_name == 'file_rst_info_path':
            return self.rst_info_data
        elif data_file_name == 'file_nxt_eco_env_path':
            return self.nxt_eco_env_data
        elif data_file_name == 'file_nxt_eco_info_path':
            return self.nxt_eco_info_data
        else:
            print "wrong data file name"
            exit(1)

    def getDataPrimartKey(self, data_class_name):
        if data_class_name == 'data_eco_env_handler':
            return 'list_id'
        elif data_class_name == 'data_eco_info_handler':
            return 'log_id'
        elif data_class_name == 'data_order_info_handler':
            return 'order_id'
        elif data_class_name == 'data_rst_info_handler':
            return 'restaurant_id'
        else:
            print "wrong data object handler name"
            exit(1)

    def loadDataInfo(self, data_class_name, data_file_name):
        i= 0
        data_file_path = self.getDataFilePath(data_file_name)
        data_object = self.getDataOject(data_class_name)
        data_primary_key = self.getDataPrimartKey(data_class_name)
        data_struct = self.getDataStruct(data_file_name)
        with open(data_file_path, 'r') as fi:
            for line in fi:
                if i == 0:
                    i += 1
                    continue
                data_with_featname_arr = []
                data_splited = line.rstrip().split('\t')
                primary_key_log_id = data_splited[data_object.getNameIndex(data_primary_key)]
                for i in range(0,len(data_splited)):
                    data_with_featname_arr\
                        .append("{0}:{1}".format(data_object.getIndexName('{0}'.format(str(i))),
                                                 data_splited[i]))
                data_struct[primary_key_log_id] = data_with_featname_arr
                i += 1
        print 'finish loading {0}'.format(data_file_name)

    def loadData(self):
        self.loadDataInfo(data_class_name='data_eco_env_handler',
                          data_file_name='file_his_eco_env_path')

        self.loadDataInfo(data_class_name='data_eco_info_handler',
                          data_file_name='file_his_eco_info_path')

        self.loadDataInfo(data_class_name='data_order_info_handler',
                          data_file_name='file_order_info_path')

        self.loadDataInfo(data_class_name='data_rst_info_handler',
                          data_file_name='file_rst_info_path')

        self.loadDataInfo(data_class_name='data_eco_env_handler',
                          data_file_name='file_nxt_eco_env_path')

        self.loadDataInfo(data_class_name='data_eco_info_handler',
                          data_file_name='file_nxt_eco_info_path')
