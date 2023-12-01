from lib.helpers import log, get_all_strings_by_lines
import re

def part_1():
    input_arr = get_all_strings_by_lines('1.txt')
    log(input_arr)

    cur_prod = 0
    for val in input_arr:
        digits = re.findall(r'\d', val)
        d = (int(digits[0]) * 10) + (int(digits[-1]))
        cur_prod += d

    return cur_prod


def part_2():
    input_arr = get_all_strings_by_lines('1.txt')
    log(input_arr)

    cur_prod = 0
    for val in input_arr:
        numbered = re.sub(r'one', 'one1one', val, flags=re.S)
        numbered = re.sub(r'two', 'two2two', numbered, flags=re.S)
        numbered = re.sub(r'three', 'three3three', numbered, flags=re.S)
        numbered = re.sub(r'four', 'four4four', numbered, flags=re.S)
        numbered = re.sub(r'five', 'five5five', numbered, flags=re.S)
        numbered = re.sub(r'six', 'six6six', numbered, flags=re.S)
        numbered = re.sub(r'seven', 'seven7seven', numbered, flags=re.S)
        numbered = re.sub(r'eight', 'eight8eight', numbered, flags=re.S)
        numbered = re.sub(r'nine', 'nine9nine', numbered, flags=re.S)
        digits = re.findall(r'\d', numbered)
        log(digits)
        d = (int(digits[0]) * 10) + (int(digits[-1]))
        cur_prod += d

    return cur_prod