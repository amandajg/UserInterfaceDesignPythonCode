from matplotlib import pyplot as plt
import csv
import statistics

xAxis = []
participantsData = [[],[],[],[],[]]
count = 0

# getting data from csv file

with open('PrototypeTestResults.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in filereader:
        if(count != 0):
            participantsData[count-1] = row
        else:
            xAxis = row
        count += 1

for array in participantsData:
    for i in range(len(array)):
        array[i] = float(array[i])

# calculating mean and standard deviation

meanOfEachTest = []
standardDevOfEachTest = []

for i in range(len(participantsData)+1):
    sum = 0.0
    mean = 0.0
    sum = participantsData[0][i] + participantsData[1][i] + participantsData[2][i] + participantsData[3][i] + participantsData[4][i]
    mean = sum / 5.0
    meanOfEachTest.append(mean)

for i in range(len(participantsData)+1):
    currentTest = []
    currentTest = [participantsData[0][i], participantsData[1][i], participantsData[2][i], participantsData[3][i], participantsData[4][i]]
    standardDevOfEachTest.append(statistics.stdev(currentTest))

# printing calculations

print("")
print("Means (seconds):")
print("")
print(f"{'Assignments Due Nov 16' : <28} - ", meanOfEachTest[0])
print(f"{'Networks Overview' : <28} - ", meanOfEachTest[1])
print(f"{'Individual Grades For Class' : <28} - ", meanOfEachTest[2])
print(f"{'Notification Settings' : <28} - ", meanOfEachTest[3])
print(f"{'App Language Settings' : <28} - ", meanOfEachTest[4])
print(f"{'New Assignment Nov 6' : <28} - ", meanOfEachTest[5])

print("")

print("Standard Deviations (seconds):")
print("")
print(f"{'Assignments Due Nov 16' : <28} - ", standardDevOfEachTest[0])
print(f"{'Networks Overview' : <28} - ", standardDevOfEachTest[1])
print(f"{'Individual Grades For Class' : <28} - ", standardDevOfEachTest[2])
print(f"{'Notification Settings' : <28} - ", standardDevOfEachTest[3])
print(f"{'App Language Settings' : <28} - ", standardDevOfEachTest[4])
print(f"{'New Assignment Nov 6' : <28} - ", standardDevOfEachTest[5])
print("")

# plotting data

plt.figure(figsize=(15, 7))
plt.ylabel('Time (seconds)',fontsize=12)
plt.xlabel('Tests',fontsize=12)

for i in range(len(participantsData)):
    plt.plot(xAxis, participantsData[i], label=str(i))

plt.legend(['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4', 'Participant 5'], ncol=2)
plt.show()