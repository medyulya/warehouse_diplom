import csv
import time
import pandas
from concurrent.futures import ThreadPoolExecutor
import random


def reading_func(date_csv):
    with open(date_csv, 'r') as f:
        reader = csv.reader(f)
        data_table = list(reader)
        return data_table

def create_matrix(data_table):
    products_list = []
    for i, value in enumerate(data_table):
        if i == 0 or data_table[i][2] in products_list:
            continue
        else:
            products_list.append(data_table[i][2])
    datetime_list = []
    for i, value in enumerate(data_table):
        if i == 0 or data_table[i][4] in datetime_list:
            continue
        else:
            datetime_list.append(data_table[i][4])
    date_array = []
    time_array = []
    for i, datetime in enumerate(datetime_list):
        datetime_split = datetime.split()
        date_array.append(datetime_split[0])
        time_array.append(datetime_split[1])
    matrix = pandas.DataFrame(index=[date_array, time_array], columns=products_list)
    for i, value in enumerate(data_table):
        if value[4] in datetime_list and value[2] in products_list:
            if int(value[3]) <= 0:
                continue
            else: matrix.iloc[datetime_list.index(value[4]), products_list.index(value[2])] = value[3]
    return matrix

def time_series_day(dataframe):
    indeсes = []
    data = []
    times_all = []
    for date, time in dataframe.index:
        times_all.append(time)
        if date in indeсes:
            continue
        else: indeсes.append(date)
    for i, value in enumerate(indeсes):
        data.append([])
        for j, value2 in enumerate(dataframe.index):
            if value2[0] == value:
                data[i].append(value2[1])
    time_series_array = pandas.DataFrame(data=data, index=indeсes)
    return time_series_array, times_all
    print(time_series_array)
    print(times_all)

def random_time(times_array, times_list):
    random_times_list = []
    i = 1
    while i <= len(times_list)//len(times_array):
        random_times_list.append(random.choice(times_list))
        i += 1
    print(random_times_list)
    return random_times_list


start_time = time.time()
with ThreadPoolExecutor(16) as p:
    dataframe_result = create_matrix(reading_func('online_retail_II.csv'))
#dataframe_result.to_csv('result.csv')
t1, t2 = time_series_day(dataframe_result)
random_time(t1,t2)
print("--- %s seconds ---" % (time.time() - start_time))
#--- 8696.000891923904 seconds --- без потоков