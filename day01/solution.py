#!/usr/local/bin python3

import os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

def getInt(line):
  intArr = []
  for l in line:
    if str.isnumeric(l):
      intArr.append(int(l))
  print(intArr, file=f_output)
  firstDig = intArr[0]
  lastDig = intArr[len(intArr) - 1]
  print("FIRST:", firstDig, file=f_output)
  print("LAST:", lastDig, file=f_output)
  concatNum = str(firstDig) + str(lastDig)
  print("line digit:", concatNum, file=f_output)
  return int(concatNum)

def main():
  total = 0
  for line in f_input:
    lineNum = getInt(line)
    total += lineNum
  print("TOTAL:", total, file=f_output)

main()
