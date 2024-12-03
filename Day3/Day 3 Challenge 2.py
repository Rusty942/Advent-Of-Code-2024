import re 

with open('memory.txt', 'r') as file:
    memory = file.read()
    
doSplit= memory.split("do()")
dontSplit = memory.split("don't()")

if (doSplit[0] > dontSplit[0]):
    start = dontSplit[0]
else:
    start = doSplit[0]
    
do = str(re.escape("do()"))
dont =  str(re.escape("don't()"))
dos = re.findall(f'{do}(.*?){dont}', memory)

string = start
for x in range (len(dos)):
    string += dos[x]
correctMemories = re.findall("mul\(\d+,\d+\)", string)

correctNums = []
for x in range (len(correctMemories)):
    nums = re.findall("\d+", correctMemories[x])   
    correctNums.append(nums)
    
total = 0
for y in range (len(correctNums)):
    multi = (int((correctNums[y][0])) * int((correctNums[y][1])))  
    total += multi

print (total)  