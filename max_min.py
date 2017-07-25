from avg import *


def find_max(data_sample, column):
    temp_list = []
    for row in data_sample:
        price = float(row[column])
        temp_list.append(price)
    return max(temp_list)


def find_min(data_sample, column):
    temp_list = []
    for row in data_sample:
        price = float(row[column])
        temp_list.append(price)
    return min(temp_list)


def find_max_min(data_sample, column, m='max'):
    temp_list = []
    val = 0
    for row in data_sample:
        price = float(row[column])
        temp_list.append(price)
    if m == 'max':
        val = max(temp_list)
    elif m == 'min':
        val = min(temp_list)
    else:
        pass
    return val


print(find_max(data_from_csv[1:], 2))
print(find_min(data_from_csv[1:], 2))
print(find_max_min(data_from_csv[1:], 2, 'min'))

price = my_csv['priceLabel']
price_in_float = [float(x) for x in price]
numpy_max = numpy.amax(price_in_float)
print(numpy_max)


numpy_min = numpy.amin(price_in_float)
print(numpy_min)
