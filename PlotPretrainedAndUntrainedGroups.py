from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

jsonFolderPath = './HadEarthquakeDrills.csv'
path = Path(jsonFolderPath).absolute()

jsonFolderPath1 = './DidnotHaveEarthquakeDrill.csv'
path1 = Path(jsonFolderPath1).absolute()


def readFile(filename):
    dp = path.joinpath(filename)
    data = pd.read_csv(dp)
    return data


def main():
    df1 = readFile(path)
    df2 = readFile(path1)

    df_total = pd.DataFrame()
    df_total['Trained'] = df1['Questionnaire1']
    df_total['Untrained'] = df2['Questionnaire1']

    df_total.boxplot(column=['Trained', 'Untrained'])
    plt.tight_layout()
    plt.savefig('./' + '/VR_Reading_Box_Plot' + '.svg')
    return


if __name__ == '__main__':
    main()
