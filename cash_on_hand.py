from pathlib import Path
import csv
#The program will compute the difference in the cash on hand between each day.
empty_list = []
coh_list = []
day_list = []
#Creating a file path to access the CSV file for Cash on Hand
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
#Opening the CSV file as read mode
with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
    reader = csv.reader(file)
    #Skipping the header to only read the data
    next(reader)
    #For loop to access the data within the csv file
    for line in reader:
        #Appending the data from the CSV file to the empty_list
        empty_list.append(line)
#For loop to iterate over the data from the empty_list
for value in empty_list:
    #Appending the data for Cash on Hand into coh_list using their index position
    coh_list.append(value[1])
    #Appending the data for the range of days into the day_list using their index position
    day_list.append(value[0])
#Using list comprehension to convert the values in the list from str to int
coh_list_final = ([int(x) for x in coh_list])
#Creating an empty list(list_diff) to store the difference in Cash on Hand between each days
list_diff = []
#Creating to iterate over the range of data(Cash on Hand per day)
for n in range(1, len(coh_list_final)):
    #Appending the difference between the Cash on Hand to list_diff, obtaining the respective values based on their index position n - (n-1)
    list_diff.append(int(coh_list_final[n] - coh_list_final[n-1]))
#For loop to iterate over the the data for the difference in Cash on Hand per day. (In enumerate) to return the index position of the negative value to be used in the day_list.
for day,difference in enumerate(list_diff):
    #If statement to identify the values by which the difference is negative
    if difference < 0:
        #Variable to store the negative values
        final_diff = difference
        #Variable for the index position of the day at which the difference in Cash on Hand is negative
        index_day = day +1
#printing the decline in Cash on Hand and the day at which it occured.
print (f"Change in Cash on Hand: ${final_diff}. Day in which it changed: {day_list[index_day]}")
