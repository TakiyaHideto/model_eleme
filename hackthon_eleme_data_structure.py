############################# define data structure #############################
# eco_env data handler
class DataEcoEnvHandler:
    def __init__(self):
        self.data_handler = {
            'list_id': 0,
            'is_select': 1,
            'day_no': 2,
            'minutes': 3,
            'eleme_device_id': 4,
            'is_new': 5,
            'x': 6,
            'y': 7,
            'user_id': 8,
            'network_type': 9,
            'platform': 10,
            'brand': 11,
            'model': 12,
            'network_operator': 13,
            'resolution': 14,
            'channel': 15
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# eco_info data handler
class DataEcoInfoHandler:
    def __init__(self):
        self.data_handler = {
            'log_id': 0,
            'list_id': 1,
            'restaurant_id': 2,
            'sort_index': 3,
            'is_click': 4,
            'is_buy': 5,
            'is_raw_buy': 6,
            'order_id': 7
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# order info data handler
class DataOrderInfoHandler:
    def __init__(self):
        self.data_handler = {
            'day_no': 0,
            'minutes': 1,
            'order_id': 2,
            'restaurant_id': 3,
            'deliver_fee': 4,
            'is_online_paid': 5,
            'order_process_minutes': 6,
            'restaurant_num': 7,
            'address_type': 8,
            'is_valid': 9,
            'is_book': 10,
            'is_coupon': 11,
            'is_invoice': 12,
            'pindan_flag': 13,
            'x': 14,
            'y': 15,
            'bu_flag_name': 16,
            'eleme_order_total': 17,
            'total': 18,
            'cut_money': 19,
            'is_activity': 20,
            'has_new_user_subsidy': 21,
            'hongbao_amount':22,
            'receiver_deliver_fee': 23,
            'user_id': 24,
            'food_name': 25,
            'food_category': 26
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)


# rst info data handler
class DataRstInfoHandler:
    def __init__(self):
        self.data_handler = {
            'restaurant_id': 0,
            'primary_category': 1,
            'food_name_list': 2,
            'category_list': 3,
            'x': 4,
            'y': 5,
            'agent_fee': 6,
            'is_premium': 7,
            'address_type': 8,
            'good_rating_rate': 9,
            'has_image': 10,
            'has_food_img': 11,
            'min_deliver_amount': 12,
            'time_ensure_spent': 13,
            'is_time_ensure':14,
            'is_ka': 15,
            'is_time_ensure_discount': 16,
            'is_eleme_deliver': 17,
            'bu_flag': 18,
            'brand_name': 19,
            'service_rating': 20,
            'invoice': 21,
            'online_payment': 22,
            'public_degree': 23,
            'food_num': 24,
            'food_image_num': 25,
            'is_promotion_info': 26,
            'is_bookable': 27
        }

    def getNameIndex(self, feat_name):
        if feat_name not in self.data_handler.keys():
            print "wrong feature name"
            return -1
        return self.data_handler.get(feat_name)
############################# define data structure #############################
