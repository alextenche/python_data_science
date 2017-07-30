import sys
import pandas as pd

# ufo = pd.read_csv('http://bit.ly/uforeports')
# ufo.to_csv('data/ufo.csv', sep=',', index=False)


ufo = pd.read_csv('data/ufo.csv')

# print (type(ufo))
print(ufo.head())

# sys.exit('')
print(type(ufo['City']))
print(ufo['City'].head())

print(ufo.City)

print(ufo['Colors Reported'])

new_series = ufo.City + ', ' + ufo.State
print(new_series)

ufo['Location'] = new_series
print(ufo)
