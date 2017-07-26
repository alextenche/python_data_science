from max_min import *


def create_bool_filed_from_search_term(data_sample, search_term):
    new_array = []
    new_array.append(data_sample[0].append(search_term))

    for row in data_sample:
        new_bool_filed = False
        if search_term in row[7]:
            new_bool_filed = True

        row.append(new_bool_filed)
        new_array.append(row)
    return new_array


def filter_col_by_bool(data_sample, col):
    matches_search_term = []
    for item in data_sample[1:]:
        if item[col]:
            matches_search_term.append(item)
    return matches_search_term


def filter_col_by_string(data_sample, field, filter_condition):
    filtered_rows = []
    col = int(data_sample[0].index(field))
    filtered_rows.append(data_sample[0])
    for item in data_sample[1:]:
        if item[col] == filter_condition:
            filtered_rows.append(item)
    return filtered_rows


def filter_col_by_float(data_sample, field, direction, filter_condition):
    filtered_rows = []
    col = int(data_sample[0].index(field))
    cond = float(filter_condition)

    for row in data_sample[1:]:
        element = float(row[col])
        if direction == '<':
            if element < cond:
                filtered_rows.append(row)
        elif direction == '<=':
            if element <= cond:
                filtered_rows.append(row)
        elif direction == '>':
            if element > cond:
                filtered_rows.append(row)
        elif direction == '>=':
            if element >= cond:
                filtered_rows.append(row)
        elif direction == '==':
            if element == cond:
                filtered_rows.append(row)
        else:
            pass

    return filtered_rows


my_new_csv = create_bool_filed_from_search_term(data_from_csv, 'cashmere')
number_of_cashmere_ties = number_of_records(filter_col_by_bool(my_new_csv, 11))
print('Length: ', number_of_cashmere_ties)

silk_ties = filter_col_by_string(data_from_csv, 'material', '_silk')
wool_ties = filter_col_by_string(data_from_csv, 'material', '_wool')
cotton_ties = filter_col_by_string(data_from_csv, 'material', '_cotton')

gucci_ties = filter_col_by_string(data_from_csv, 'brandName', 'Gucci')

print('found {} silk ties '.format(number_of_records(silk_ties)))
print('found {} wool ties '.format(number_of_records(wool_ties)))
print('found {} cotton ties '.format(number_of_records(cotton_ties)))

print('found {} Gucci ties '.format(number_of_records(gucci_ties)))

under_20_bucks = filter_col_by_float(data_from_csv, 'priceLabel', '<', 20)
print('found {} under 20 bucks ties '.format(number_of_records(under_20_bucks)))
