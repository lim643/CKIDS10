import utils
import csv
import string

class utils:
    def preprocess_wage(data):
        wage = []
        for row in data[1:]:
            for year in ["2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"]:
                wage.append({"rows": "60", "page": "1", "sidx": "EAW_LST_NAM", "year": year, "lastname": row[2], "firstname": row[0], "location": row[3]})
        return wage

    def preprocess_scholar(data):
        scholar = []
        for row in data[1:]:
            scholar.append(row[0] + row[1] + ' ' + row[2] + ', ' + row[3])
        return scholar

    def preprocess_uc(data):
        directory = []
        for row in data[1:]:
             directory.append({'First': row[0].rstrip(), 'Middle': row[1], 'Last': row[2], 'Location': row[3]})
        return directory

    def read_csv(input_file="../data/input.csv"):
        with open(input_file, 'r') as inputFile:
            data = []
            csv_reader = csv.reader(inputFile)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv(wage_data, scholar_data, uc_data, output_file="../data/output.csv"):
        with open(output_file, 'w') as outputFile:
            csv_writer = csv.writer(outputFile, delimiter=',')
            csv_writer.writerow(['Year', 'Institution', 'First Name', 'Last Name', 'Title', 'Gross Pay', 'Regular Pay', 'Overtime Pay', 'Other', 'Faculty Title', 'Department', 'Education', 'h-index', 'i10-index', 'number of citations'])
            for wage in wage_data:
                wage_name = (wage[2] + wage[3]).translate({ord(c): None for c in string.whitespace})
                wage_name = wage_name.replace('.', '')

                for record in uc_data:
                    record_name = (record['Name']).translate({ord(c): None for c in string.whitespace})
                    if wage_name == record_name:
                        if 'Title' in record: 
                            wage.append(record['Title'])
                        else:
                            wage.append(' ')
                        if 'Department' in record:
                            wage.append(record['Department'])
                        else:
                            wage.append(' ')
                        if 'Education' in record: 
                            wage.append(record['Education'])
                        else:
                            wage.append(' ')
                    else:
                        wage.append(' ')
                        wage.append(' ')
                        wage.append(' ')

                for record in scholar_data:
                    scholar_name = (record[0]).translate({ord(c): None for c in string.whitespace})
                    if wage_name == scholar_name:
                        for index in record[1:]:
                            wage.append(index)

                csv_writer.writerow(wage)
