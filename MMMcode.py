import csv
from collections import Counter

"""new_data = "Tanush Prusty"
data = Counter(new_data)
new_list = data.items()
values = data.values()
print(values)"""

with open("Height-Weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#FINDING THE MEAN
n = len(new_data)
total = 0
for x in new_data:
    total = total + x
    #Alternate: total += x

mean = total/n

print("Mean is: ", mean)

#FINDING THE MEDIAN
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]

print("Median is: ", median)

#FINDING THE MODE
data = Counter(new_data)
mode_data_range = {
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for height, occurence in data.items():
    if 85 < float(height) < 95:
        mode_data_range["85-95"] += occurence
    elif 95 < float(height) < 105:
        mode_data_range["95-105"] += occurence
    elif 105 < float(height) < 115:
        mode_data_range["105-115"] += occurence
    elif 115 < float(height) < 125:
        mode_data_range["115-125"] += occurence
    elif 125 < float(height) < 135:
        mode_data_range["125-135"] += occurence
    elif 135 < float(height) < 145:
        mode_data_range["135-145"] += occurence
    elif 145 < float(height) < 155:
        mode_data_range["145-155"] += occurence
    elif 155 < float(height) < 165:
        mode_data_range["155-165"] += occurence
    elif 165 < float(height) < 175:
        mode_data_range["165-175"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1])/2)

print("Mode is: ", mode)