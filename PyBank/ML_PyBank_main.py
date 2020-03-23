# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

PyBank_csv_path = os.path.join('Resources','budget_data.csv')

# Define the function and have it accept the 'PyBankInfo' as its sole parameter
def budget(PyBankInfo):

#set variables
    month = str(PyBankInfo[0])
    Profit_Losses = int(PyBankInfo[1])

# Read the header row first (should this be here?)
    csv_header = next(csvfile)
        print(f"CSV Header: {csv_header}")

#count months
    Total_month = len(list(csvreader))

#Net total of profit/losses over entire period

#average of the changes in profit/losses over entire period

#greatest increase in profits (date & amount) over entire period

#greatest decrease in profits (date & amount) over entire period



# Method 2: Improved Reading using CSV module
#with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
with open(PyBank_csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')












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
