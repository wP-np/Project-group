from pathlib import Path
import csv
#The program will compute the difference in the net profit between each day.
empty_list = []
pl_list = []
day_list = []
file_path = Path.cwd()/"csv_reports"/"p&l.csv"
with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
            empty_list.append(line)

for value in empty_list:
    pl_list.append(value[4])
    day_list.append(value[0])
print(day_list)
#Using list comprehension to convert the values in the list from str to int
pl_list1 = ([int(x) for x in pl_list])

list_diff = []
for n in range(1, len(pl_list1)):
    list_diff.append(int(pl_list1[n] - pl_list1[n-1]))

print(list_diff)

for difference in list_diff:
    if difference < 0:
        print("Negative net profit")