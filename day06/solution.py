#!/usr/bin python3

import math as m, re, os

def race_distance(hold: int, total_time: int):
  if hold == 0: return 0
  if hold == total_time: return 0
  
  travel_time = total_time - hold
  total_distance = hold * travel_time
  return total_distance

races = ([61, 430], [67, 1036], [75, 1307], [71, 1150])

ways_to_win_totals = []
for race in races:
  ways_to_win = 0
  for h in range(race[0]):
    print("hold:", h)
    print("distance:", race_distance(h, race[0]))
    distance = race_distance(h, race[0])
    if distance > race[1]:
      ways_to_win += 1
  print("Ways to win race", ways_to_win)
  ways_to_win_totals.append(ways_to_win)
  
print("Margin of error:", m.prod(ways_to_win_totals))
