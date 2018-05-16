import numpy as np


def distance(start, stop):
    """
    Basic distance function for euclidean distance

    Args:
        start: VRPNode as start
        stop: VRPNode as stop

    Returns: euclidean distance

    """

    x_dist = np.subtract(start.x, stop.x)
    y_dist = np.subtract(start.y, stop.y)

    x_dist_square = np.square(x_dist)
    y_dist_square = np.square(y_dist)

    return np.sqrt(np.add(x_dist_square, y_dist_square))

