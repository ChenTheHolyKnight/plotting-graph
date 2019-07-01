from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt

# change path to the location of Records folder when you use this on your device
csvFolderPath = 'E:/Part4Project/PreviousProject/vr-earthquake-lab/VR Earthquake Lab/Records'
path = Path(csvFolderPath).absolute()


def readFile(filename):
    dp = path.joinpath(filename)
    df = pd.read_csv(dp)
    return df


def plotGraph(df, filename):
    plt.plot(df[df.columns[0]], df[df.columns[1]], 'g--')
    plt.title('displacement vs time')
    plt.ylabel('object displacement')
    plt.xlabel('time')

    sep = '.'
    name = filename.split(sep, 1)[0]
    plt.savefig('./images/' + name + '.png')  # generated plots will be saved inside the images folder
    return


def main():
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        df = readFile(file)
        plotGraph(df, file)

    return


if __name__ == '__main__':
    main()
