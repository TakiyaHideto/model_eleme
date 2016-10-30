from hackthon_eleme_feature_processing import *
import os

feat_cand = [
    'info@restaurant_id',
    'info@sort_index',
    'info@is_raw_buy',	
    'env@is_select',
    'env@day_no',	
    'env@minutes',	
    'env@is_new',
    'env@eleme_device_id',
    'env@x',
    'env@y',
    'env@user_id',
    'env@network_type',	
    'env@platform',		
    'env@network_operator',	
    'env@resolution',	
    'rst@primary_category',	
    'rst@food_name_list',	
    'rst@category_list',	
    'rst@x',	
    'rst@y',	
    'rst@agent_fee',	
    'rst@address_type',	
    'rst@good_rating_rate',		
    'rst@has_image',
    'rst@has_food_img',	
    'rst@min_deliver_amount',	
    'rst@time_ensure_spent',	
    'rst@is_time_ensure_discount',	
    'rst@is_eleme_deliver',
    'rst@radius',
    'rst@bu_flag',	
    'rst@service_rating',	
    'rst@invoice',	
    'rst@public_degree',	
    'rst@food_num',	
    'rst@food_image_num',
    'rst@is_promotion_info',	
    'rst@is_bookable',

]
    


onehot_feat_cand = [
    'info@restaurant_id',
    'env@day_no',
    'env@minutes',
    'env@eleme_device_id',
    'env@network_type',
    'env@platform',
    'env@network_operator',
    'env@user_id',
    'rst@primary_category',
    'rst@address_type',
    'rst@time_ensure_spent',
    'rst@bu_flag',
    'rst@public_degree',
    'rst@food_num',
    'rst@food_image_num'
    
    
]


def str2dic(input_str):
    result_dic={}
    input_value=input_str
    value_list=input_value.split('\t')
    for i in range(0,len(value_list)):
        elements=value_list[i].rstrip().split(':')
        if elements[0] not in feat_cand:
            continue
        else:
#            print 'ok',elements[0]
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
                        if not feat_map.has_key(elements[i].split(":")[0]):
                            feat_index += 1
                            feat_map[elements[i].split(":")[0]] = str(feat_index)
                            
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
                content_dic.pop('info@log_id')
                content_dic.pop('info@list_id')
                content_dic.pop('info@restaurant_id')
                content_dic['info@sort_index']=featuremap.normalization('info@sort_index',200,1)
                content_dic.pop('info@is_click')
                content_dic.pop('info@is_buy')
                content_dic.pop('info@order_id')
                content_dic.pop('env@list_id')
                content_dic['env@day_no']=featuremap.transformweek('env@day_no')
                content_dic['env@minutes']=featuremap.split3('env@minutes',600,840)
                content_dic.pop('env@eleme_device_id')
                content_dic['distance']=featuremap.getdistance('env@x','env@y','rst@x','rst@y')
                content_dic.pop('env@x')
                content_dic.pop('env@y')
                content_dic.pop('env@user_id')
                content_dic['env@network_type']=featuremap.name2num('env@network_type',['"2G"','"3G"','"4G"','"WIFI"','"UNKNOWN"'])        
                content_dic['env@platform']=featuremap.name2num('env@platform',['"iOS"','"Android"'])
                content_dic.pop('env@brand')
                content_dic.pop('env@model')
                content_dic['env@resolution']=featuremap.resolution('env@resolution')
                content_dic['evn@resolution']=featuremap.normalization('env@resolution',500000,3000000)
                content_dic.pop('env@channel')
                content_dic.pop('rst@restaurant_id')
                content_dic.pop('rst@x')
                content_dic.pop('rst@y')
                content_dic.pop('food_name_list')
                content_dic.pop('category_list')
                content_dic['rst@agent_fee']=featuremap.normalization('rst@agent_fee',0,10)
                content_dic.pop('rst@is_premium')
                content_dic.pop('rst@open_month_num')
                content_dic['rst@min_deliver_amount']=featuremap.normalization('rst@min_deliver_amount',0,50)                
                content_dic.pop('rst@is_time_ensure')
                content_dic.pop('rst@is_ka')
                content_dic['rst@radius']=featuremap.normalization('rst@radius',0,3)
                content_dic.pop('rst@brand_name')
                content_dic['rst@service_rating']=featuremap.normalization('rst@service_rating',4,5)                

                content_dic.pop('rst@online_payment')
                content_dic['rst@food_num']=featuremap.split3('rst@food_num',100,200)
                content_dic['rst@food_image_num']=featuremap.split3('rst@food_image_num',60,150)
                food_name_list=featuremap.getfoodname('rst@food_name_list')
                category_list=featuremap.getfoodname('rst@category_list')
                for i in range(0,len(food_name_list)):
                    content_dic[food_name_list[i]]=1
                for i in range(0,len(category_list)):
                    content_dic[category_list[i]]=1
                content_dic.pop('rst@food_name_list')
                content_dic.pop('rst@category_list')
                
                # a little strange of this line
    
                
                new_feature_line=dic2str(content_dic)
                new_line="{0}\t{1}\n".format(label, new_feature_line)
                fo.write(new_line)


#input_file='/Users/wangjun/documents/dict_test.txt'
#output_file='/Users/wangjun/documents/dict_test_out.txt'
#feat_map_file='/Users/wangjun/documents/feat_map.txt'
#oneHot(input_file,output_file,feat_map_file)
