import utils

class utils:
    def preprocess(data_node):
        return {
            "rows": "60",
            "page": "1",
            "sidx": "EAW_LST_NAM",
            "year": data_node['year'],
            "location": data_node['location'],
            "firstname": data_node['firstname'],
            "lastname": data_node['lastname']
        }

    def input():
        return None
    def output():  
        return None                                              
