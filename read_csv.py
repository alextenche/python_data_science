import csv
import numpy

FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'print',
              'material']
DATATYPES = [('myint', 'i'), ('myid', 'i'), ('price', 'f8'), ('names', 'a200'), ('brandId', '<i8'),
             ('brandName', 'a200'), ('imageLink', '|S500'), ('description', '|S900'), ('vendor', '|S100'),
             ('pattern', '|S50'), ('material', '|S50')]


def open_with_csv(filename, d='\t'):
    data = []

    with open(filename, encoding='utf-8') as tsvin:
        tie_reader = csv.reader(tsvin, delimiter=d)
        for line in tie_reader:
            data.append(line)
    return data


def load_data(filename, d='\t'):
    my_csv = numpy.genfromtxt(
        filename,
        delimiter=d,
        skip_header=1,
        invalid_raise=False,
        names=FIELDNAMES,
        dtype=DATATYPES
    )
    return my_csv


data_from_csv = open_with_csv('data.csv')
# print(data_from_csv[0])

my_csv = load_data('data.csv')
