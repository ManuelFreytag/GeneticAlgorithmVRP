import node
import numpy as np


def distance(start,stop):
    """
    Basic distance function for euclidean distance
    :param start: VRPNode as start
    :param stop: VRPNode as stop
    :return: euclidean distance
    """
    x_dist = np.subtract(start.x, stop.x)
    y_dist = np.subtract(start.y - stop.y)

    x_dist_square = np.square(x_dist)
    y_dist_square = np.square(y_dist)

    return np.sqrt(np.add(x_dist_square, y_dist_square))


class VRPRoute:
    def __init__(self, nodes, capacity=None, length=None, service_duration=None, fitness=None):

        self.nodes = nodes
        self.capacity = capacity
        self.length = length
        self.service_duration = service_duration
        self.fitness = fitness

    def evaluate(self):
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