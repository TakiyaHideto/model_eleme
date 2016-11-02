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
                 output_file_clk,
                 output_file_buy,
                 output_file_nxt):
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
        self.output_file_clk = output_file_clk
        self.output_file_buy = output_file_buy
        self.output_file_nxt = output_file_nxt

    def joinData(self):
        self.DataLoadingClass.loadData()

        if os.path.exists(self.output_file_clk):
            os.remove(self.output_file_clk)
        if os.path.exists(self.output_file_buy):
            os.remove(self.output_file_buy)
        if os.path.exists(self.output_file_nxt):
            os.remove(self.output_file_nxt)

        with open(self.output_file_clk, 'w') as fo_click:
            with open(self.output_file_buy, 'w') as fo_buy:
                for key in self.DataLoadingClass.his_eco_info_data.keys():
                    log_id = key
                    data_his_eco_info_arr = self.DataLoadingClass.his_eco_info_data[log_id]
                    list_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('list_id')].split(":")[1]
                    # get his_eco_env data
                    data_his_eco_env_arr = self.DataLoadingClass.his_eco_env_data[list_id]
                    order_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('order_id')].split(":")[1]
                    # get order info data
                    if order_id == '"NULL"':
                        data_order_info_arr = []
                    else:
                        data_order_info_arr = self.DataLoadingClass.order_info_data[order_id]
                    rst_id = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('restaurant_id')].split(":")[1]
                    # get restaurant info data
                    data_rst_info_arr = self.DataLoadingClass.rst_info_data[rst_id]
                    # join data
                    is_click = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('is_click')].split(":")[1]
                    is_buy = data_his_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('is_buy')].split(":")[1]
                    if order_id != '"NULL"':
                        data_basic = 'info@' + '\tinfo@'.join(data_his_eco_info_arr) + '\t' + \
                                     'env@' + '\tenv@'.join(data_his_eco_env_arr) + '\t' + \
                                     'ord@' + '\tord@'.join(data_order_info_arr) + '\t' + \
                                     'rst@' + '\trst@'.join(data_rst_info_arr)
                    else:
                        data_basic = 'info@' + '\tinfo@'.join(data_his_eco_info_arr) + '\t' + \
                                     'env@' + '\tenv@'.join(data_his_eco_env_arr) + '\t' + \
                                     'rst@' + '\trst@'.join(data_rst_info_arr)
                    data_click = is_click + '\t' + data_basic
                    data_buy = is_buy + '\t' + data_basic
                    fo_click.write("{0}\n".format(data_click))
                    fo_buy.write("{0}\n".format(data_buy))

        with open(self.output_file_nxt, 'w') as fo:
            for key in self.DataLoadingClass.nxt_eco_info_data.keys():
                log_id = key
                data_nxt_eco_info_arr = self.DataLoadingClass.nxt_eco_info_data[log_id]
                list_id = '\"{0}\"'.format(data_nxt_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('list_id')].split(":")[1])
                data_nxt_eco_env_arr = self.DataLoadingClass.nxt_eco_env_data[list_id]
                rst_id = '\"{0}\"'.format(data_nxt_eco_info_arr[self.DataLoadingClass.data_eco_info_handler.getNameIndex('restaurant_id')].split(":")[1])
                data_rst_info_arr = self.DataLoadingClass.rst_info_data[rst_id]

                data_str = '0' + '\t' + \
                           'info@' + '\tinfo@'.join(data_nxt_eco_info_arr) + '\t' + \
                           'env@' + '\tenv@'.join(data_nxt_eco_env_arr) + '\t' + \
                           'rst@' + '\trst@'.join(data_rst_info_arr)
                fo.write("{0}\n".format(data_str))