reports = []
with open('Reports.txt', 'r') as file:
    for line in file:
        reports.append(line.rstrip())
        
reportsSep = []
for x in range (len(reports)):
    levels=[]
    currentNumber = ""
    for level in reports[x]:
        if level != ' ':
            currentNumber += level
        else:
            levels.append(int(currentNumber))
            currentNumber = ""
    levels.append(int(currentNumber))
    reportsSep.append(levels)
reports=reportsSep

safeReports = 0
for report in reports:
    incrementing = True
    decrementing = True
    notSafe = False
    for z in range (len(report) -1):
        gap = abs(report[z + 1] - report[z]) 
        if gap < 1 or gap > 3:
            notSafe = True
        if (report[z] < report[z + 1]):
            decrementing = False
        elif (report[z] > report[z + 1]):
            incrementing = False
    if (incrementing or decrementing) and notSafe == False:
        safeReports += 1
    else:
        for w in range(len(report)):
            newReport= report[:]
            newReport.pop(w)
            incrementing = True
            decrementing = True
            notSafe = False
            for v in range (len(newReport) -1):
                gap = abs(newReport[v + 1] - newReport[v]) 
                if gap < 1 or gap > 3:
                    notSafe = True
                if (newReport[v] < newReport[v + 1]):
                    decrementing = False
                elif (newReport[v] > newReport[v + 1]):
                    incrementing = False
            if (incrementing or decrementing) and notSafe == False:
                safeReports += 1
                break
            
print (safeReports)
          