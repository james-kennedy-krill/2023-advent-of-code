#!/usr/local/bin python3

import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output2.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")
lines = f_input.readlines()

# TDD
# We need to find numbers that share adjacent star symbols
# It may be more effecient to search for star symbols,
# and then look for adjacent numbers
# if exactly 2 matches are found for numbers in adjacent positions, 
# capture, multiply, and add those "gear ratios" together

stars_re = re.compile("\*")
number_re = re.compile("(\D(\d+)\D)|(\D(\d+)$)|(^(\d+)\D)")
symbol_re = re.compile("[^\w\d\s.]")

def getStars(line: str):
  stars = stars_re.findall(line)
  return stars

def getPreviousChar(line_index, char_index):
  if char_index > 0:
    return lines[line_index][char_index-1]
  
def getNextChar(line_index, char_index):
  if char_index < len(lines[line_index]) - 1:
    return lines[line_index][char_index+1]

def getNumbersBeforeNumber(line_index, char_index):
  numbersBefore = ""
  if char_index > 0:
    lookingForNumbers = True
    i = 0
    while lookingForNumbers:
      prev_char = getPreviousChar(line_index, char_index - i)
      if re.match("\d", prev_char):
        numbersBefore = prev_char + numbersBefore
        i += 1
      else:
        lookingForNumbers = False
  return numbersBefore

def getNumbersAfterNumber(line_index, char_index):
  numbersAfter = ""
  if char_index < len(lines[line_index]) - 1:
    lookingForNumbers = True
    i = 0
    while lookingForNumbers:
      next_char = getNextChar(line_index, char_index + i)
      if re.match("\d", next_char):
        numbersAfter = numbersAfter + next_char
        i += 1
      else:
        lookingForNumbers = False
  return numbersAfter

def getNumberFromIndex(line_index, char_index):
  number = getNumbersBeforeNumber(line_index, char_index) + lines[line_index][char_index] + getNumbersAfterNumber(line_index, char_index)
  return int(number)

def getAdjacentGearRatio(star_data):
  print("---- STAR DATA:", star_data, file=f_output)
  line_index = star_data["line_index"]
  char_index = star_data["star_index"]
  gear_ratio = 0
  numbers = []
  
  # Check the character directly to the left
  if char_index > 0:
    char_left = lines[line_index][char_index-1]
    if re.match("\d", char_left):
      print("LEFT IS NUMBER", file=f_output)
      numbers.append(getNumberFromIndex(line_index, char_index-1))
  
  # Check the character directly to the right
  if char_index < len(lines[line_index])-1:
    char_right = lines[line_index][char_index+1]
    if re.match("\d", char_right):
      print("RIGHT IS A NUMBER", file=f_output)
      numbers.append(getNumberFromIndex(line_index, char_index+1))
  
  # Check the characters above
  if line_index > 0:
    char_above = lines[line_index-1][char_index]
    char_above_left = lines[line_index-1][char_index-1]
    char_above_right = lines[line_index-1][char_index+1]
    print("CHAR ABOVE", char_above, file=f_output)
    if re.match("\d", char_above):
      print("ABOVE IS NUMBER", file=f_output)
      numbers.append(getNumberFromIndex(line_index-1, char_index))
    else:
      # If there is no number directly above, we want to check both up/left and up/right
      if re.match("\d", char_above_left):
        print("ABOVE/LEFT IS NUMBER", file=f_output)
        numbers.append(getNumberFromIndex(line_index-1, char_index-1))
      if re.match("\d", char_above_right):
        print("ABOVE/RIGHT IS NUMBER", file=f_output)
        numbers.append(getNumberFromIndex(line_index-1, char_index+1))
      
      
  # Check the characters below
  if (line_index < len(lines)-1):
    char_below = lines[line_index+1][char_index]
    char_below_left = lines[line_index+1][char_index-1]
    char_below_right = lines[line_index+1][char_index+1]
    print("CHAR BELOW", char_below, file=f_output)
    if re.match("\d", char_below):
      print("BELOW IS NUMBER", file=f_output)
      numbers.append(getNumberFromIndex(line_index+1, char_index))
    else:
      # If there is no number directly below, check left and right below
      if re.match("\d", char_below_left):
        print("BELOW/LEFT IS NUMBER", file=f_output)
        numbers.append(getNumberFromIndex(line_index+1, char_index-1))
      if re.match("\d", char_below_right):
        print("BELOW/RIGHT IS NUMBER", file=f_output)
        numbers.append(getNumberFromIndex(line_index+1, char_index+1))
      
  # Check if we have exactly two numbers
  print("NUMBERS:", numbers, file=f_output)
  if len(numbers) == 2:
    gear_ratio = numbers[0]*numbers[1]
    print("HAS EXACTLY TWO NUMBERS", gear_ratio, file=f_output)
    return gear_ratio
  else:
    print("HAS NOT EXACTLY TWO NUMBERS", numbers)
  return 0
  

star_map = []

def main():
  print("--- DAY 3: Part 2 ---", file=f_output)
  total = 0
  for line_index, line in enumerate(lines):
    print("LINE", line_index + 1, file=f_output)
    if line_index > 0:
      print(lines[line_index - 1].strip(), file=f_output)
    print(line.strip(), file=f_output)
    if line_index < len(lines) - 1:
      print(lines[line_index+1].strip(), file=f_output)
    for star_index, char in enumerate(line):
      if char == "*":
        # print("STAR FOUND:",  file=f_output)
        # print("Line Index:", line_index, "Star Index:", star_index, file=f_output)
        star_map.append({ "line_index": line_index, "star_index": star_index })
    for star_data in star_map:
      total += getAdjacentGearRatio(star_data)
    # stars = getStars(line.strip())
    # for star in stars:
    #   print("STAR DATA:", star, file=f_output)
    # for number in line_numbers:
    #   number_data = lineNumberPositioning(line.strip(), number)
    #   # print("NUMBER DATA:", number_data, file=f_output)
    #   if hasAdjacentSymbol(line.strip(), index, number_data):
    #     print("HAS ADJACENT: ", number_data["number"], file=f_output)
    #     total += number_data["number"]
    # print("LINE NUMBERS: ", line_numbers, file=f_output)
  print("TOTAL:", total, file=f_output)

main()
