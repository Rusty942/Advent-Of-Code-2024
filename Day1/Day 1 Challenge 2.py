import numpy as np

with open('Codes.txt', 'r') as file:
    allCodes = file.read().split()

list1 = allCodes[0::2]
list2 = allCodes[1::2]

list1Sorted = np.sort(list1).astype(int)
list2Sorted = np.sort(list2).astype(int)

totalSimScore = 0
for x in range (len(list1Sorted)):
    codeAmm = 0
    for y in range (len(list2Sorted)):
        if (list1Sorted[x] == list2Sorted[y]):
            codeAmm += 1
    totalSimScore += (list1Sorted[x] * codeAmm)  

print(totalSimScore)      