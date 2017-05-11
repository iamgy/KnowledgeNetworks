import pandas as pd
import numpy as np
import os
import os.path as op
import inspect
import csv


def colla_count(data, country_list, column_name):
    """
    Function to count collaborations between 2 countries as well as number of
    papers from each country specified
    """
    count = {}
    collaboration = np.zeros((len(country_list), len(country_list)))
    for i in country_list:
        count[i] = 0
    for i in range(0, len(data)):
        string1 = data[column_name][i]
        a = []
        for j in string1.split():
            for k in range(len(country_list)):
                if j.lower() == country_list[k].lower() or j.lower() == (country_list[k].lower() + ';'):
                    if any(i == country_list[k] for i in a):
                        pass
                    else:
                        count[country_list[k]] += 1
                        a.append(country_list[k])
        if len(a) > 1:
            for m in a:
                x_index = country_list.index(m)
                for n in a:
                    if m == n:
                        pass
                    else:
                        y_index = country_list.index(n)
                        collaboration[x_index][y_index] += 1
    for i in range(len(country_list)):
        collaboration[i][i] = count[country_list[i]]

    return collaboration


def wrapping_function(data_source, year, country_list, column_name):
    """
    Wrapping function to count collaborations for a particular year
    """
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = op.join(path, 'data')
    path = op.join(path, data_source)
    path = op.join(path, '%d' % year)
    filelist = os.listdir(path)
    count = np.zeros((len(country_list), len(country_list)))
    for i in filelist:
        filepath = op.join(path, i)
        try:
            data = pd.read_csv(filepath, sep='\t', engine='python', usecols=['C1'], keep_default_na=False, index_col=False)
        except:
            data = pd.read_csv(filepath, sep='\t', engine='python', usecols=['C1'], keep_default_na=False, index_col=False,quoting=csv.QUOTE_NONE)
        result = colla_count(data, country_list, column_name)
        count += result
    return count


def count_all_years(data_source, year_list, country_list, column_name):
    results = []
    for i in year_list:
        count = wrapping_function(data_source, i, country_list, column_name)
        results.append(count)
    return results
