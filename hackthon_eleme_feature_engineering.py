
# please write your function of feat engineering below
# notice that data_block and output_file are required to writtern as the necessary paras in all the functions
import os
from hackthon_eleme_feature_processing_all import *  

def feature_engineering(input_file, output_file, feat_map_file):
    file_feat_eng=input_file+'_feateng'
    file_onehot=file_feat_eng+'_onehot'
    featureProcessing(input_file,file_feat_eng)
    oneHot(file_feat_eng,file_onehot,feat_map_file)
    feature2num(file_onehot,output_file,feat_map_file)



  


################### feat eng: one hot ###################
