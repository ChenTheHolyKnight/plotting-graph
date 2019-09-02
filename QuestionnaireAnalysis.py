from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt

# change path to the location of Records folder when you use this on your device
csvFolderPath = './UserQuestionnaire'
path = Path(csvFolderPath).absolute()


def readFile(filename):
    dp = path.joinpath(filename)
    df = pd.read_csv(dp)
    dflist = df.values.tolist()
    q1counts = []
    q2counts = []
    q3counts = []
    for items in dflist:
        count1 = 0
        count2 = 0
        count3 = 0
        index = 0
        for item in items:
            if item is True:
                if index <= 5:
                    count1 = count1 + 1
                elif index <= 10:
                    count2 = count2 + 1
                elif index <= 15:
                    count3 = count3 + 1
            index = index + 1

        q1counts.append(count1)
        q2counts.append(count2)
        q3counts.append(count3)

    df['Qustionnaire1'] = q1counts
    df['Qustionnaire2'] = q2counts
    df['Qustionnaire3'] = q3counts
    return df


def plotGraph(df, filename):
    x = df[df.columns[0]]
    y0 = df[df.columns[1]]
    y1 = df[df.columns[2]]
    y2 = df[df.columns[3]]
    y3 = df[df.columns[4]]

    plt.figure(figsize=(20, 8))
    plt.subplot(2, 2, 1)
    plt.plot(x, y0, 'g--')
    plt.title('x-orientation vs time')
    plt.ylabel('object orientation')
    plt.xlabel('time')

    plt.subplot(2, 2, 2)
    plt.plot(x, y1, 'b--')
    plt.title('y-orientation vs time')
    plt.ylabel('object orientation')
    plt.xlabel('time')

    plt.subplot(2, 2, 3)
    plt.plot(x, y2, 'r--')
    plt.title('z-orientation vs time')
    plt.ylabel('object orientation')
    plt.xlabel('time')

    plt.subplot(2, 2, 4)
    plt.plot(x, y3, 'y--')
    plt.title('displacement vs time')
    plt.ylabel('object orientation')
    plt.xlabel('time')

    plt.tight_layout()
    sep = '.'
    name = filename.split(sep, 1)[0]
    # plt.savefig('./UserQuestionnaire/' + name + '.png')  # generated plots will be saved inside the images folder
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    return


def main():
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        df = readFile(file)
        # plotGraph(df, file)
        df.to_csv('VR Processed Data.csv')
    return


if __name__ == '__main__':
    main()
