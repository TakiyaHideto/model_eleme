
import math

def calculate_cosine_distinct(obj1, obj2):
    keys_obj1 = obj1.keys()
    keys_obj2 = obj2.keys()
    value_obj1 = []
    value_obj2 = []
    for key in keys_obj1:
        value_obj1.append(obj1.get(key))
        value_obj2.append(obj2.get(key))


def get_product(vec1, vec2):
    sum = 0.0
    for i in range(0, len(vec1)):
        sum += vec1[i] * vec2[i]
    return math.sqrt(sum)


