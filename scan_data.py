from read_csv import *


def number_of_records(data_sample):
    return len(data_sample)


def number_of_records_numpy(data_sample):
    return data_sample.size


number_of_ties = number_of_records(data_from_csv)
# print(number_of_ties, 'ties in our data sample')

# print(number_of_records_numpy(my_csv), '')
