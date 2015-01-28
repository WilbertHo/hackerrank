import fileinput


def map_cavities(grid):
    def is_cavity(row, col):
        depth = grid[row][col]
        if grid[row - 1][col] < depth and \
           grid[row + 1][col] < depth and \
           grid[row][col - 1] < depth and \
           grid[row][col + 1] < depth:
            return True
        return False

    cavity_map = grid

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if is_cavity(row, col):
                cavity_map[row] = cavity_map[row][:col] + 'X' + cavity_map[row][col + 1:]

    return cavity_map


def main():
    # get input grid, discard first line, which is number of lines
    input = [line.strip() for line in fileinput.input()][1:]

    cavities = map_cavities(input)
    for row in cavities:
        print row


if __name__ == '__main__':
    main()
