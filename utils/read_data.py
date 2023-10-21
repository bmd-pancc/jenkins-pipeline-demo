import yaml
import os
def get_data():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')
    fp = open(path + '/data.yaml',encoding='utf8')
    data = yaml.safe_load(fp)
    return data
