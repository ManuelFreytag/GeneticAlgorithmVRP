from VRPNode import Depot
from VRPNode import Customer
import os


class Data:
    def __init__(self, dat_path):
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
        self.type = prob_desc[0]
        self.nr_customers = int(prob_desc[2])
        self.nr_depots = int(prob_desc[3])

        # 2) Depot description
        depots = []
        for i in range(self.nr_depots):
            depot_vehicle_info = dat_list.pop(0)
            depot_location_info = dat_list.pop(-1)

            tmp_depot = Depot(depot_location_info[0], depot_location_info[1], depot_location_info[2], int(prob_desc[1]),
                              depot_vehicle_info[0], depot_vehicle_info[1])

            depots.append(tmp_depot)
        self.depots = depots

        # 2) CUSTOMER DATA
        # 2.1) parse customer data
        customers = []
        for i in range(self.nr_customers):
            raw_customer_data = dat_list.pop(0)

            customer_data = raw_customer_data[:7]

            # for all visit combinations decode them into a binary array
            # NOTE: ALL OUR DATA IS CURRENTLY ONE PERIOD -> USELESS
            list_visit_comb = []
            for x in raw_customer_data[7:]:
                hex_visit_comb = int(x)
                str_binary_list = list("{0:b}".format(hex_visit_comb))
                binary_list = [int(y) for y in str_binary_list]
                list_visit_comb.append(binary_list)
            customer_data.append(list_visit_comb)

            customers.append(Customer(*customer_data))  # create new customer object based on given list
        self.customers = customers


if __name__ == "__main__":
    # create data instances
    data_files = []
    cwd = os.getcwd()
    for i in range(1, 10):
        path = cwd + "\\data\\pr" + str(i).zfill(2) + ".txt"  # iterate through files
        data_files = data_files + [Data(path)]