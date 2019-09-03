from os import listdir
from os.path import isfile, join
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# change path to the location of Records folder when you use this on your device
from matplotlib import pyplot

from Stats import do_ks_test, do_man_whitney_u_test

jsonFolderPath = './ProcessedVR First Data .csv'
path = Path(jsonFolderPath).absolute()

jsonFolderPath1 = './ProcessedReading First Data .csv'
path1 = Path(jsonFolderPath1).absolute()


def readFile(filename):
    dp = path.joinpath(filename)
    data = pd.read_csv(dp)
    return data


def process_norm(df1):
    list1 = df1['Qustionnaire1'].values.tolist()
    list2 = df1['Qustionnaire2'].values.tolist()
    list3 = df1['Qustionnaire3'].values.tolist()
    # df2 = readFile(onlyfiles[1])

    pyplot.hist(list1)
    pyplot.show()
    do_ks_test(list1)

    pyplot.hist(list2)
    pyplot.show()
    do_ks_test(list2)

    pyplot.hist(list3)
    pyplot.show()
    do_ks_test(list3)


def normality_test():
    df1 = readFile(path)
    process_norm(df1)

    df2 = readFile(path1)
    process_norm(df2)


def process_whit(df1, df2):
    lista1 = df1['Qustionnaire1'].values.tolist()
    listb1 = df2['Qustionnaire1'].values.tolist()

    do_man_whitney_u_test(lista1, listb1)

    lista2 = df1['Qustionnaire2'].values.tolist()
    listb2 = df2['Qustionnaire2'].values.tolist()
    do_man_whitney_u_test(lista2, listb2)

    lista3 = df1['Qustionnaire3'].values.tolist()
    listb3 = df2['Qustionnaire3'].values.tolist()
    do_man_whitney_u_test(lista3, listb3)


def main():
    # normality_test()

    df1 = readFile(path)
    df2 = readFile(path1)
    process_whit(df1, df2)

    df_total = pd.DataFrame()
    df_total['Questionnaire']
    return


if __name__ == '__main__':
    main()
