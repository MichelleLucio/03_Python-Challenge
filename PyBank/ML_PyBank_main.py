# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

PyBank_csv_path = os.path.join('Resources','budget_data.csv')

#with open(PyBank_csv_path,'r') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')


#set variables
monthcounter = 0
netamount = 0
monthlydiff = 0
monthlydifftotal = 0
previousmonthamt = 0
monthlydiffdict = {}


#def loop for counting number of months
def month_number():
    PyBank_csv_path = os.path.join('Resources','budget_data.csv')
    with open(PyBank_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
    #monthcounter = 0
        csv_header = next(csvfile)
        monthcounter = len(list(csvreader))
    #for row in csvreader:
        #if row [0] == "Date":
            #pass
        #else:
            #counter = counter + 1
            #print (row)
            #if counter >= n:
                #break
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
def pl_change():
    PyBank_csv_path = os.path.join('Resources','budget_data.csv')
    with open(PyBank_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        monthlydiff = 0
        monthlydifftotal = 0
        previousmonthamt = 0
        monthlydiffdict = {}
        for row in csvreader:
            if row[0] == 'Date':
                pass
            else:  #calc for month diff, adding total of diff, add to dictionary, storing previous month info   

                monthlydiff = (int(row[1]) - previousmonthamt)
                monthlydifftotal = monthlydifftotal + monthlydiff
                monthlydiffdict.update({str(row[0]) : int(monthlydiff)})
                previousmonthamt = int(row[1])

    return monthlydiff, monthlydifftotal, monthlydiffdict
    #return monthlydifftotal


#dict.update({'key3':'geeks'})


#def for finding average of changes in profit/losses
#def monthlyave():
    #PyBank_csv_path = os.path.join('Resources','budget_data.csv')
    #with open(PyBank_csv_path,'r') as csvfile:
        #csvreader = csv.reader(csvfile, delimiter=',')

        #monthlydifftotal = 0
        #previousmonthamt = 0

        #for row in csvreader:
            #if row[0] == 'Date':
                #pass
            #else:  #adding total of diff, storing previous month info   

                #monthlydifftotal = monthlydifftotal + (int(row[1]) - previousmonthamt)

                #previousmonthamt = int(row[1])

    #return monthlydifftotal
    #monthlydifftotal / (monthcounter - 1)



#test if working
monthcounter = month_number()
netamount = net_total()
monthlydifftotal = pl_change()
monthlydiff = pl_change()

monthlydiffdict = pl_change()

print(monthcounter)
print(netamount)
print(monthlydiff)
print(monthlydifftotal)
#print(monthlydiffdict)










