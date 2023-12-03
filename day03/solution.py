#!/usr/local/bin python3

import os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

# TDD
# We'll need to build an iterator
# Which goes line by line
# and has knowledge of before and after lines (so need current index and reference to lines by index?)
# and checks for numbers (regex) 
# and then gets their start/end index in the line of characters
# and checks against the following locations to see if symbols (except periods) exist:
#   1. before and after the number on the same line
#   2. on the line above (before), if it exists, starting one less than the start index, and going to one more than the end index
#   3. on the line below (after), if it exists, starting on less than the start index and going to one more than the end index
# if any of these conditions are true, we use this number as part of the sum of the output

def main():
  print("--- DAY 3: Gear Ratios ---", file=f_output)

main()