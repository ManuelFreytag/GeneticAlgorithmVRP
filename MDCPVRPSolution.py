import VRPRoute
import numpy as np


class MDCPVRPSolution():

    def __init__(self,routes):
        self.routes = []

    def evaluate(self):
        """
        Evaluate the quality of a solution
        """

        #iterate over the route routes and add their solution values
        q = 0
        for r in self.routes:
            q += r.quality
        return q