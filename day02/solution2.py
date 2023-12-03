#!/usr/local/bin python3

import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output2.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")
  
# Regular Expressions
id_re = re.compile('^Game (\d+)')
red_re = re.compile('(\d+)\sred')
green_re = re.compile('(\d+)\sgreen')
blue_re = re.compile('(\d+)\sblue')

def getId(line: str) -> int:
  id_m = id_re.match(line)
  print("ID: ", id_m.group(1), file=f_output)
  return int(id_m.group(1))

def getRed(line: str) -> int:
  red_m = red_re.findall(line)
  print("RED: ", red_m, file=f_output)
  largest_red = max(map(int, red_m))
  print("LARGEST RED: ", largest_red, file=f_output)
  return largest_red
  
def getGreen(line: str) -> int:
  green_m = green_re.findall(line)
  print("GREEN: ", green_m, file=f_output)
  largest_green = max(map(int, green_m))
  print("LARGEST GREEN: ", largest_green, file=f_output)
  return largest_green
  
def getBlue(line: str) -> int:
  blue_m = blue_re.findall(line)
  print("BLUE: ", blue_m, file=f_output)
  largest_blue = max(map(int, blue_m))
  print("LARGEST BLUE: ", largest_blue, file=f_output)
  return largest_blue

def main():
  total = 0
  for line in f_input:
    line_value = getId(line)
    largest_red = getRed(line)
    largest_green = getGreen(line)
    largest_blue = getBlue(line)
    color_power = largest_red * largest_green * largest_blue
    print("COLORS POWER: ", color_power, file=f_output)
    total += color_power
    print("LINE: ", line.strip(), file=f_output)
    print("-----------------------------------------------------", file=f_output)
  print("SUM OF POWER SETS:", total, file=f_output)
    
main()
