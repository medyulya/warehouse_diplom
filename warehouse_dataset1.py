import csv
import time
import pandas



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

start_time = time.time()
dataframe_result = create_matrix(reading_func('online_retail_II.csv'))
dataframe_result.to_excel('result.xlsx')
print("--- %s seconds ---" % (time.time() - start_time))
