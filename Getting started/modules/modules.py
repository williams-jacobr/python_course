import time
import os
import pandas

location = "C:/Users/willi/Desktop/Programming/Python/Python Course/Getting started/processing files/"


while True:
    if os.path.exists(location + 'files/temps_today.csv'):
        data = pandas.read_csv(location + 'files/temps_today.csv')
        print(data.mean())
    else:
        print('File does not exist')
    time.sleep(10)