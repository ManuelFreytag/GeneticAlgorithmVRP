import VRPRoute
import numpy as np


class MDCPVRPSolution():

    def __init__(self,routes):
        self.population = []

    def random_population_initialization(self):
        #TODO

        # TODO: Implementation of the population init of the paper
        return None


    def evaluation(self):
        #TODO
        return None

    def selection(self):
        #TODO
        return None

    def crossover(self):
        #TODO
        return None

    def mutation(self):
        #TODO
        return None

    def evaluate(self):
        """
        Evaluate the quality of a solution
        """

        #iterate over the route routes and add their solution values
        q = 0
        for r in self.routes:
            q += r.quality
        return q