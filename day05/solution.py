#!/usr/bin python3

import math as m, re, os

script_dir = os.path.dirname(os.path.realpath(__file__))
# input_file_path = os.path.join(script_dir, "input.txt")
input_file_path = os.path.join(script_dir, "input_example.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

board = list(f_input)
