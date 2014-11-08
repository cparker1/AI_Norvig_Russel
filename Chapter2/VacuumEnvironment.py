import matplotlib.pyplot as plt
import numpy as np
import Vacuum
from random import randint
__author__ = "Charles A. Parker"

# TODO use logging module


# The task from Artificial Intelligence: A Modern Approach by Russel and Norvig

# 2.5 Implement a performance-measuring environment simulator for the vacuum-cleaner world.
# This world can be described as follows:

# Percepts: Each vacuum-cleaner agent gets a three-element percept vector on each turn.
# The first element, a touch sensor, should be a 1 if the machine has bumped into something
# and a 0 otherwise. The second comes from a photosensor under the machine, which emits
# a 1 if there is dirt there and a 0 otherwise. The third comes from an infrared sensor, which
# emits a 1 when the agent is in its home location, and a 0 otherwise.

# Actions: There are five actions available: go forward, turn right by 90 deg, turn left by 90 deg,
# suck up dirt, and turn off.

# Goals: The goal for each agent is to clean up and go home. To be precise, the performance
# measure will be 100 points for each piece of dirt vacuumed up, minus 1 point for each
# action taken, and minus 1000 points if it is not in the home location when it turns itself off.

# Environment: The environment consists of a grid of squares. Some squares contain
# obstacles (walls and furniture) and other squares are open space. Some of the open squares
# contain dirt. Each "go forward" action moves one square unless there is an obstacle in that
# square, in which case the agent stays where it is, but the touch sensor goes on. A "suck up
# dirt" action always cleans up the dirt. A "turn off" command ends the simulation.

# We can vary the complexity of the environment along three dimensions:

# Room shape: In the simplest case, the room is an n x n square, for some fixed n. We can
# make it more difficult by changing to a rectangular, L-shaped, or irregularly shaped room,
# or a series of rooms connected by corridors.

# Furniture: Placing furniture in the room makes it more complex than an empty room. To
# the vacuum-cleaning agent, a piece of furniture cannot be distinguished from a wall by
# perception; both appear as a 1 on the touch sensor.

# Dirt placement: In the simplest case, dirt is distributed uniformly around the room. But
# it is more realistic for the dirt to predominate in certain locations, such as along a heavily
# travelled path to the next room, or in front of the couch.

# def get_rand_weighted_val(values, probabilities):
#     bins = np.add.accumulate(probabilities)
#     return values[np.digitize(np.random.random_sample(1), bins)]

def get_rand_weighted_val(value_probability_pair):
    """
    Useful for setting up environments.  Pass in a list of tuples
    where the first value in the tuple is the value, and the
    second value is the probability of the first value being returned.
    The probabilities will be normalized by their value relative to
    sum of the passed in probabilities.
    """
    probabilities = [pair[1] for pair in value_probability_pair]
    prob_sum = sum(probabilities)
    bins = np.add.accumulate(probabilities)
    return value_probability_pair[np.digitize(prob_sum * np.random.random_sample(1), bins)][0]


# TODO do I really need this class?...
class Dirt(object):
    """
    This is a placeholder.  It doesn't do anything
    but indicate that dirt is in a cell!

    Also have static methods defined here for setting
    up an environment
    """
    @staticmethod
    def dump_dirt(environment, positions):
        for x, y in positions:
            environment.add_object_to_cell(x, y, Dirt())
        pass

    @staticmethod
    def dump_rand_dirt(environment, count):
        positions = []
        for n in range(count):
            rand_x = randint(0, environment.xdim - 1)
            rand_y = randint(0, environment.ydim - 1)
            positions.append((rand_x, rand_y))
        Dirt.dump_dirt(environment, positions)


class Furniture(object):
    pass


class Wall(object):
    pass


class VacuumHome(object):
    pass


class VacuumEnvironment(object):
    """
    This class contains the map of the envirnoment.  It
    holds all the objects that exist in it, and also
    governs the operation of each object.  Objects can
    send a request to perform an action, and the environment
    returns the actions result.

    Each cell in the environment has a list of objects occupying
    that cell.
    """

    def __init__(self):
        self._xdim = 0
        self._ydim = 0
        pass

    @property
    def xdim(self):
        return self._xdim

    @xdim.setter
    def xdim(self, value):
        self._xdim = value

    @property
    def ydim(self):
        return self._ydim

    @ydim.setter
    def ydim(self, value):
        self._ydim = value

    def set_dimensions(self, xdim, ydim):
        self._xdim = xdim
        self._ydim = ydim
        self._env = [[[] for n in range(xdim)] for n in range(ydim)]

    def get_cell_contents(self, x, y):
        try:
            return self._env[y][x]
        except:
            return None

    def add_object_to_cell(self, x, y, thing):
        self._env[y][x].append(thing)

    def check_for_object_in_cell(self, x, y, thing):
        return any(isinstance(item, thing) for item in self.get_cell_contents(x, y))

    def remove_object_from_cell(self, x, y, thing):
        try:
            get_cell_contents(x, y).remove(thing)
        except ValueError:
            print "remove_object_from_cell(): TRIED TO REMOVE NON EXISTENT OBJECT"
            print "thing={}, cell={}".format(thing, get_cell_contents(x, y))

    def display_cell_counts(self):
        for y in range(self.ydim):
            print [len(self.get_cell_contents(x, y)) for x in range(self.xdim)]

    # TODO Figure out how to do this correctly.  Trying
    # to apply an arbitrary functionto the whole data set
    def display_map(self, display_types=None):
        plt.imshow(grid)
        plt.show()


class AgentEnvironmentInterface(object):
    """
    An interface for an agent and an environment.
    The interface takes commands from the agent and
    returns the environments response.
    """
    def __init__(self, environment):
        pass


def build_environment(dimensions, dirt_cnt, vacuum_cnt):
    env = VacuumEnvironment()
    env.set_dimensions(*dimensions)
    Dirt.dump_rand_dirt(env, dirt_cnt)
    return env

if __name__ == "__main__":
    dims = (10, 10)
    test = build_environment(dims, 15, 1)
    test.display_cell_counts()

    # for x in [ele for row in test.array for ele in row]:
    #     x.set_state(get_rand_weighted_val([(0, 0.8), (1, 0.2)]))

    # test.display_map(MapCell.get_state)
