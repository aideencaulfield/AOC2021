import sys
import time


def parse(file_loc):
    """
    read input to list
    :param file_loc: file path to AOC Day1_input.txt
    :return floor_depth: list of depths recorded on submarine
    """

    bingo_input = open(file_loc, "r").read().strip('\n\n').split()
    bingo_numbers = bingo_input[0].split(',')
    bingo_cards = separate_cards(bingo_input[1:])

    return bingo_numbers, bingo_cards


def separate_cards(card_numbers):
    """
    Each card has a total of 25 numbers, this function separates all of the numbers into their cards
    :param card_numbers:
    :return:
    """
    cards = []
    for i in range(0, len(card_numbers), 25):
        cards.append(card_numbers[i:i + 25])

    return cards


def mark_cards(bingo_numbers, bingo_cards, part_number):
    for i in bingo_numbers:
        for card in bingo_cards:
            for iterate, c in enumerate(card):
                if int(i) == int(c):
                    card[iterate] = 1000
                    check_cards(card, i, part_number)
    return None


def check_cards(card, last_called_number, part_number):
    check_rows(card, last_called_number, part_number)
    check_columns(card, last_called_number, part_number)

    return None


def check_rows(card, last_called_number, part_number):
    for i in range(0, len(card), 5):
        row_numbers = card[i:i+5]
        if all(x == 1000 for x in row_numbers):
            if part_number == 1:
                bingo(card, last_called_number)
    return None


def check_columns(card, last_called_number, part_number):
    for i in range(0,5):
        col_numbers = card[i::5]
        if all(x == 1000 for x in col_numbers):
            if part_number == 1:
                bingo(card, last_called_number)

    return None


def bingo(card, last_called_number):
    print('Bingo!!')
    for i in range(0, len(card), 5):
        unmarked_sum = 0
        for unmarked in card:
            if unmarked != 1000:
                unmarked_sum += int(unmarked)

        print(f'Score of winning card = {int(unmarked_sum) * int(last_called_number)}')
        sys.exit()


def main(file):
    numbers, cards = parse(file)
    mark_cards(numbers, cards, part_number)


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day4_sample.txt'
    main(file_loc)
