from filter import *

gucci_ties = filter_col_by_string(data_from_csv, 'brandName', 'Gucci')
jcrew_ties = filter_col_by_string(data_from_csv, 'brandName', 'J.Crew')

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max_min(jcrew_ties[1:], 2)

print('maximum {} tie price is ${:03.2f} '.format('Gucci', max_gucci))
print('maximum {} tie price is ${:03.2f} '.format('J.Creq', max_jcrew))

avg_gucci = find_average(gucci_ties, True)
avg_jcrew = find_average(jcrew_ties, True)
print('average {} tie price is ${:03.2f} '.format('Gucci', avg_gucci))
print('average {} tie price is ${:03.2f} '.format('J.Creq', avg_jcrew))

striped_ties = filter_col_by_string(data_from_csv, 'print', '_striped')
print_ties = filter_col_by_string(data_from_csv, 'print', '_print')
paisley_ties = filter_col_by_string(data_from_csv, 'print', '_paisley')
solid_ties = filter_col_by_string(data_from_csv, 'print', '_solid')

print('average {} tie price is ${:03.2f} '.format('striped', find_average(striped_ties, True)))
print('average {} tie price is ${:03.2f} '.format('print', find_average(print_ties, True)))
print('average {} tie price is ${:03.2f} '.format('paisley', find_average(paisley_ties, True)))
print('average {} tie price is ${:03.2f} '.format('solid', find_average(solid_ties, True)))
