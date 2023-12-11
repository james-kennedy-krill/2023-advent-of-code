#!/usr/bin python3

import math as m, re, os

def race_distance(hold: int, total_time: int):
  if hold == 0: return 0
  if hold == total_time: return 0
  
  travel_time = total_time - hold
  total_distance = hold * travel_time
  return total_distance

race = [61677571, 430103613071150]

ways_to_win = 0
for h in range(race[0]):
  distance = race_distance(h, race[0])
  if distance > race[1]:
    ways_to_win += 1
  
print("Margin of error:", ways_to_win)
