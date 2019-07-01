from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt


def readFile(filename):
    # change path to the location of Records folder when you use this on your device
    path = Path('E:/Part4Project/PreviousProject/vr-earthquake-lab/VR Earthquake Lab/Records').absolute()
    dp = path.joinpath(filename)
    df = pd.read_csv(dp)
    return df


def plotGraph(df, filename):
    plt.plot(df[df.columns[0]], df[df.columns[1]], 'g--')
    plt.title('displacement vs time')
    plt.ylabel('object displacement')
    plt.xlabel('time')
    # Need to give a name for each of the graph when it saves multiple images.
    sep = '.'
    name = filename.split(sep, 1)[0]
    plt.savefig('./images/' + name + '.png')
    return


def main():
    path = Path('E:/Part4Project/PreviousProject/vr-earthquake-lab/VR Earthquake Lab/Records').absolute()
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        df = readFile(file)
        plotGraph(df, file)

    return


if __name__ == '__main__':
    main()
