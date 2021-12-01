import time
import numpy as np


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


def depth_increase(sliding_depths):
    """
    checks if the depth has increased and counts how many times it does so
    :param sliding_depths: a list of the summed sliding depths
    :return: count - int representing how many times the depth increased
    """

    depth_count = 0
    for i in range(1, len(sliding_depths)):
        if sliding_depths[i] > sliding_depths[i - 1]:
            depth_count = depth_count + 1

    return depth_count


def sliding_window(floor_depth):
    """
    Computes the floor depth for the sliding window using convolve
    :param floor_depth: list of all the recorded depths
    :return: sliding_depths - list of the summed sliding depths
    """
    sliding_depths = np.convolve(floor_depth, np.ones(3, dtype=int), 'valid')

    return sliding_depths


def main(file):
    floor_depth = parse(file)
    sliding_depth = sliding_window(floor_depth)
    increase_count = depth_increase(sliding_depth)

    return increase_count


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day1_input.txt'

    depth_increase_count = main(file_loc)
    print(f'The depth increases {depth_increase_count} times')

    end_time = time.time()
    print(f'Time taken:{end_time - start_time}')
