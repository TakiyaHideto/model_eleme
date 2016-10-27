
# please write your function of feat engineering below
# notice that data_block and output_file are required to writtern as the necessary paras in all the functions
import os

def feature_engineering(input_file, output_file, feat_map_file):
    oneHot(input_file, output_file, feat_map_file)


################### feat eng: one hot ###################
feat_cand = [
    'is_select',
    'day_no',
    'minutes',
    'is_new',
    'sort_index',
    'primary_category',
    'agent_fee',
    'good_rating_rate',
    'bu_flag',
    'has_image',
    'min_deliver_amount',
    'is_time_ensure',
    'is_ka',
    'radius',
    'online_payment',
    'is_promotion_info',
    'food_num',
    'food_image_num'
]
feat_cand = set(feat_cand)

onehot_feat_arr = [
    'primary_category',
    'bu_flag'
]
onehot_feat_set = set(onehot_feat_arr)

def oneHot(input_file, output_file, feat_map_file):
    feat_map = {}
    feat_index = 1
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
                    if elements[i].split(":")[0] not in feat_cand:
                        continue
                    try:
                        feat_name = elements[i].split(":")[0]
                        feat_value = elements[i].split(":")[1]
                        if feat_name in onehot_feat_set:
                            feat_name = "{0}_{1}".format(elements[i].split(":")[0],
                                                     elements[i].split(":")[1])
                            feat_value = '1'

                        if not feat_map.has_key(feat_name):
                            feat_index += 1
                            feat_map[feat_name] = str(feat_index)

                        records.append("{0}:{1}".format(feat_map[feat_name], feat_value))
                    except IndexError:
                        print i
                        print elements[i]
                        continue
                fo.write("{0}\t{1}\n".format(label, '\t'.join(records)))
    outputFeatMap(feat_map, feat_map_file)


def outputFeatMap(feat_map, feat_map_file):
    with open(feat_map_file, 'w') as fo:
        for key in feat_map.keys():
            fo.write('{0}:{1}\n'.format(key,
                                        feat_map[key]))


################### feat eng: one hot ###################
