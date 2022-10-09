def gridmatrix(grid_size, grid_value):
    return [grid_value[i:i + grid_size] for i in range(0, len(grid_value), grid_size)]