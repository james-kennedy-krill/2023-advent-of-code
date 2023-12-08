#!/usr/bin python3

import math as m, re, os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output2.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

board = list(f_input)
cards = len(board)
card_copies = []
for card in range(cards):
  card_copies.append(1)

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
    for y in range(card_copies[r]):
      for x in range(num_of_winners):
        card_copies[r+1+x] += 1
    print("\tWINNERS, NO DUPLICATES:", winners_no_duplicates, file=f_output)
    print("\tWINNERS:", num_of_winners, file=f_output)
    
print("CARD COPIES", card_copies, file=f_output)
print("TOTAL CARDS:", sum(card_copies), file=f_output)
    
