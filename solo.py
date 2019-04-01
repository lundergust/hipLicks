import csv
import pandas
from tabulate import tabulate

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ['ii-1', 'ii-2', 'ii-3', 'ii-4', 'ii-5', 'ii-6', 'ii-7', 'ii-8',
         'V-1', 'V-2', 'V-3', 'V-4', 'V-5', 'V-6', 'V-7', 'V-8', 'I-1', 'I-2', 'I-3', 'I-4', 'I-5', 'I-6', 'I-7', 'I-8']
df = pandas.read_csv('licksData.csv', names=names)

# shape
print(df.shape)
# head
print(df.head(20))
# printing specific columns
# print(df['ii-1'])


# print boolean array indiciating if lick starts on the 1
# print(df['ii-1'] == '1')

# prints all licks that start on 1
# print(df[df['ii-1'] == '1'])

# prints length of set above
print('/////')
print('////')

# descriptions
print(df.describe())
print('')

lick_stats = [['Rest'],['1'],['b2'],['2'],['b3'],['3'],['s3'],['4'],['b5'],['5'],['b6'],['6'],['b7'],['7'],['s7'],['sum']]
for column in df:
    tot = df.shape[0]
    restnum = df[df[column] == 0].shape[0]
    rest = restnum/df.shape[0]
    onenum = df[df[column] == 1].shape[0]
    one = onenum/df.shape[0]
    btwonum = df[df[column] == 1.5].shape[0]
    btwo = btwonum/df.shape[0]
    twonum = df[df[column] == 2].shape[0]
    two = twonum/df.shape[0]
    bthreenum = df[df[column] == 2.5].shape[0]
    bthree = bthreenum/df.shape[0]
    threenum = df[df[column] == 3].shape[0]
    three = threenum/df.shape[0]
    sthreenum = df[df[column] == 3.5].shape[0]
    sthree = sthreenum/df.shape[0]
    fournum = df[df[column] == 4].shape[0]
    four = fournum/df.shape[0]
    bfivenum = df[df[column] == 4.5].shape[0]
    bfive = bfivenum/df.shape[0]
    fivenum = df[df[column] == 5].shape[0]
    five = fivenum/df.shape[0]
    bsixnum = df[df[column] == 5.5].shape[0]
    bsix = bsixnum/df.shape[0]
    sixnum = df[df[column] == 6].shape[0]
    six = sixnum/df.shape[0]
    bsevennum = df[df[column] == 6.5].shape[0]
    bseven = bsevennum/df.shape[0]
    sevennum = df[df[column] == 7].shape[0]
    seven = sevennum/df.shape[0]
    ssevennum = df[df[column] == 7.5].shape[0]
    sseven = ssevennum/df.shape[0]

    sum = restnum+onenum+btwonum+twonum+bthreenum+threenum+sthreenum+fournum+bfivenum+fivenum+bsixnum+sixnum+sevennum+ssevennum

    lick_stats[0].append(rest*100)
    lick_stats[1].append(one*100)
    lick_stats[2].append(btwo*100)
    lick_stats[3].append(two*100)
    lick_stats[4].append(bthree*100)
    lick_stats[5].append(three*100)
    lick_stats[6].append(sthree*100)
    lick_stats[7].append(four*100)
    lick_stats[8].append(bfive*100)
    lick_stats[9].append(five*100)
    lick_stats[10].append(bsix*100)
    lick_stats[11].append(six*100)
    lick_stats[12].append(bseven*100)
    lick_stats[13].append(seven*100)
    lick_stats[14].append(sseven*100)
    lick_stats[15].append(sum)


print(tabulate(lick_stats, headers=names))
