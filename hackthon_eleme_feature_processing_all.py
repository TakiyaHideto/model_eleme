from hackthon_eleme_feature_processing import *
import os

onehot_feat_cand = [
    'day_no',
    'minutes',
    'network_type',
    'platform',
    'network_operator',
    'primary_category',
    'address_type',
    'time_ensure_spent',
    'bu_flag',
    'public_degree',
    'food_num',
    'food_image_num'
    
    
]


def str2dic(input_str):
    result_dic={}
    input_value=input_str
    value_list=input_value.split('\t')
    for i in range(0,len(value_list)):
        elements=value_list[i].rstrip().split(':')
        result_dic[elements[0]]=elements[1]
    return result_dic

def dic2str(input_dic):
    result_list=[]
    for key, value in input_dic.items():
        elemet="{0}:{1}".format(key,value)
        result_list.append(elemet)
    result_str='\t'.join(result_list)
    return result_str
        
def feature2num(input_file,output_file,feat_map_file):
    feat_map = {}
    if os.path.exists(feat_map_file):
        with open(feat_map_file, 'r') as fi:
            for line in fi:
                elements = line.rstrip().split(":")
                feat_map[elements[0]] = elements[1]
      
    with open(output_file, 'w') as fo:
        with open(input_file, 'r') as fi:
            for data in fi:
                records = []
                elements = data.rstrip().split('\t')
                label = elements[0]
                for i in range(1, len(elements)):
                    elements0=elements[i].split(':')[0]
                    elements1=elements[i].split(':')[1]
                    if feat_map.has_key(elements0):
                        records.append('{0}:{1}'.format(feat_map[elements0],elements1))
                fo.write("{0}\t{1}\n".format(label, '\t'.join(records)))



def oneHot(input_file, output_file, feat_map_file):
    feat_map = {}
    feat_index = 0
    if os.path.exists(feat_map_file):
        with open(feat_map_file, 'r') as fi:
            for line in fi:
                elements = line.rstrip().split(":")
                feat_map[elements[0]] = elements[1]
                feat_index = max(int(elements[1]), feat_index)

    with open(output_file, 'w') as fo:
        with open(input_file, 'r') as fi:
            for data in fi:
                records = []
                elements = data.rstrip().split('\t')
                label = elements[0]
                for i in range(1, len(elements)):
                    if elements[i].split(":")[0] not in onehot_feat_cand:
                        continue
                    try:
                        feat_name = "{0}_{1}".format(elements[i].split(":")[0],
                                                     elements[i].split(":")[1])
                        if not feat_map.has_key(feat_name):
                            feat_index += 1
                            feat_map[feat_name] = str(feat_index)
 
                        records.append("{0}:1".format(feat_name))
                    except IndexError:
                        print i
                        print elements[i]
                        continue
                old_line=data.strip()
                fo.write("{0}\t{1}\n".format(old_line, '\t'.join(records)))
                #fo.write("{0}\t{1}\n".format(label, '\t'.join(records)))
    for i in range(0,len(onehot_feat_cand)):
        if feat_map.has_key(onehot_feat_cand[i]):
            feat_map.pop(onehot_feat_cand[i])
    outputFeatMap(feat_map, feat_map_file)


def outputFeatMap(feat_map, feat_map_file):
    with open(feat_map_file, 'w') as fo: 
        for key in feat_map.keys():
            fo.write('{0}:{1}\n'.format(key,
                                        feat_map[key]))


def featureProcessing(input_file,output_file):
    with open(output_file,'w') as fo:
        with open(input_file, 'r') as fi:
            for line in fi:
            
                element=line.rstrip().split('\t')
                label=element[0]
                feature_line='\t'.join(element[1:])
                content_dic=str2dic(feature_line)
                featuremap=Featureprocessing(content_dic)
                content_dic.pop('log_id')
                content_dic.pop('list_id')
                content_dic.pop('restaurant_id')
                content_dic['sort_index']=featuremap.normalization('sort_index',200,1)
                content_dic['day_no']=featuremap.transformweek('day_no')
                content_dic['minutes']=featuremap.split3('minutes',600,840)
                content_dic.pop('eleme_device_id')
                content_dic['x']=featuremap.normalization('x',0,10)
                content_dic['y']=featuremap.normalization('y',0,10)
                content_dic.pop('user_id')
                content_dic['network_type']=featuremap.name2num('network_type',['"2G"','"3G"','"4G"','"WIFI"','"UNKNOWN"'])        
                content_dic['platform']=featuremap.name2num('platform',['"iOS"','"Android"'])
                content_dic.pop('brand')
                content_dic.pop('model')
                content_dic['resolution']=featuremap.resolution('resolution')
                content_dic['resolution']=featuremap.normalization('resolution',500000,3000000)
                content_dic.pop('channel')
                content_dic.pop('food_name_list')
                content_dic.pop('category_list')
                content_dic['agent_fee']=featuremap.normalization('agent_fee',0,10)
                content_dic.pop('is_premium')
                content_dic.pop('open_month_num')
                content_dic['min_deliver_amount']=featuremap.normalization('min_deliver_amount',0,50)                
                content_dic.pop('is_time_ensure')
                content_dic.pop('is_ka')
                content_dic['radius']=featuremap.normalization('radius',0,3)
                content_dic.pop('brand_name')
                content_dic['service_rating']=featuremap.normalization('service_rating',4,5)                
                content_dic.pop('online_payment')
                content_dic['food_num']=featuremap.split3('food_num',100,200)
                content_dic['food_image_num']=featuremap.split3('food_image_num',60,150)
            
                # a little strange of this line
            
                new_feature_line=dic2str(content_dic)
                new_line="{0}\t{1}\n".format(label, new_feature_line)
                fo.write(new_line)


#input_file='/Users/wangjun/documents/dict_test.txt'
#output_file='/Users/wangjun/documents/dict_test_out.txt'
#feat_map_file='/Users/wangjun/documents/feat_map.txt'
#oneHot(input_file,output_file,feat_map_file)
