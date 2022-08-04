from pathlib import Path
import csv
def overhead_function(forex):
    """
    The function will compute the highest overhead expnense and reutrn the value with its respective category
    """
    try:
    #Bypassing any error
        #empty_list to store the CSV data
        empty_list = []
        #overhead_list to store the overhead expense value
        overhead_list = []
        #cat_list to store the various category
        cat_list = []
        #Creating a file path to access the CSV file for Overheads
        file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
        #Opening the CSV file as read mode
        with file_path.open(mode='r', encoding='UTF-8', newline="") as file:
            reader = csv.reader(file)
            #Skipping the header to only read the data
            next(reader)
            #For loop to access the data within the csv file
            for line in reader:
                #Appending the data from the CSV file to the empty_list
                empty_list.append(line)
        #for loop to iterate over the data in the list
        for value in empty_list:
        #Appending the data for overhead expense value into overhead_list using their index position
            overhead_list.append(value[1])
            #Appending the data for the type of category into cat_list using their index position
            cat_list.append(value[0])
        #Using list comprehension to convert the values in the list from str to float
        overhead_list_sorted = ([float(x) for x in overhead_list])
        #Sorting the overhead expense value from highest to lowest of which the 0 index position will always be the highest value
        overhead_list_sorted.sort(reverse=True)
        overhead_list_unsorted = ([float(x) for x in overhead_list])
        #For loop to iterate over the unsorted overhead expense data for each category. (in enumerate) to return the index position 
        #of the category type that has the highest overhead expense
        for category_type,overheads in enumerate(overhead_list_unsorted):
            #If statement to obtain the index position of the maximum overhead expense in the unsorted list
            if overheads == overhead_list_sorted[0]:
                #Variable to store the maximum overhead expense value
                max_overhead = overheads
                #Variable to store the index of the category type
                category = category_type
                file_path1 = Path.cwd()/"summary_report.txt"
                #Appends the maximum overhead expense & what category it falls under to summary_report.txt
                with file_path1.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    file.write(f"\n[HIGHEST OVERHEADS] {cat_list[category]}: SGD{round((max_overhead * forex),1)}")
    except TypeError:
        print("Refer to summary_report.txt")
    #Printing the str if a type error occurs during the conversion

overhead_function(1)



    





