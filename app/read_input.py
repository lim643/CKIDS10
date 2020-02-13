import csv


def read_csv(input_file):
    """
    return: {'headers': ['First Name', 'Last Name', 'Institution'], 
             'rows': [['KHALEEL', 'ABDULRAZAK', 'Riverside'],
                      ['CYNTHIA', 'CHUANG', 'San Francisco'],
                       ...]}
    """
    ret = {}
    with open(input_file, 'r') as inputFile:
        rows = []
        csv_reader = csv.reader(inputFile)
        ret['headers'] = [h.strip() for h in next(csv_reader) if not h.startswith('Middle')]
        for row in csv_reader:
            rows.append([r.strip() for r in row if len(r)>1])
        ret['rows'] = rows
    return ret
