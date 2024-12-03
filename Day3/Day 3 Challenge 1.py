import re 

with open('memory.txt', 'r') as file:
    memory = file.read()

correctMemories = re.findall("mul\(\d+,\d+\)", memory)
correctNums = []
for x in range (len(correctMemories)):
    nums = re.findall("\d+", correctMemories[x])   
    correctNums.append(nums)

total = 0
for y in range (len(correctNums)):
    multi = (int((correctNums[y][0])) * int((correctNums[y][1])))  
    total += multi

print (total)   