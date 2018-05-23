import os
import numpy as np
import random
from data_import import Data


def get_sub_tour_length(distance_matrix, tour):
    """
    Calculate the tour distance

    Args:
        distance_matrix: distance matrix of all nodes
        tour: Iterable with the depot on position 0

    Returns: tour distance of all nodes

    """

    tour_distance = 0
    for i in range(1,len(tour)):
        start = tour[i-1]
        stop = tour[i]
        tour_distance += distance_matrix[start,stop] # NODE ID starts at 1

    # add the distance from the depot end to depot
    distance_matrix[tour[-1],tour[0]]

    return tour_distance


def random_chromosome(data):
    """
    Generate a random solution based on a given data object (might be infeasible)
    Args:
        data: data object in form of a MDPVP

    Returns: randomized chromosome

    """
    depots = data.depots
    customers = data.customers
    nr_periods = data.nr_periods

    depot_chromosome = {}
    gt_chromosome = {x.n_id:[] for x in depots}

    # 1) select a random pattern and depot
    for c_node in customers:
        depot_chromosome[c_node.n_id] = random.choice(depots).n_id

    # 2) create the grand tour chromosome (list of dictionaries)
    for c_id in depot_chromosome:  # fill the depot grand tour chromosome based on the previous random selection
        d_id = depot_chromosome[c_id]
        gt_chromosome[d_id] += [c_id]

    return Individual(data, depot_chromosome, gt_chromosome)


class Individual:
    def __init__(self, data, depot_chromosome, gt_chromosome, capacity=None, length=None, service_duration=None, fitness=None):
        self.data = data
        # CHROMOSOME
        self.depot_chromosome = depot_chromosome
        self.gt_chromosome = gt_chromosome # a list of dictionaries

        # CHROMOSOME DESCRIPTION
        self.capacity = capacity
        self.length = length
        self.service_duration = service_duration
        self.fitness = fitness
        self.feasibility = False

    def set_length(self):
        """
        Calculate the distance for each route in the grand tour chromosome
        Set the the values identical to the gt chromosome documentation
        """
        # for each depot / vehicle / periode check if it exceeds the limit
        print(self.gt_chromosome)
        length_list = {}
        for d_id in self.gt_chromosome:
            # add depot to start of route
            tour = [d_id] + self.gt_chromosome[d_id]
            length = get_sub_tour_length(self.data.distance_matrix, tour)

            # solution documentation
            length_list[d_id] = length
        self.length = length_list

    def set_feasibility(self):

        return

    def evaluate(self):
        """
        TODO:

        Returns:

        """
        nodes = self.nodes()
        length = np.double()
        capacity = np.double()
        service_duration = np.double()

        #We start from -1 to also consider the depot
        for i in range(-1,len(nodes)):
            node = nodes[i]

            if(type(node) == "VRPOCustomer"):
                #TODO:Test if type check works
                # get the capacity
                capacity = np.add(capacity, nodes[i].demand)
                # get service_duration
                service_duration = np.add(service_duration, nodes[i].service_dur)

            #get the length
            #TODO


if __name__ == "__main__":
    data_files = []
    cwd = os.getcwd()
    for i in range(1, 10):
        path = cwd + "\\data\\pr01.txt"  # iterate through files
        data = Data(path)
        sol1 = random_chromosome(data)
        sol1.set_length()