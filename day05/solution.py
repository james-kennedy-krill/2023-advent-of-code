#!/usr/bin python3

import math as m, re, os

script_dir = os.path.dirname(os.path.realpath(__file__))
# input_file_path = os.path.join(script_dir, "input.txt")
input_file_path = os.path.join(script_dir, "input_example.txt")
output_file_path = os.path.join(script_dir, "output.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

board = list(f_input)

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