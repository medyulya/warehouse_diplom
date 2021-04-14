import csv
import pandas


def reading_func(date_csv):
    with open(date_csv, 'r') as f:
        reader = csv.reader(f)
        data_table = list(reader)
        return data_table


def create_matrix(data_table):
    products_list = []
    for i, value in enumerate(data_table):
        if data_table[i][3] in products_list:
            continue
        else:
            products_list.append(data_table[i][3])
    datetime_list = []
    for i, value in enumerate(data_table):
        if data_table[i][4] in products_list:
            continue
        else:
            datetime_list.append(data_table[i][4])
    datetime_array = []
    for value in datetime_list:
        datetime_split = value.split()
        datetime_array.append(datetime_split)


create_matrix(reading_func('online_retail_II.csv'))
