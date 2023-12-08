#!/usr/bin python3

import math as m, re, os, gc

gc.set_threshold(0)

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
# input_file_path = os.path.join(script_dir, "input_example.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

seeds = []
seed_data = {}
map_keys = []
maps = {}
location_map_key = "humidity-to-location map"
locations = []
number_re = re.compile(r'(\d+)')

current_map_key = ""
for line in f_input:
  if re.match("seeds:", line):
    # For part 2, we need to process this seeds array
    # We need to put it into pairs, a number and a length
    # then we need to create a list that enumerates out all those numbers
    # print("seeds:", line)
    seeds_raw = list(map(int, number_re.findall(line)))
    seed_index = 0
    for i in range(int((len(seeds_raw)+1)/2)):
      for r in range(int(seeds_raw[i+i+1])):
        seeds.append(seeds_raw[i+i]+r)
      
  elif re.match(r"([a-z]+-to-[a-z]+\s[a-z]+\:)", line):
    map_key = re.match(r"([a-z]+-to-[a-z]+\s[a-z]+)", line).group()
    current_map_key = map_key
    map_keys.append(map_key)
    maps[map_key] = []
  elif re.match(r"(\d+\s?)+", line):
    map_nums = list(map(int, number_re.findall(line)))
    maps[current_map_key].append(map_nums)
  else:
    current_map_key = ""

print("SEEDS:", seeds)

for seed in seeds:
  # print("\n")
  # print("PROCESSING SEED:", seed)
  seed_data[seed] = {}
  next_val = seed
  for map_key in map_keys:
    # print("PROCESSING MAP:", map_key)
    map_datas = maps[map_key]
    # print("MAP DATAS:", map_datas)
    for map_data in map_datas:
      # print("MAP DATA:", map_data)
      low = map_data[1]
      # print("\tlow:", low)
      high = map_data[1]+(map_data[2]-1)
      # print("\thigh:", high)
      # print("\tprev_val:", next_val)
      if high >= next_val >= low:
        next_val -= (map_data[1]-map_data[0])
        seed_data[seed][map_key] = next_val
        # print("\tNEXT VAL SET:", next_val)
        break
      else:
        # print("\tstored value:", next_val)
        seed_data[seed][map_key] = next_val
    if map_key == location_map_key:
      locations.append(seed_data[seed][map_key])
      print(locations)
      seed_data[seed] = {}
      gc.collect()
   
print("SEED DATA", seed_data) 
print("LOCATIONS:", locations)
print("Lowest location:", min(locations))
