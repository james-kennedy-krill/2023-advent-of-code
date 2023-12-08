#!/usr/bin python3

import math as m, re, os

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
number_re = re.compile('(\d+)')
# ([a-z]+-to-[a-z]+\s[a-z]+\:[.\n\d\s]*)(?=(\n\n|$))

current_map_key = ""
for line in f_input:
  if re.match("seeds:", line):
    print("seeds:", line)
    seeds = list(map(int, number_re.findall(line)))
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
print("MAP KEYS:", map_keys)
print("MAPS:", maps)

for seed in seeds:
  print("\n")
  print("PROCESSING SEED:", seed)
  seed_data[seed] = {}
  next_val = seed
  for map_key in map_keys:
    print("PROCESSING MAP:", map_key)
    map_datas = maps[map_key]
    print("MAP DATAS:", map_datas)
    for map_data in map_datas:
      print("MAP DATA:", map_data)
      low = map_data[1]
      print("\tlow:", low)
      high = map_data[1]+(map_data[2]-1)
      print("\thigh:", high)
      print("\tprev_val:", next_val)
      if high >= next_val >= low:
        next_val -= (map_data[1]-map_data[0])
        seed_data[seed][map_key] = next_val
        print("\tNEXT VAL SET:", next_val)
        break
      else:
        print("\tstored value:", next_val)
        seed_data[seed][map_key] = next_val
    if map_key == location_map_key:
      locations.append(seed_data[seed][map_key])
   
print("SEED DATA", seed_data) 
print("LOCATIONS:", locations)
print("Lowest location:", min(locations))
# TDD
# 
# 1. Make dictionary of seed numbers (seeds needing to be planted)
#    each entry should have:
#    seedNum: {
#       seed: number,
#       soil: number,
#       fertilizer: number,
#       water: number,
#       light: number,
#       temperature: number,
#       humidity: number,
#       location: number
#     }
  

# 2. There should probably be some generic mapping function that
#     a. takes a value to be mapped
#     b. and the map to use
#     c. and produces the next item
#
# So maybe like:  farmingMap(value: number, map: "soil-to-fertilizer")
#
# From this information we know:
#  - the number to be mapped (value)
#  - the map to use (map)
#  - where to save the mapped value into (map regex after "to-" is the key to save the new value into)

# 3. With this you could call a function that then calls and sets a series of values
#
# i.e.  mapSeedToSoil(79)
#
# def mapSeedToSoil(seedNum: number):
#   soil_value = farmingMap(seedNum, "seed-to-soil");
#   ## update seeds
#   seeds[seedNum].soil = soil_value
#   mapSoilToFertilizer(soil_value, seedNum)
#
# def mapSoilToFertilizer(soilNum: number, seedNum: number):
#   fertilizer_value = farmingMap(soilNum, "fertilizer-to-water")
#   seeds[seedNum].fertilizer = fertilizer_value
#   mapFertilizerToWater(fertilizer_value, seedNum)
#
# and so on...
#
# this would eventually give us a giant dictionary of all the seeds, with seeds[#].location values
#
# to answer this question I think we need to determine the lowest of these and return this number
