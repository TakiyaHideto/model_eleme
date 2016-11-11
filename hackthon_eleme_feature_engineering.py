#coding=utf-8

# please write your function of feat engineering below
# notice that data_block and output_file are required to writtern as the necessary paras in all the functions
import os
import math
from hackthon_eleme_feature_processing_all import *  

def feature_engineering(input_file, output_file, feat_map_file):
    file_feat_eng=input_file+'_feateng'
    file_onehot=file_feat_eng+'_onehot'
    featureProcessing(input_file,file_feat_eng)
    oneHot(file_feat_eng,file_onehot,feat_map_file)
    feature2num(file_onehot,output_file,feat_map_file)



  


################### feat eng: one hot ###################



def feature_eng(input_file, output_file, feat_map_file, feat_map, feat_map_index_max):
    readFeatMapFile(feat_map_file, feat_map)

    with open(output_file, 'w') as fo:
        with open(input_file, 'r') as fi:
            for line in fi:
                label, feat_dict = str2dict(line)

                distance = calDistance(
                    feat_dict['env@x'],
                    feat_dict['env@y'],
                    feat_dict['rst@x'],
                    feat_dict['rst@y']
                )
                sort_index = feat_dict['info@sort_index']
                is_select = feat_dict['env@is_select']
                day_no = int(feat_dict['env@day_no'])%7
                minutes = feat_dict['env@minutes']
                is_new = feat_dict['env@is_new']
                if feat_dict['env@resolution'] == '"OTHER"':
                    feat_dict['env@resolution'] = '0x0'
                resolution_length = feat_dict['env@resolution'].replace('\"','').split('x')[0]
                resolution_wide = feat_dict['env@resolution'].replace('\"', '').split('x')[1]
                # channel = feat_dict['env@channel'].replace('\"','')
                agent_fee = feat_dict['rst@agent_fee']
                is_premium = feat_dict['rst@is_premium']
                good_rating_rate = feat_dict['rst@good_rating_rate']
                has_image = feat_dict['rst@has_image']
                has_food_img = feat_dict['rst@has_food_img']
                min_deliver_amount = feat_dict['rst@min_deliver_amount']
                time_ensure_spent = feat_dict['rst@time_ensure_spent']
                is_time_ensure = feat_dict['rst@is_time_ensure']
                is_ka = feat_dict['rst@is_ka']
                radius = feat_dict['rst@radius']
                service_rating = feat_dict['rst@service_rating']
                invoice = feat_dict['rst@invoice']
                online_payment = feat_dict['rst@online_payment']
                public_degree = feat_dict['rst@public_degree']
                food_num = feat_dict['rst@food_num']
                food_image_num = feat_dict['rst@food_image_num']
                is_promotion_info = feat_dict['rst@is_promotion_info']


                user_id_key_list = keyList(key_prefix='env@user_id',
                                           key_content=feat_dict['env@user_id'])
                feat_map, feat_map_index_max, user_id_list = addOnehotFeatIndex(user_id_key_list,
                                                                                feat_map,
                                                                                feat_map_index_max)

                primary_category_key_list = keyList(key_prefix='rst@primary_category',
                                                    key_content=feat_dict['rst@primary_category'].decode('utf8'))
                # print primary_category_key_list.encode('utf-8')
                feat_map, feat_map_index_max, primary_category_list = addOnehotFeatIndex(primary_category_key_list,
                                                                                         feat_map,
                                                                                         feat_map_index_max)

                category_list_key_list = keyList(key_prefix='rst@category_list',
                                                 key_content=feat_dict['rst@category_list'].decode('utf8'))
                feat_map, feat_map_index_max, category_list = addOnehotFeatIndex(category_list_key_list,
                                                                                          feat_map,
                                                                                          feat_map_index_max)

                food_name_list_key_list = keyList(key_prefix='rst@food_name_list',
                                                  key_content=feat_dict['rst@food_name_list'].decode('utf8'))
                feat_map, feat_map_index_max, food_name_list = addOnehotFeatIndex(food_name_list_key_list,
                                                                                           feat_map,
                                                                                           feat_map_index_max)
                new_record = "{0}\t".format(label) + \
                            "{0}:{1}\t".format(feat_map['distance'], distance) + \
                            "{0}:{1}\t".format(feat_map['sort_index'], sort_index) + \
                            "{0}:{1}\t".format(feat_map['is_select'], is_select) + \
                            "{0}:{1}\t".format(feat_map['day_no'], day_no) + \
                            "{0}:{1}\t".format(feat_map['minutes'], minutes) + \
                            "{0}:{1}\t".format(feat_map['is_new'], is_new) + \
                            "{0}:{1}\t".format(feat_map['resolution_length'], resolution_length) + \
                            "{0}:{1}\t".format(feat_map['resolution_wide'], resolution_wide) + \
                            "{0}:{1}\t".format(feat_map['agent_fee'], agent_fee) + \
                            "{0}:{1}\t".format(feat_map['is_premium'], is_premium) + \
                            "{0}:{1}\t".format(feat_map['good_rating_rate'], good_rating_rate) + \
                            "{0}:{1}\t".format(feat_map['has_image'], has_image) + \
                            "{0}:{1}\t".format(feat_map['has_food_img'], has_food_img) + \
                            "{0}:{1}\t".format(feat_map['min_deliver_amount'], min_deliver_amount) + \
                            "{0}:{1}\t".format(feat_map['time_ensure_spent'], time_ensure_spent) + \
                            "{0}:{1}\t".format(feat_map['is_time_ensure'], is_time_ensure) + \
                            "{0}:{1}\t".format(feat_map['is_ka'], is_ka) + \
                            "{0}:{1}\t".format(feat_map['radius'], radius) + \
                            "{0}:{1}\t".format(feat_map['service_rating'], service_rating) + \
                            "{0}:{1}\t".format(feat_map['invoice'], invoice) + \
                            "{0}:{1}\t".format(feat_map['online_payment'], online_payment) + \
                            "{0}:{1}\t".format(feat_map['public_degree'], public_degree) + \
                            "{0}:{1}\t".format(feat_map['food_num'], food_num) + \
                            "{0}:{1}\t".format(feat_map['food_image_num'], food_image_num) + \
                            "{0}:{1}\t".format(feat_map['is_promotion_info'], is_promotion_info) + \
                            "{0}\t".format('\t'.join(user_id_list)) + \
                            "{0}\t".format('\t'.join(primary_category_list)) + \
                            "{0}\t".format('\t'.join(category_list)) + \
                            "{0}\n".format('\t'.join(food_name_list))

                fo.write(new_record)
        output_file(feat_map, feat_map_file)


def outputFeatMap(feat_map, feat_map_file):
    with open(feat_map_file, 'w') as fo:
        for key in feat_map.keys():
            fo.write("{0}:{1}\n".format(key, feat_map[key]))


def readFeatMapFile(feat_map_file, feat_map):
    if os.path.exists(feat_map_file):
        with open(feat_map_file, 'r') as fi:
            for line in fi:
                elements = line.rstrip().split(':')
                if not feat_map.has_key(elements[0]):
                    feat_map[elements[0]] = elements[1]

def str2dict(data_records):
    feat_dict = {}
    elements = data_records.rstrip().split('\t')
    label = elements[0]
    for i in range(1, len(elements)):
        feat_name = elements[i].split(':')[0]
        feat_value = elements[i].split(':')[1]
        feat_dict[feat_name] = feat_value
    return label, feat_dict

def calDistance(x1, y1, x2, y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def keyList(key_prefix, key_content):
    key_content = key_content.replace('\"','').split(',')
    key_list = [key_prefix+key for key in key_content]
    return key_list

def addOnehotFeatIndex(feat_key_list, feat_map, feat_map_index_max):
    onehot_feat_list = []
    for key in feat_key_list:
        if not feat_map.has_key(key):
            feat_map[key] = feat_map_index_max
            feat_map_index_max += 1
        onehot_feat_list.append("{0}:1".format(feat_map[key]))
    return feat_map, feat_map_index_max, onehot_feat_list