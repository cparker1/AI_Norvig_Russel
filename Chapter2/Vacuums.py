
__author__ = "Charles A. Parker"


class Vacuum(object):
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
        _direction = 0
        _bumper = 0
        _power = 5000
        pass

    @property
    def power(self):
        return self._power

    @property
    def direction(self):
        return self._direction

    @property
    def bumper(self):
        return self._bumper

    #ACTIONS
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

    #PERCEPTS
    def check_bumper(self):
        pass

    def check_for_dirt(self):
        pass

    def check_if_home(self):
        pass

    #DECISIONS!!!!
    def make_decision(self):
        pass


