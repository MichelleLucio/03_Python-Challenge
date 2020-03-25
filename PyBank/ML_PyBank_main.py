# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

PyBank_csv_path = os.path.join('Resources','budget_data.csv')




# Define the function and have it accept the 'PyBankInfo' as its sole parameter
def budget():
    PyBank_csv_path = os.path.join('Resources','budget_data.csv')

#set variables
    month = str(budget_data[0])   #problems with parameter here -needs definition!
    Profit_Losses = int(budget_data[1])

# Read the header row first (should this be here?)
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

#count months
    Total_month = len(list(csvreader))
    print(f"Total Months: {str(Total_month)}")
#Net total of profit/losses over entire period
    Sum_of_all = 0

    for row in csvreader:
       total += float(row[2])
    print(f"Total: {str(Sum_of_all)}")


#average of the changes in profit/losses over entire period



#greatest increase in profits (date & amount) over entire period
    maxNumber = max(Profit_Losses), 2
    


#greatest decrease in profits (date & amount) over entire period
    minNumber = min(Profit_Losses), 2





# Method 2: Improved Reading using CSV module
#with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
with open(PyBank_csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#print out analysis
print ("Financial Analysis")
print ("_____________________")
budget()











#test print
    #for row in csvreader:
        #if row[0] is ("Jan-2012"):
            #print("This is working so far")



#csv_header = next(csvfile)
#print(f"Header: {csv_header}")

#added way to print list of headers with number of columns
#count = 0
#header_list = csv_header.split(",")
#for col in header_list:
#    count +=1
 #   print(count,col)

# Read the header row first (skip this step if there is not header)
#csv_header = next(csvfile)
#print(f"CSV Header: {csv_header}")

# Read each row of data after the header
#for row in csvreader:
 #   print(row)
