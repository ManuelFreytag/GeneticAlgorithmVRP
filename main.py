import pandas as pd
import math

df = pd.read_excel("D:\\OneDrive\\10_Project_Datascience\Java\computational_logistics\src\TSP.xlsx")


class TSPSolution:
    def eucl_dist_m(self, x, y):
        return [[math.sqrt(sum([(val[i] - val[j]) ** 2 for val in (x, y)])) for j in range(len(y))] for i in
                range(len(x))]

    def manh_dist_m(self, x, y):
        return [[(sum([abs(val[i] - val[j]) for val in (x, y)])) for j in range(len(y))] for i in range(len(x))]



class TSPData:
    id_values = []
    x_values = []
    y_values = []

    def __init__(self, id_values=[], x_values=[], y_values=[]):
        self.id_values = id_values
        self.x_values = id_values
        self.y_values = y_values;

    def addCustomer(self, x, y):
        self.x_values += [x]
        self.y_values += [y]

if __name__ == "__main__":
    x = list(df["x coordinate"])
    y = list(df["y coordinate"])

    # create data
    dat = TSPData()
    for i in range(len(x)):
        dat.addCustomer(x[i], y[i])

    inst = TSPSolution()
    print(inst.eucl_dist_m(x, y))
    print(inst.manh_dist_m(x, y))