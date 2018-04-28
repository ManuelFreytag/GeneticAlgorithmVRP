from VRPNode import
import pandas as pd
import os

class Data:

    def __init__(self):
        self.type = None #type of the problem
        self.customers = None
        self.depots = None

    def __init__(self,path):
        dat = pd.read_csv(path,  sep="\t", header = False)

        # 1) set the problem type
        self.type = dat.iloc[0,0]

        # 2) set number of vehicles/depot
        nr_dep = dat.iloc[0,3]
        dat.iloc[nr_dep+1]



        # check row number till the first not null entry
        # -> splitt first and last part

        # initialize depots
        print(dat)
        return None

if __name__ = "__main__":
    #create data instances
    data_files = []
    cwd = os.getcwd()
    for i in range(1,10):
        path = cwd + "\\data\\pr" + str(i).zfill(2) + ".csv"  # iterate through files
        data_files = data_files + [Data(path)]