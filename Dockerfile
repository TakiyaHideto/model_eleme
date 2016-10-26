FROM rickyking/ds-xgboost
MAINTAINER wei.zhang15@ele.me

RUN apt-get install -y python python-setuptools python-dev python-numpy python-scipy

WORKDIR /opt/xgboost/python-package

RUN python setup.py install

WORKDIR /
ADD hackathonCaseB.sh /hackathonCaseB.sh
RUN chmod u+x /hackathonCaseB.sh
ADD hackthon_eleme.py /hackthon_eleme.py
ADD hackthon_eleme_data_joining.py /hackthon_eleme_data_joining.py
ADD hackthon_eleme_data_loading.py /hackthon_eleme_data_loading.py
ADD hackthon_eleme_data_structure.py /hackthon_eleme_data_structure.py
ADD hackthon_eleme_feature_engineering.py /hackthon_eleme_feature_engineering.py
ADD configuration_buy.conf /configuration_buy.conf
ADD configuration_clk.conf /configuration_clk.conf
