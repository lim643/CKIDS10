import utils
import csv

class utils:
    def preprocess_wage(data):
        wage = []
        for row in data:
            for year in ["2018", "2017", "2016", "2015", "2014"]:
                wage.append({"rows": "60", "page": "1", "sidx": "EAW_LST_NAM", "year": year, "lastname": row[2], "firstname": row[0], "location": row[3]})
        return wage

    def read_csv(input_file="../data/input.csv"):
        with open(input_file, 'r') as inputFile:
            data = []
            csv_reader = csv.reader(inputFile)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv():
        return 0 
