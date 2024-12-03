import re 

with open('memory.txt', 'r') as file:
    memory = file.read()
    
doSplit= memory.split("do()")
dontSplit = memory.split("don't()")

if (len(doSplit[0]) > len(dontSplit[0])):
    start = dontSplit[0]
else:
    start = doSplit[0]
    
do = str(re.escape("do()"))
dont =  str(re.escape("don't()"))
dos = re.findall(f'{do}(.*?){dont}', memory)
extraDos = re.findall(f'{do}(?!.*{dont}).*?{do}', memory)

string = start
for x in range (len(dos)):
    string += dos[x]
extraString = ""
for z in range (len(extraDos)):
    extraString += extraDos[z]
correctMemories = re.findall("mul\(\d+,\d+\)", string)
extraCorrectMemories = re.findall("mul\(\d+,\d+\)", extraString)

correctNums = []
for x in range (len(correctMemories)):
    nums = re.findall("\d+", correctMemories[x])   
    correctNums.append(nums)

extraCorrectNums = []
for x in range (len(extraCorrectMemories)):
    extraNums = re.findall("\d+", extraCorrectMemories[x])   
    extraCorrectNums.append(extraNums)
    
total = 0
for y in range (len(correctNums)):
    multi = (int((correctNums[y][0])) * int((correctNums[y][1])))  
    total += multi

for y in range (len(extraCorrectNums)):
    multi = (int((extraCorrectNums[y][0])) * int((extraCorrectNums[y][1])))  
    total += multi


print (total)  