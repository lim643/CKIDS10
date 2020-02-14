import utils
import csv

class utils:
    def file_path():
        return "../data/input.csv"

    def read_csv(input_file):
        with open(input_file, 'r') as inputFile:
            rows = []
            csv_reader = csv.reader(inputFile)
            for row in csv_reader:
                for year in ["2018", "2017", "2016", "2015", "2014"]:
                    rows.append({"rows": "60", "page": "1", "sidx": "EAW_LST_NAM", "year": year, "lastname": row[2], "firstname": row[0], "location": row[3]})
        return rows

    def write_csv(input_file):
        return 0 
