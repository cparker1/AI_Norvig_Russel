__author__ = "Charles A. Parker"

from VacuumEnvironment import Thing

XDIR = 0
YDIR = 1
POSI = 1
NEGI = 0

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

    def __init__(self, env_interface):
        self._direction_axis = 0
        self._direction_positivity = 0
        self._bumper = 0
        self._power = 5000
        self.power_threshold = 200
        self.rand_turn = [(self.turn_left, 1),
                          (self.turn_right, 1)]
        self.rand_motion = [(self.turn_left, 1),
                            (self.turn_right, 1),
                            (self.move_forward, 1)]

        self.interface = env_interface
        pass

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def bumper(self):
        return self._bumper

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
