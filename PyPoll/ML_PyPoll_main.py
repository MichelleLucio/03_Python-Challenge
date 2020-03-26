# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

PyPoll_csv_path = os.path.join('Resources','election_data.csv')

with open(PyPoll_csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

vote_count = int

#def loop for counting number of rows
def row_Number (n):
    PyPoll_csv_path = os.path.join('Resources','election_data.csv')

    with open(PyPoll_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        Counter = 0
        for row in csvreader:
            Counter = Counter + 1
            print (row)
            if Counter >= n:
                break

#def loop to total number of votes
def Total_votes():
    #initialize vote counter
    vote_count = 0
    PyPoll_csv_path = os.path.join('Resources','election_data.csv')

    with open(PyPoll_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvfile)
        for row in csvreader:
      
            vote_count = vote_count + 1 #total number of votes
    return vote_count

#def loop to creat list of candidates
def candidate_list():
    PyPoll_csv_path = os.path.join('Resources','election_data.csv')

    with open(PyPoll_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        candidates = []
        for row in csvreader:
            if row[2] == 'Candidate':
                pass
            else:
                if row[2] not in candidates: #check if candidate in list
                    candidates.append(row[2]) #add candidate if not in list
                else:
                    pass
    return candidates


#def for looping to tallying votes for each candidate using dictionary
def candvotecount():
    PyPoll_csv_path = os.path.join('Resources','election_data.csv')

    with open(PyPoll_csv_path,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        candidatedict = {}
        for candidate in candidates:
            csv_header = next(csvfile) #skip header row
            candidatedict[candidate] = [0,0]   #dictionary is candidate to (percentage, votes)

        for row in csvreader:
            if row[0] == 'Voter ID':
                pass
            else:
                for key, value in candidatedict.items(): 
                    if key == row[2]:    #go thru candidate dictionary
                        value[1] = value[1] + 1   #increment vote count
                        value[0] = round(((value[1] / vote_count) * 100), 1)  #update percent votes for candidate
                    else:
                        pass
    return candidatedict

#def for finding the winner
def findwinner():
    firstplace = 0
    for key, value in candidatedict.items():  #go thru dictionary
        if value[1] > firstplace:   #will save largest count until all went thru
            firstplace = value[1]
            winner = key   #storage for winner name
        else:    
            pass
    return winner



# run above functions in sequence to get numbers
vote_count = Total_votes()
candidates = candidate_list()
candidatedict = candvotecount()
winner = findwinner()

#def to print results to screen
def printresults():
    print('Election Results')
    print('------------------------')
    print('\n', 'Total Votes:  ', vote_count)
    print('------------------------')
    for key, value in candidatedict.items():
        print('\n' + key + ' : ', str(value[0]) + ' % (' + str(value[1]) + ')')
    print('------------------------')
    print('\n' + 'Winner: ', winner)
    print('------------------------')


#def to print to text file
def printtofile():
    output_path = os.path.join('election_results.txt')
    with open(output_path, 'w', newline='') as f:
        f.write('Election Results')
        f.write('\n' + '------------------------')
        f.write('\n' + 'Total Votes:  ' + str(vote_count))
        f.write('\n' + '------------------------')
        for key, value in candidatedict.items():
            f.write('\n' + key + ' : ' + str(value[0]) + ' % (' + str(value[1]) + ')')
        f.write('\n' + '------------------------')
        f.write('\n' + 'Winner: ' + winner)
        f.write('\n' + '------------------------')

#run print functions
printresults()
printtofile()










