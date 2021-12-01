import time


def parse(file_loc):
    '''
    read input to list

    :param file_loc: file path to AOC Day1_input.txt
    :return list_containers: list of container sizes
    '''
    floor_depth = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            value = int(line)
            floor_depth.append(value)
    return floor_depth


def depth_increase(floor_depth):
    count = 0
    for i in range(1,len(floor_depth)):
        if floor_depth[i] > floor_depth[i-1]:
            count = count + 1
    print(f'The depth increases {count} times')

    return None


def main(file):
    floor_depth = parse(file)
    depth_increase(floor_depth)



if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day1_input.txt'

    main(file_loc)