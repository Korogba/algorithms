# implementation by @kaba_y, https://korogba.github.io
from math import log

from utils.file_operations import convert_file_to_two_sat


def papadimitriou(file_path):
    clauses, variables = convert_file_to_two_sat(file_path)
    random_trials = log(len(clauses), 10)
    pass