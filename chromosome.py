import os
import numpy as np
import random
from data_import import Data


def distance(start,stop):
    """
    Basic distance function for euclidean distance

    Args:
        start: VRPNode as start
        stop: VRPNode as stop

    Returns: euclidean distance

    """

    x_dist = np.subtract(start.x, stop.x)
    y_dist = np.subtract(start.y - stop.y)

    x_dist_square = np.square(x_dist)
    y_dist_square = np.square(y_dist)

    return np.sqrt(np.add(x_dist_square, y_dist_square))


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

    pattern_chromosome = {}
    depot_chromosome = {}
    gt_chromosome = []

    # 1) select a random pattern and depot
    for c_node in customers:
        pattern_chromosome[c_node.n_id] = random.choice(c_node.list_visit_comb)
        depot_chromosome[c_node.n_id] = random.choice(depots).n_id

    # 2) create the grand tour chromosome (list of dictionaries)
    for p in range(nr_periods):
        period_tour = {x.n_id:[] for x in depots}  # dictionary of empty lists for depot id
        for c_id in depot_chromosome:  # fill the depot grand tour chromosome based on the previous random selection
            d_id = depot_chromosome[c_id]
            if pattern_chromosome[c_id][p] == 1:
                period_tour[d_id] += [c_id]
        gt_chromosome.append(period_tour)

    return Chromosome(pattern_chromosome, depot_chromosome, gt_chromosome)

class Chromosome:
    def __init__(self, pattern_chromosome, depot_chromosome, gt_chromosome, capacity=None, length=None, service_duration=None, fitness=None):
        self.pattern_chromosome = pattern_chromosome
        self.depot_chromosome = depot_chromosome
        self.gt_chromosome = gt_chromosome # a list of dictionaries
        self.capacity = capacity
        self.length = length
        self.service_duration = service_duration
        self.fitness = fitness

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