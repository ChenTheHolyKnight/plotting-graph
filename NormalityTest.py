from os import listdir
from os.path import isfile, join
from pathlib import Path
import seaborn as sns
import numpy as np

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


def draw_box_plot(list1, list2):
    ticks = ['Quiz 1', 'Quiz 2', 'Quiz 3']

    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color="#008000")

    plt.figure()

    bpl = plt.boxplot(list1, positions=np.array(range(len(list1))) * 2.0 - 0.4, widths=0.6, showfliers=True)
    bpr = plt.boxplot(list2, positions=np.array(range(len(list2))) * 2.0 + 0.4, widths=0.6, showfliers=True)
    set_box_color(bpl, '#D7191C')  # colors are from http://colorbrewer2.org/
    set_box_color(bpr, '#2C7BB6')

    # draw temporary red and blue lines and use them to create a legend
    plt.plot([], c='#D7191C', label='Group A (VR First)')
    plt.plot([], c='#2C7BB6', label='Group B (Reading First)')
    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    plt.xlim(-2, len(ticks) * 2)
    plt.tight_layout()
    # plt.show()
    plt.savefig('./' + '/VR_Quiz_Box_Plot' + '.svg')


def main():
    # normality_test()

    df1 = readFile(path)
    df2 = readFile(path1)
    process_whit(df1, df2)

    df_total = pd.DataFrame()
    df_total['VR_1'] = df1['Qustionnaire1']
    df_total['VR_2'] = df1['Qustionnaire2']
    df_total['VR_3'] = df1['Qustionnaire3']

    df_total['Reading_1'] = df2['Qustionnaire1']
    df_total['Reading_2'] = df2['Qustionnaire2']
    df_total['Reading_3'] = df2['Qustionnaire3']

    list1 = [df1['Qustionnaire1'].values.tolist(), df1['Qustionnaire2'].values.tolist(),
             df1['Qustionnaire3'].values.tolist()]
    list2 = [df2['Qustionnaire1'].values.tolist(), df2['Qustionnaire2'].values.tolist(),
             df2['Qustionnaire3'].values.tolist()]
    draw_box_plot(list1, list2)

    # df_total.boxplot(
    #     column=['VR_1', 'Reading_1', 'VR_2', 'Reading_2', 'VR_3', 'Reading_3'])
    #
    # plt.show()
    # plt.savefig('./' + '/VR_Reading_Box_Plot' + '.png')
    return


if __name__ == '__main__':
    main()
