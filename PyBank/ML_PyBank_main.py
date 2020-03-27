# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

PyBank_csv_path = os.path.join('Resources','budget_data.csv')


#set variables
monthcounter = 0
netamount = 0
monthlydiff = 0
monthlydifftotal = 0
previousmonthamt = 0
monthlydiffave = 0
monthlydifflist = []
max_monthnum = 0
min_monthnum = 0
csvDataFile = str


#def loop for counting number of months
def month_number():
    PyBank_csv_path = os.path.join('Resources','budget_data.csv')
    with open(PyBank_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvfile)
        monthcounter = len(list(csvreader))

    return monthcounter          


#def loop for  net amount of profit/losses over entire period
def net_total():
    PyBank_csv_path = os.path.join('Resources','budget_data.csv')
    with open(PyBank_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        netamount = 0
        for row in csvreader:
            if row [0] == "Date":
                pass
            else:
                netamount = netamount + int(row[1])
                #print (row)

    return netamount 


#def for creating a dictionary for values of changes in profit/losses
#def pl_change():
PyBank_csv_path = os.path.join('Resources','budget_data.csv')
with open(PyBank_csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    monthlydiff = 0
    previousmonthamt = 0
    monthlydifflist = []
    monthlydiffave = 0
    for row in csvreader:
        if row[0] == 'Date':
            pass
        else:  
                
                #calc for month diff, adding total of diff, add to dictionary, storing previous month info   
            monthlydiff = (int(row[1]) - previousmonthamt)

            monthlydifflist.append(int(row[1]) - previousmonthamt)
            previousmonthamt = int(row[1])

  

#run above functions
monthcounter = month_number()
netamount = net_total()


#for finding average of changes in profit/losses
for x in monthlydifflist[1:]:
    monthlydifftotal = ((monthlydifftotal) + x)
    monthlydiffave = ((monthlydifftotal) / (monthcounter - 1))


with open(PyBank_csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#for printing max & min month
    for index, row in enumerate(csvreader):
        if index == (monthlydifflist.index(max(monthlydifflist)) +1):
            max_month = (row[0])
            #print (max_month)
        else:
            if index == (monthlydifflist.index(min(monthlydifflist)) +1):
                min_month = (row[0])
                #print(min_month)



print('Financial Analysis')
print('\n', '----------------------')
print('Total Months: ', monthcounter)
print('Net Total of Profit/Losses: $', netamount)
print('Average Change: $', round(monthlydiffave, 2))
print('Greatest Increase in Profits: $', max(monthlydifflist), max_month)
print('Greatest Decrease in Profits: $', min(monthlydifflist), min_month)



#def to print to text file
def printtofile():
    output_path = os.path.join('FinancialAnalysis.txt')
    with open(output_path, 'w', newline='') as f:
        f.write('Financial Analysis')
        f.write('\n' + '------------------------')
        f.write('\n' + 'Total Months: '+ str(monthcounter))
        f.write('\n' + '------------------------')
        f.write('\n' + 'Average Change: $'+ str(round(monthlydiffave, 2)))
        f.write('\n' + 'Greatest Increase in Profits: $' + str(max(monthlydifflist)) + ' ' + str(max_month))
        f.write('\n' + 'Greatest Decrease in Profits: $' + str(min(monthlydifflist)) + ' ' + str(min_month))

#run print functions
printtofile()

