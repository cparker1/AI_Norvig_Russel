import matplotlib.pyplot as plt
import numpy as np
__author__ = "Charles A. Parker"

# TODO use logging module
# TODO figure out wtf i'm doing


def get_rand_weighted_val(values, probabilities):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(np.random.random_sample(1), bins)]


# TODO do I really need this class?...
class MapCell(object):
    """
    MapCell is a single element of a map.  It is intended to be
    built up into a larger map.
    """
    def __init__(self):
        self.state = 0
        pass

    def set_state(self, value):
        if value in [0, 1]:
            self.state = value

    def get_state(self):
        return self.state

    def toggle_state(self):
        self.state = int(not self.state)
        return self.state


class MapRect(object):
    """
    MapRect is an object intended to create a map for other
    objects to interact with it.  It only contains a grid
    where each cell has properties.

    Expects a class to be passed in during initialization, which will
    specify the class of data that the map represents.
    """

    def __init__(self, cell_contents, cell_content_args=None):
        self.cell_content_args = cell_content_args if cell_content_args else tuple()
        self.array = []
        self.col_len = 0
        self.row_len = 0
        self.cell_type = cell_contents
        pass

    def set_dimensions(self, col_len, row_len):
        self.x_dim = col_len
        self.row_len = row_len
        # TODO Try to make the map more general in terms of what the cells can be
        self.array = [[self.cell_type(*self.cell_content_args) for x in range(col_len)]
                      for y in range(row_len)]
        pass

    def get_dimensions(self):
        return [self.col_len, self.row_len]

    def get_element(self, row, col):
        try:
            return self.array[row][col]
        except:
            return None

    def apply_function_to_map(self, map_function):
        if map_function is not None:
            self.array = [map(map_function, row) for row in self.array]

    # TODO Probably a more concise way to do this, too
    def get_next_neighbor(self, cur_row, cur_col, direction):
        return_row = cur_row
        return_col = cur_col
        if direction == "UP":
            return_row -= 1
        elif direction == "LEFT":
            return_col -= 1
        elif direction == "DOWN":
            return_row += 1
        elif direction == "RIGHT":
            return_col += 1

        if return_col == self.col_len:
            return_col -= 1
        if return_col == -1:
            return_col += 1
        if return_row == self.row_len:
            return_row -= 1
        if return_row == -1:
            return_row += 1

        return [return_row, return_col]

    # TODO Figure out how to do this correctly.  Trying
    # to apply an arbitrary functionto the whole data set
    def display_map(self, map_function=None):
        grid = [map(map_function, row) for row in self.array]
        plt.imshow(grid)
        plt.show()


if __name__ == "__main__":
    test = MapRect(MapCell)
    test.set_dimensions(100, 100)
    for x in [ele for row in test.array for ele in row]:
        x.set_state(get_rand_weighted_val([0, 1], [0.95, 0.05]))

    test.display_map(MapCell.get_state)
