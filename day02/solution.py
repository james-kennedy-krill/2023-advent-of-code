#!/usr/local/bin python3

import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

# Totals in the bag
red_cubes = 12
green_cubes = 13
blue_cubes = 14
  
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
  # total_red = sum(map(int, red_m))
  # print("TOTAL RED:", total_red, file=f_output)
  # return total_red
  largest_red = max(map(int, red_m))
  return largest_red
  
def getGreen(line: str) -> int:
  green_m = green_re.findall(line)
  print("GREEN: ", green_m, file=f_output)
  # total_green = sum(map(int, green_m))
  # print("TOTAL GREEN:", total_green, file=f_output)
  # return total_green
  largest_green = max(map(int, green_m))
  return largest_green
  
def getBlue(line: str) -> int:
  blue_m = blue_re.findall(line)
  print("BLUE: ", blue_m, file=f_output)
  # total_blue = sum(map(int, blue_m))
  # print("TOTAL BLUE:", total_blue, file=f_output)
  # return total_blue
  largest_blue = max(map(int, blue_m))
  return largest_blue
  
def isGamePossible(red: int, green: int, blue: int) -> bool:
   if ((red <= red_cubes) & (green <= green_cubes) & (blue <= blue_cubes)):
     print("game is possible", red, green, blue)
     return True
   else:
     print("NOT possible", red, green, blue)
     return False

def main():
  total = 0
  for line in f_input:
    line_value = getId(line)
    red = getRed(line)
    green = getGreen(line)
    blue = getBlue(line)
    print(line_value, "RED: ", red, red <= red_cubes)
    print(line_value, "GREEN: ", green, green <= green_cubes)
    print(line_value, "BLUE: ", blue, blue <= blue_cubes)
    if (isGamePossible(red, green, blue)):
      print("GAME IS POSSIBLE!", file=f_output)
      total += line_value
    else:
      print("NOT POSSIBLE!", file=f_output)
    print("LINE: ", line.strip(), file=f_output)
    print("-----------------------------------------------------", file=f_output)
  print("TOTAL VALID GAMES SUM:", total, file=f_output)
    
main()
