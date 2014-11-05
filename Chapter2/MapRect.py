# import matplotlib.pyplot as plt
# import numpy as np
__author__ =   "Charles A. Parker"

# TODO use logging module
# TODO figure out wtf i'm doing


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
        if value in [0,1]:
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
    """

    def __init__(self, cell_contents):
        self.array = []
        self.col_len = 0
        self.row_len = 0
        self.cell_type = cell_contents
        pass

    def set_dimensions(self, col_len, row_len):
        self.x_dim = col_len
        self.row_len = row_len
        self.array = [[self.cell_type() for x in range(col_len)] for y in range(row_len)]
        pass

    def get_dimensions(self):
        return [self.col_len, self.row_len]

    def get_element(self, row, col):
        try:
            return self.array[row][col]
        except:
            return None

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
    def print_map(self, map_function = None):
        for row in self.array:
            if map_function is None:
                print row
            else:
                print map(map_function, row)



if __name__ == "__main__":
    test = MapRect(MapCell)
    test.set_dimensions(10,5)
    test.get_element(0, 0).toggle_state()

    test.print_map(MapCell.get_state)

    print "\n{}".format(test.get_next_neighbor(4,4,"DOWN"))

# EXAMPLE PLOTTING STUFF
#     methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
#                      'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
#                      'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

#     grid = np.random.rand(4, 4)

#     fig, axes = plt.subplots(3, 6, figsize=(12, 6),
#                                                      subplot_kw={'xticks': [], 'yticks': []})

#     fig.subplots_adjust(hspace=0.3, wspace=0.05)

#     for ax, interp_method in zip(axes.flat, methods):
#             ax.imshow(grid, interpolation=interp_method)
#             ax.set_title(interp_method)

#     plt.show()