#!/usr/local/bin python3

import os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")
output_file_path = os.path.join(script_dir, "output2.txt")
f_input = open(input_file_path, "r", encoding="utf-8")
f_output = open(output_file_path, "w")

wordMap = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}
    
def keyInWord(word: str) -> str:
  for key in wordMap.keys():
    if (word.count(key)):
      return key
  return ""

def getFirstInt(line: str):
  word = ""
  for l in line.strip():
    if str.isnumeric(l):
      return int(l)
    else:
      word = word + l
      if keyInWord(word):
        wordKey = keyInWord(word)
        return wordMap[wordKey]
      
def getLastInt(line: str):
  word = ""
  for l in line.strip():
    if str.isnumeric(l):
      return int(l)
    else:
      word = l + word
      if keyInWord(word):
        wordKey = keyInWord(word)
        return wordMap[wordKey]

def getInt(line: str):
  print("LINE:", line.strip(), file=f_output)    
  firstDig = getFirstInt(line)
  lastDig = getLastInt(line[::-1])
  concatNum = str(firstDig) + str(lastDig)
  print("line digit:", concatNum, file=f_output)
  return int(concatNum)

def main():
  total = 0
  for line in f_input:
    lineNum = getInt(line)
    total += lineNum
    print("SUBTOTAL:", total, file=f_output)
  print("TOTAL:", total, file=f_output)

main()
