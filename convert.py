import csv
import json
import argparse
import sys


def csv2dict(data, delimiter):
    reader = csv.DictReader(data, delimiter=delimiter)
    output = []

    for row in reader:
        output.append(row)

    return json.dumps(output)
def handle_result(result, output):
    if output == 'stdout':
        print(result)
        return None

    f = open(output, 'w')
    f.write(result)
    f.close()

    return None

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
        result = correspondance[from_format][to_format](f, delimiter=delimiter)
    f.close()

    handle_result(result, kwargs['output_file'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a file to an other type')
    parser.add_argument('--file', help='file to convert')
    parser.add_argument('--input-format', default='csv', help='Input format')
    parser.add_argument('--output-format', default='json', help='Output format')
    parser.add_argument('--output-file', default='stdout', help='Output file')
    parser.add_argument('--delimiter', default=',', help='delimiter of the csv')
    args = parser.parse_args()

    transform_csv(args.file, delimiter=args.delimiter, output_file=args.output_file)
