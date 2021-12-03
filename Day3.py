import time
from collections import Counter


def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day1_input.txt
    :return floor_depth: list of depths recorded on submarine
    """
    diag_report = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            diag_report.append(line)

    diag_report_zip = zip(*diag_report)
    return diag_report_zip, diag_report


def most_least_common(report, oxg=False):
    most_common_bin = []
    least_common_bin = []
    for l in report:
        sum_l = sum([int(i) for i in l if type(i)== int or i.isdigit()])
        if sum_l/len(l) > 0.5:
            most_common_bin.append('1')
            least_common_bin.append('0')
        elif sum_l/len(l) < 0.5:
            most_common_bin.append('0')
            least_common_bin.append('1')
        else:
            most_common_bin.append('1')
            least_common_bin.append('0')

    most_common = ''.join(most_common_bin)
    least_common = ''.join(least_common_bin)

    return most_common, least_common


def oxygen_gen_rating(report):
    index = 0
    while len(report) > 1:
        most_c, unused = most_least_common(zip(*report))
        report = rating(report, most_c, index)
        index += 1
    return report[0]


def co2_scrub_rating(report):
    index = 0
    while len(report) > 1:
        unused, least_c = most_least_common(zip(*report))
        report = rating(report, least_c, index)
        index += 1

    return report[0]


def rating(report, keep_numbers, index):
    new_report = []
    for line in report:
        if line[index] == keep_numbers[index]:
            new_report.append(line)
    return new_report


def main(file):
    report_zip, report = parse(file)
    most_c_bin, least_c_bin = most_least_common(report_zip)
    oxyg_rating = oxygen_gen_rating(report)
    co2_rating = co2_scrub_rating(report)

    return most_c_bin, least_c_bin, oxyg_rating, co2_rating


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day3_input.txt'

    most_c, least_c, oxyg_rating, co2_rating = main(file_loc)

    print(oxyg_rating)
    print(co2_rating)

    print(f'The most common bit in decimal form:{int(most_c, 2)}')
    print(f'The least common bit in decimal form:{int(least_c, 2)}')
    print(f'The power consumption of the submarine is: {int(most_c, 2) * int(least_c, 2)}')

    print(f'The oxygen rating in decimal form:{int(oxyg_rating, 2)}')
    print(f'The co2 rating in decimal form:{int(co2_rating, 2)}')
    print(f'The life support rating of the submarine is: {int(oxyg_rating, 2) * int(co2_rating, 2)}')
