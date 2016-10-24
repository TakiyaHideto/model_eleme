import os
from hackthon_eleme_data_loading import *

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
