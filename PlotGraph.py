from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance


def readFile():
    # change path to the location of Records folder when you use this on your device
    path = Path('E:/Part4Project/PreviousProject/vr-earthquake-lab/VR Earthquake Lab/Records').absolute()
    dp = path.joinpath('Cube (1).csv')
    df = pd.read_csv(dp)
    return df


def plotGraph(df):
    plt.plot(df[df.columns[0]], df[df.columns[1]], 'g--')
    plt.title('displacement vs time')
    plt.ylabel('object displacement')
    plt.xlabel('time')
    #plt.show()
    #Need to give a name for each of the graph when it saves multiple images.
    plt.savefig('./images/test.png')
    return


def main():
    df = readFile()

    plotGraph(df)
    return


if __name__ == '__main__':
    main()
