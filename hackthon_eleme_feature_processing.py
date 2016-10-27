#feature processing
#encoding='utf-8'
class Featureprocessing:
    def __init__(self,
                 dic_input):
        self.dic_input=dic_input

    def addOne(self,col_name):
        inivalue=self.dic_input[col_name] 
        finalvalue=int(inivalue)+1
        return finalvalue

    def rmfeature(self,col_name):
        value=self.dic_input
        value.pop(col_name)
        return value
    
    def split3(self,col_name,upper_num,lower_num):
        if upper_num<lower_num:
            upper_num,lower_num=lower_num,upper_num
        value=self.dic_input[col_name]
        if value>=upper_num:
            result=3
        else:
            if value<=lower_num:
                result=1
            else:
                result=2
        return result

    def transformweek(self,col_name):
        value=int(self.dic_input[col_name])
        result=value%7
        return result

    def name2num(self,col_name,name_list):
        value=self.dic_input[col_name].strip()
        result=name_list.index(value)+1
        return result

    def calcoincide(self,col_name1,col_name2):
        value1=self.dic_input[col_name1]
        value2=self.dic_input[col_name2]
        list1=value1.split(',')
        list2=value2.split(',')
        coincide_num=len(set(list1)&set(list2))
        return coincide_num

    def resolution(self,col_name):
        value=self.dic_input[col_name]
        if 'x' in value:
            value.replace('"','')
            num=value.split('x')
            #print 'ready'
            result=int(num[0].replace('"',''))*int(num[1].replace('"',''))
            #print 'resolution',result
            return result
            
        else:
            return 500000
    def normalization(self,col_name,min_value,max_value):
        if max_value<min_value:
            min_value,max_value=max_value,min_value
        value=float(self.dic_input[col_name])
        result_value=(value-min_value)/(max_value-min_value)
        return result_value
        

        
#dicttest={'a':1,'b':'a,b,c,d,e','c':'c,d,e'}
#lista=['a','e','f']
#featuremap=Featureprocessing(dicttest)
#print featuremap.rmfeature('a')
#dicttest['d']=featuremap.addOne('b')
#print dicttest
