import time


def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day1_input.txt
    :return floor_depth: list of depths recorded on submarine
    """
    floor_depth = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            value = int(line)
            floor_depth.append(value)
    return floor_depth


def depth_increase(floor_depth):
    """
    checks if the depth has increased and counts how many times it does so
    :param floor_depth: a list of depths recorded
    :return: count: int representing how many times the depth increased
    """

    depth_count = 0
    for i in range(1, len(floor_depth)):
        if floor_depth[i] > floor_depth[i - 1]:
            depth_count = depth_count + 1

    return depth_count


def main(file):
    floor_depth = parse(file)
    depth_count = depth_increase(floor_depth)

    return depth_count


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day1_input.txt'

    depth_increase_count = main(file_loc)
    print(f'The depth increases {depth_increase_count} times')

    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')
