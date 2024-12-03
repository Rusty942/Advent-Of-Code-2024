import numpy as np

with open('Codes.txt', 'r') as file:
    allCodes = file.read().split()

list1 = allCodes[0::2]
list2 = allCodes[1::2]

list1Sorted = np.sort(list1).astype(int)
list2Sorted = np.sort(list2).astype(int)

totalDeductions = 0
for x in range (len(list1Sorted)):
    if(list1Sorted[x] < list2Sorted[x]):
        deduction = (list2Sorted[x] - list1Sorted[x])
    elif(list2Sorted[x] < list1Sorted[x]):
        deduction = (list1Sorted[x] - list2Sorted[x])
    else:
        deduction = 0
    totalDeductions += deduction

print (totalDeductions)