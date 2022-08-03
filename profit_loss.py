from pathlib import Path
import csv
def profitloss_function(forex):
    """
    #The the function will compute the difference in net profits between each day and will return the difference in net profit together with
    the day that there is a decline in net profit. Meanwhile, if each day is consecutively higher, the function will return the net profit surplus
    scenario
    """
    #empty_list to store all of the data form the CSV file
    empty_list = []
    pl_list = []
    day_list = []
    #Creating a file path to access the CSV file for Profit and Loss
    file_path = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
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
    #Appending the data for profit and loss into pl_list using their index position
        pl_list.append(value[4])
    #Appending the data for the range of days into the day_list using their index position
        day_list.append(value[0])
    #Using list comprehension to convert the values in the list from str to int
    pl_list_final = ([int(x) for x in pl_list])
    #Creating an empty list(list_diff) to store the difference in net profit between each days
    list_diff = []
    #Creating to iterate over the range of data(net profit per day)
    for n in range(1, len(pl_list_final)):
    #Appending the difference between the net profit per day to list_diff, obtaining the respective values based on their index position n - (n-1)
        list_diff.append(int(pl_list_final[n] - pl_list_final[n-1]))
    file_path1 = Path.cwd()/"summary_report.txt"
    with file_path1.open(mode = "a", encoding = "UTF-8", newline = "") as file:
    #For loop to iterate over the the data for the difference in net profit per day. (In enumerate) to return the index position of the negative value to be used in the day_list.
        for day,difference in enumerate(list_diff):
        #If statement to identify the values by which the difference is negative
            if difference < 0:
        #Variable to store the negative values as positive
                final_diff = abs(difference)
            #Variable for the index position of the day at which the net profit is negative
                index_day = day +1
            #printing the decline in net profit and the day at which it occured.
            #with file_path1.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                file.write(f"\n[PROFIT DEFICIT] DAY: {day_list[index_day]}, AMOUNT: SGD{final_diff * forex}")
            else:
                continue
            if difference > 0:
                file.write("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
            

profitloss_function(1)