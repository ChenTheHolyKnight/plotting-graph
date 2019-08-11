import csv
from pathlib import Path
from os import listdir
from os.path import isfile, join
import pandas as pd
import json

# change path to the location of Records folder when you use this on your device
jsonFolderPath = 'E:/Part4Project/PlotComponents/UserData'
path = Path(jsonFolderPath).absolute()


class Test(object):
    def __init__(self, data):
        self.__dict__ = data


def readFile(filename):
    dp = path.joinpath(filename)
    with open(dp, 'r') as json_file:
        data = json.load(json_file)

    test1 = Test(data)
    office = test1.scenarios[0]
    print(office["ScenarioName"])
    OfficeStage = office["stages"]
    print(office["stages"][0])
    # questions = office["stages"][0]["questions"]

    f = csv.writer(open("test.csv", "w"))
    f.writerow(["user", "scenario", "stage", "object_name", "correctness"])

    for scenario in test1.scenarios:
        scenario_name = scenario["ScenarioName"]
        for stage in scenario["stages"]:
            stage_num = stage["StageNumber"]
            questions = stage["questions"]
            for question in questions:
                # print(filename + " " + scenario_name + " " + str(stage_num) + " " + question["ObjectName"] +" "+ str(question["IsCorrect"]))
                f.writerow([filename,
                            scenario_name,
                            stage_num,
                            question["ObjectName"],
                            question["IsCorrect"]])


def main():
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        df = readFile(file)

    return


if __name__ == '__main__':
    main()
