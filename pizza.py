import sys


class Pizza(object):
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            params = [int(i) for i in f.readline().split()]
            self.rows, self.cols, self.min, self.max = params
            self.pizza = [list(f.readline().strip()) for i in range(self.rows)]

    def find_candidates(self, start, end):
        row1, col1 = start
        row2, col2 = end
        slices = []
        for row in range(row1, row2):
            for col in range(col1, col2):
                slice_end = (row + 1, col + 1)
                if(self.validate_slice(start, slice_end)):
                    slices.append({
                        'cells': self.list_cells(start, (row, col,)),
                        'start': (row1, col1),
                        'end': (row, col)
                    })
        return slices

    def validate_slice(self, start, end):
        row1, col1 = start
        row2, col2 = end
        size = (row2 - row1) * (col2 - col1)
        if not self.min * 2 <= size <= self.max:
            return False
        tomatoes, mushrooms = 0, 0
        for row in range(row1, row2):
            for col in range(col1, col2):
                if self.pizza[row][col] == 'T':
                    tomatoes += 1
                else:
                    mushrooms += 1
                if mushrooms >= self.min and tomatoes >= self.min:
                    return True
        return False

    def list_cells(self, start, end):
        row1, col1 = start
        row2, col2 = end
        cells = []
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                cells.append((row, col,))
        return cells


example = Pizza('example.in')
for i in example.find_candidates((2, 0,), (example.rows, example.cols,)):
    print i
