#!/usr/local/bin python3

import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")
lines = f_input.readlines()

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

numbers_re = re.compile("([\d]+)")
symbol_re = re.compile("[^\w\d\s.]")

def getLineNumbers(line: str):
  line_numbers = numbers_re.findall(line)
  return line_numbers

def lineNumberPositioning(line, line_number):
  number_re = re.compile("\D?" + line_number + "\D?")
  number_match = number_re.search(line)
  # print(number_match, file=f_output)
  if number_match:
    start_index = number_match.start()
    end_index = number_match.end()
    number_data = { "number": int(line_number), "start_index": start_index, "end_index": end_index}
    return number_data
  
def isSymbol(text):
  match = symbol_re.search(text)
  return match
  
def hasAdjacentSymbol(line, line_index, number_data):
  # Check this line
  print("NUM:", number_data["number"], file=f_output)
  print(line[number_data["start_index"]:number_data["end_index"]], file=f_output)
  
  # To the left
  if isSymbol(line[number_data["start_index"]]):
    print("symbol before:", line[number_data["start_index"]], file=f_output)
    return True
  
  # To the right
  line_length = len(line)
  if number_data["end_index"] < line_length:
    if isSymbol(line[number_data["end_index"]-1]):
      print("symbol after:", line[number_data["end_index"]-1], file=f_output)
      return True
    
  # Check line before if it exists
  if line_index > 0:
    prev_line = lines[line_index-1]
    if isSymbol(prev_line[number_data["start_index"]:number_data["end_index"]]):
      print("NUM:", number_data["number"], file=f_output)
      print("symbol, line before:", prev_line[number_data["start_index"]:number_data["end_index"]], file=f_output)
      return True
  
  # Check line after if it exists
  lines_len = len(lines)
  if line_index < lines_len-1:
    next_line = lines[line_index+1]
    if isSymbol(next_line[(number_data["start_index"]):(number_data["end_index"])]):
      print("NUM:", number_data["number"], file=f_output)
      print("symbol, line after:", next_line[(number_data["start_index"]):(number_data["end_index"])], file=f_output)
      return True
    
  return False

def main():
  print("--- DAY 3: Gear Ratios ---", file=f_output)
  total = 0
  for index, line in enumerate(lines):
    print("LINE", index + 1, file=f_output)
    if index > 0:
      print(lines[index - 1].strip(), file=f_output)
    print(line.strip(), file=f_output)
    if index < len(lines) - 1:
      print(lines[index+1].strip(), file=f_output)
    line_numbers = getLineNumbers(line.strip())
    for number in line_numbers:
      number_data = lineNumberPositioning(line.strip(), number)
      # print("NUMBER DATA:", number_data, file=f_output)
      if hasAdjacentSymbol(line.strip(), index, number_data):
        print("HAS ADJACENT: ", number_data["number"], file=f_output)
        total += number_data["number"]
    print("LINE NUMBERS: ", line_numbers, file=f_output)
  print("TOTAL:", total, file=f_output)

main()
