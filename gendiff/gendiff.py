#!/usr/bin/env python

from gendiff.parsing import read_file, get_format
from gendiff.parsing import parse
from gendiff.data_comparer import compare_data
from gendiff.formaters.formatter import format_diff
from gendiff.formaters.formats import STYLISH


def generate_diff(filepath1, filepath2, formatter=STYLISH):
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(read_file(filepath1), format1)
    data2 = parse(read_file(filepath2), format2)
    diff = compare_data(data1, data2)
    return format_diff(diff, formatter)
