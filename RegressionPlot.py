from pathlib import Path
from os import listdir
from os.path import isfile, join, splitext
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# change path to the location of Records folder when you use this on your device
csvFolderPath = 'D:/Edwin/UniversityOfAuckland/UOA2019/Part4Project/ProcessedUserQuestionnaire'
path = Path(csvFolderPath).absolute()

def readFile(filename):
    dp = path.joinpath(filename)
    df = pd.read_csv(dp)
    print(df.head())
    print(df.tail())
    return df

def plotGraph(df, filename):
    x = df[df.columns[2]].values.reshape(1, -1)
    y = df[df.columns[3]].values.reshape(1, -1)

    # plt.figure(figsize=(20, 8))
    # plt.plot(x, y, 'ro')
    # plt.xlim(0, 5)
    # plt.ylim(0, 5)
    # sep = '.'
    # name = filename.split(sep, 1)[0]
    # plt.savefig(csvFolderPath + '/' + name + '.png')

    model = LinearRegression()
    model.fit(x, y)
    #r_sq = model.score(x, y)

    predictions = model.predict(x)
    plt.scatter(x, y, 'black')
    plt.plot(x, predictions, 'blue', 2)
    #print('coefficient of determination:', r_sq)

    sep = '.'
    name = filename.split(sep, 1)[0]
    plt.savefig(csvFolderPath + '/' + name + '.png')

    return


def main():
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)
    for file in onlyfiles:
        df = readFile(file)
        plotGraph(df, file)
    return



if __name__ == '__main__':
    main()