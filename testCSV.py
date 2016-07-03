import csv
import pandas as pd
import numpy as nm
from pylab import*

folder = 'D:\\STUDY\\3.2\\Project 300\\T20_male_csv\\'
# file_name = folder + teams + '.csv'

for value in range(1,664):
    filename = folder + str(value) + '.csv'

    file=open(filename, "r")

    reader = csv.reader(file)

    for line in reader:
        a = line[20]

    print(value, a)
