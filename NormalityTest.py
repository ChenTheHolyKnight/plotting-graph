from os import listdir
from os.path import isfile, join
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# change path to the location of Records folder when you use this on your device
from Stats import do_ks_test

jsonFolderPath = './ProcessedVR First Data .csv'
path = Path(jsonFolderPath).absolute()


def readFile(filename):
    dp = path.joinpath(filename)
    data = pd.read_csv(dp)
    return data


def main():


    df1 = readFile(path)
    list1 = df1['Qustionnaire1'].values.tolist()
    # df2 = readFile(onlyfiles[1])

    do_ks_test()
    return


if __name__ == '__main__':
    main()
