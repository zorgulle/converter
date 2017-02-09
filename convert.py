import csv

def csv2dict(data, delimiter):
    reader = csv.DictReader(data, delimiter=delimiter)
    output = []

    for row in reader:
        output.append(row)

    print(output)

def transform_csv(file_to_transform, from_format='csv', to_format='dict', **kwargs):
    f = open(file_to_transform, 'r')
    correspondance = {
        'csv': {
            'dict': csv2dict
        }
    }

    if from_format == 'csv':
        delimiter = kwargs.get('delimiter')
        if not delimiter:
            raise Exception('No delimiter')
        correspondance[from_format][to_format](f, delimiter=delimiter)

    f.close()

if __name__ == '__main__':
    file_path = '/tmp/toto.csv'
    delimiter = ','
    transform_csv(file_path, delimiter=delimiter)
