"""This module convert file to another filetype
Available convertion is CSV to JSON
"""
import csv
import json
import argparse


def csv2dict(data, delimiter):
    """CSV to json convertion
    """
    reader = csv.DictReader(data, delimiter=delimiter)
    output = []

    for row in reader:
        output.append(row)

    return json.dumps(output)

def handle_result(result, output):
    """Handle ouputing of the result
    """
    if output == 'stdout':
        print(result)
        return None

    f_to_write = open(output, 'w')
    f_to_write.write(result)
    f_to_write.close()

    return None

def convert(file_to_transform, from_format='csv', to_format='dict', **kwargs):
    """Convert type to an other type
    """

    f_to_convert = open(file_to_transform, 'r')
    correspondance = {
        'csv': {
            'dict': csv2dict
        }
    }

    if from_format == 'csv':
        delimiter = kwargs.get('delimiter')
        if not delimiter:
            raise Exception('No delimiter')
        result = correspondance[from_format][to_format](f_to_convert, delimiter=delimiter)
    f_to_convert.close()

    handle_result(result, kwargs['output_file'])

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Convert a file to an other type')
    PARSER.add_argument('--file', help='file to convert')
    PARSER.add_argument('--input-format', default='csv', help='Input format')
    PARSER.add_argument('--output-format', default='json', help='Output format')
    PARSER.add_argument('--output-file', default='stdout', help='Output file')
    PARSER.add_argument('--delimiter', default=',', help='delimiter of the csv')
    ARGS = PARSER.parse_args()

    convert(ARGS.file, delimiter=ARGS.delimiter, output_file=ARGS.output_file)
