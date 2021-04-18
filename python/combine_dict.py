# https://youtu.be/Hmg19Z_AKoE
from collections import defaultdict

def combine_dict(*dicts):
    df = defaultdict(list)
    for d in dicts:
        for key in d:
            df[key].append(d[key])
    return dict(df)

dict1 = {'a':2,'b':'foo','c':300}
dict2 = {'a':3,'b':200,'c':500}
print(combine_dict(dict1,dict2))
