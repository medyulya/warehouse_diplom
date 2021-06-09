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
    i = 0
    while i < len(times_list)//len(times_array):
        t = random.choice(times_list)
        if t in random_times_list:
            continue
        else: random_times_list.append(t)
        i += 1
    return random_times_list

def random_data(dataframe, random_times_list):
    count_element = len(dataframe)
    data_list_number = []
    i = 0
    while i < len(random_times_list):
        t = random.randrange(0, count_element)
        data_list_number.append(t)
        i += 1
    new_dataframe = dataframe.iloc[data_list_number]
    new_dataframe.index = random_times_list
    return new_dataframe


start_time = time.time()
dataframe_result = create_matrix(reading_func('test.csv'))
#dataframe_result.to_csv('result.csv')
t1, t2 = time_series_day(dataframe_result)
x = random_time(t1,t2)
print(random_data(dataframe_result, x))
print("--- %s seconds ---" % (time.time() - start_time))
