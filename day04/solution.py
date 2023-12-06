#!/usr/bin python3

import math as m, re, os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

board = list(f_input)
points = 0

for r, row in enumerate(board):
  print("CARD", r+1, file=f_output)
  w_n = re.search(r'(?<=: ).+(?= \|)', row)
  n = re.search(r'(?<= \|).+$', row)
  w_n_sorted = sorted(list(map(int, filter(lambda num: num != '', re.split(r"\s+", w_n.group())))))
  print("\tW:", w_n_sorted, file=f_output)
  n_sorted = sorted(list(map(int, filter(lambda num: num != '', re.split(r"\s+", n.group())))))
  print("\tN:", n_sorted, file=f_output)
  winners = list(filter(lambda num: num in n_sorted, w_n_sorted))
  winners_no_duplicates = list(set(winners))
  num_of_winners = len(winners_no_duplicates)
  if num_of_winners == 0:
    print("\tNO WINNERS", file=f_output)
  else:
    print("\tWINNERS, NO DUPLICATES:", winners_no_duplicates, file=f_output)
  if num_of_winners == 1:
    points += 1
    print("\tPOINTS:", 1, file=f_output)
  elif num_of_winners == 2:
    points += 2
    print("\tPOINTS:", 2, file=f_output)
  elif num_of_winners > 1:
    points += m.pow(2, num_of_winners-1)
    print("\tPOINTS:", int(m.pow(2, num_of_winners-1)), file=f_output)
    
print(int(points), file=f_output)
    
