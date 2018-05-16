from node import Depot
from node import Customer
from tools import distance
import numpy as np
import os


def binary_decoding(x):
    hex_visit_comb = int(x)
    str_binary_list = list("{0:b}".format(hex_visit_comb))
    binary_list = [int(y) for y in str_binary_list]
    return binary_list


class Data:
    def __init__(self, dat_path):
        """
        Base constructor of the VRP data used in our solver
        NOTE:   All ids set for all nodes are unique and start at 0.
                The min(customer_id) is max(depot_id) +1

        Args:
            dat_path: Path to the data file in txt format

        Class variables:
            type:          Description of problem type to which the data belongs
                            0 (VRP)
                            1 (PVRP)
                            2 (MDVRP)
                            3 (SDVRP)
                            4 (VRPTW)
                            5 (PVRPTW)
                            6 (MDVRPTW)
                            7 (SDVRPTW)

            nr_customers:   Number of customer nodes
            customers:      Customer nodes from VRPNode class
            nr_depots:      Number of depots
            depots:         Depot nodes from VRPNode class
            nr_periods:       Number of periods

        """

        dat_list = []
        with open(dat_path, "r") as file:
            for row in file:
                # get the row data and perform simple preprocessing
                row = row[:-1]  # remove '\n'
                row_list = row.split(" ")  # split at " "
                # cast all values to double and remove empty entries caused by multiple sapces
                row_list = [float(x) for x in row_list if x is not ""]
                dat_list.append(row_list)


        # 1) PROBLEM DESCRIPTION
        prob_desc = dat_list.pop(0)
        self.type = int(prob_desc[0])
        self.nr_customers = int(prob_desc[2])
        self.nr_depots = int(prob_desc[3])
        self.nr_periods = 1 # TODO: Remove hardcoding if necessary

        # 2) DEPOT DESCRIPTION
        id_counter = 0 # set id counter for all current nodes


        depots = []
        for i in range(self.nr_depots):
            depot_vehicle_info = dat_list.pop(0)
            depot_location_info = dat_list.pop(-1)

            tmp_depot = Depot(id_counter, depot_location_info[1], depot_location_info[2], int(prob_desc[1]),
                              depot_vehicle_info[0], depot_vehicle_info[1])
            id_counter += 1

            depots.append(tmp_depot)
        self.depots = depots

        # 3) CUSTOMER DATA
        customers = []
        for i in range(self.nr_customers):
            raw_customer_data = dat_list.pop(0)
            customer_data = [id_counter]
            id_counter += 1
            customer_data += raw_customer_data[1:7]
            customer_data[0] = int(customer_data[0]) # set ID as integer

            # for all visit combinations decode them into a binary array
            # NOTE: ALL OUR DATA IS CURRENTLY ONE PERIOD -> USELESS
            list_visit_comb = []
            for x in raw_customer_data[7:]:
                binary_list = binary_decoding(x)
                list_visit_comb.append(binary_list)
            # As it is currently only one redundant representation only select the first
            #customer_data.append(list_visit_comb)
            # TODO: Make sure that the rep has euqal length all the time
            customer_data.append([list_visit_comb[0]])

            customers.append(Customer(*customer_data))  # create new customer object based on given list
        self.customers = customers

        # 4) SET DISTANCE MATRIX OF ALL NODES (based on id)
        self.distance_matrix = None
        self.set_distance_matrix()

    def set_distance_matrix(self):
        """
        Calculate the distance matrix of between all depots and customers with current sorting.
        (Default: ids are increasing)
        TODO:
        """

        # initialize distance matrix
        m = self.nr_depots +self.nr_customers # get number dimensionality
        distance_matrix = np.zeros((m,m))

        # calculate the distance matrix for all values
        for i,start in enumerate(self.depots + self.customers):
            for j,stop in enumerate(self.depots + self.customers):
                distance_matrix[i,j] = distance(start, stop)

        self.distance_matrix = distance_matrix


if __name__ == "__main__":
    # create data instances
    data_files = []
    cwd = os.getcwd()
    for i in range(1, 10):
        path = cwd + "\\data\\pr" + str(i).zfill(2) + ".txt"  # iterate through files
        data_files = data_files + [Data(path)]