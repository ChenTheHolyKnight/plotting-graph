import csv
from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd
import json
import os

# change path to the location of Records folder when you use this on your device
jsonFolderPath = './UserCSV'
path = Path(jsonFolderPath).absolute()


class Test(object):
    def __init__(self, data):
        self.__dict__ = data


def readFile(filename, f):
    dp = path.joinpath(filename)
    data = pd.read_csv(dp)

    


def main():
    directory = 'CombinedCSV'
    if not os.path.exists(directory):
        os.makedirs(directory)

    f = csv.writer(open('./' + directory + '/' + 'combined' + ".csv", "w"))
    f.writerow(
        ["UserName", "O_S0_Shelf", "O_S0_PictureFrame", "O_S0_OfficeChair", "O_S0_CoatStand", "O_S0_Desk",
         "O_S0_Monitor",
         "O_S0_Printer", "O_S1_OfficeChair", "O_S1_Printer", "L_S0_Shelf", "L_S0_Shelf1", "L_S1_RoundBase1",
         "L_S1_RoundVase2",
         "L_S1_Vase", "L_S2_Orchid", "L_S2_CornPlant", "L_S3_StackedBooks", "L_S3_StackedBooks1",
         "L_S4_FlaskPhilodendron", "L_S4_FlaskPhilodendron1", "O_S0_Cup", "O_S0_CupSmall", "O_S0_SmallestCup",
         "O_S1_TallDrawer", "O_S1_Drawer", "O_S2_HospitalBed", "O_S2_ECGMonitor", "O_S2_IVStand"])
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    dp = path.joinpath(onlyfiles[0])
    data = pd.read_csv(dp)
    for file in onlyfiles:
        df = readFile(file, f)

    return


if __name__ == '__main__':
    main()
