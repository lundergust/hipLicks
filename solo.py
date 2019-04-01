import csv
import pandas
names = ['ii-1', 'ii-2', 'ii-3', 'ii-4', 'ii-5', 'ii-6', 'ii-7', 'ii-8',
         'V-1', 'V-2', 'V-3', 'V-4', 'V-5', 'V-6', 'V-7', 'V-8', 'I-1', 'I-2', 'I-3', 'I-4', 'I-5', 'I-6', 'I-7', 'I-8', 'info']
dataset = pandas.read_csv('licksData.csv', names=names)

# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())
