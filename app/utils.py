import utils
import csv

class utils:
    def file_path():
        return "../data/input.csv"

    def preprocess(data_node):
        return {
            "rows": "60",
            "page": "1",
            "sidx": "EAW_LST_NAM",
#            "year": data_node['year'],
            "location": data_node['location'],
            "firstname": data_node['firstname'],
            "lastname": data_node['lastname']
        }

    def read_csv(input_file):
        with open(input_file, 'r') as inputFile:
            rows = []
            csv_reader = csv.reader(inputFile)
            for row in csv_reader:
                rows.append(utils.preprocess({"lastname": row[2], "firstname": row[0], "location": row[3]}))
        return rows

    def write_csv(input_file):
        return 0 
