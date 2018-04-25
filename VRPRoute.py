import VRPNode
import numpy as np

def distance(start,stop):
    """
    Basic distance function for euclidean distance
    :param start: VRPNode as start
    :param stop: VRPNode as stop
    :return: euclidean distance
    """
    return np.sqrt(np.add(np.square(np.subtract(start.x,stop.x)),np.square(np.subtract(start.y - stop.y))))

class VRPRoute:

    def __init__ (self,nodes, capacity = None, length = None, service_duration = None,
                  quality = None, max_capacity = 50, max_service_duration = 60):

        self.nodes = nodes
        self.capacity = capacity
        self.length = length
        self.service_duration = service_duration
        self.quality = quality

        #set standard parameters
        self.max_capacity = max_capacity
        self.max_service_duration = max_service_duration

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



        #get the quality


