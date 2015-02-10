import matplotlib.pyplot as plt
import numpy as np
from random import randint
import itertools
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


class Thing(object):
    """
    Base class for a thing that is on a map.
    """
    def __init__(self):
        self.pos = None


class Dirt(Thing):
    @staticmethod
    def dump_dirt(environment, positions):
        for pos in positions:
            environment.create_object(pos, Dirt())
        pass

    @staticmethod
    def dump_rand_dirt(environment, count):
        positions = [environment.get_random_cell() for n in range(count)]
        Dirt.dump_dirt(environment, positions)

class Furniture(Thing):
    pass


class Wall(Thing):
    pass


class VacuumHome(Thing):
    pass


class ThingList(dict):
    """
    A Class that a Vacuum environment uses to track the 
    locations and types of objects that the environment
    houses
    """
    def __init__(self):
        self._id_cntr = itertools.count()

    @property
    def id_cntr(self):
        return self._id_cntr.next()

    def new_object(self, coords, thing):
        thing.pos = coords
        self.update({self.id_cntr: thing})

    def get_objects_at_location(self, coords):
        return [thing for thing in self.values() if thing.pos == coords]
        pass

    def print_list(self):
        for key, value in self.items():
            print key, value, value.pos


class Vacuum(Thing):
    """
    A simple vacuum object.

    It has five basic commands:
    Move forward
    Turn left
    Turn right
    Clean curent position

    It has three percepts:
    Bump - Unable to move in the direction attempted
    See dirt - Found dirt underneath the vacuum
    Sense home - Is the vacuum in the home square
    """

    def __init__(self):
        Thing.__init__(self)
        self._direction_axis = 0
        self._direction_positivity = 1
        self._bumper = 0
        self._power = 5000
        self.power_threshold = 200
        self.rand_turn = [(self.turn_left, 1),
                          (self.turn_right, 1)]
        self.rand_motion = [(self.turn_left, 1),
                            (self.turn_right, 1),
                            (self.move_forward, 1)]
        self.env = None

    # ACTIONS
    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def move_forward(self):
        pass

    def clean_square(self):
        pass

    def power_off(self):
        pass

    # ACTION WRAPPERS
    def rand_move(self, cmds):
        get_rand_weighted_val(cmds)()

    # PERCEPTS
    def check_bumper(self):
        pass

    def check_for_dirt(self):
        pass

    def check_if_home(self):
        pass

    # DECISIONS!!!!
    def make_decision(self):
        if self.check_bumper():
            self.rand_motion(self.rand_turn)
            return None
        if self.check_for_dirt():
            self.clean_square()
            return None
        if check_if_home():
            if self.power < self.power_threshold:
                self.power_off()
                return None
        self.rand_move(self.rand_motion)
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

    def __init__(self, dims):
        self.dims = dims
        self._obj_list = ThingList()
        pass

    def get_random_cell(self):
        return_coord = []
        f = lambda x: randint(0, x - 1)
        for dim in self.dims:
            return_coord += [f(dim)]
        return(tuple(return_coord))

    def get_cell_contents(self, coords):
        return self._obj_list.get_objects_at_location(coords)

    def check_for_object_in_cell(self, coords, thing):
        return any(isinstance(item, thing) for item in self.get_cell_contents(coords))

    def move_object_from_cell_to_cell(self, src_coords, targ_coords, thing):
        pass

    def create_object(self, coords, thing):
        if coords is None:
            coords = self.get_random_cell()
        self._obj_list.new_object(coords, thing)
        if hasattr(thing, 'env'):
            print thing
            thing.env = self
        pass

    def delete_object(self, thing):
        pass

    def display_cell_counts(self):
        self._obj_list.print_list()
        for y in range(self.dims[0]):
            print [len(self.get_cell_contents((x, y, 0))) for x in range(self.dims[1])]


    def display_map(self, display_types=None):
        plt.imshow(grid)
        plt.show()

    def process_turn():
        pass


def build_environment(dimensions, dirt_cnt, vacuum_cnt):
    env = VacuumEnvironment(dimensions)
    Dirt.dump_rand_dirt(env, dirt_cnt)
    env.create_object(None, Vacuum())
    return env

if __name__ == "__main__":
    dims = (7, 4,3)
    test = build_environment(dims, 5, 1)
    test.display_cell_counts()
