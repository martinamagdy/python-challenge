import csv
import os
from decimal import *

#function for taking csv file 
def election(filepath):

    candidates=[]
    vote=[]
    voters=0
    candidates=[]
    
    #open csv file
    with open(filepath,newline='') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')

        #skip header
        next(csvreader,None)
        
        for row in csvreader:

            #The total number of votes cast
             voters=voters+1

             #list of candidates and list of  number of votes each candidate won
             if row[2] not in candidates:
                candidates.append(row[2])
                vote.append(1)
             else:
                vote[candidates.index(row[2])]=vote[candidates.index(row[2])]+1

        #decide who's the winner
        win=max(vote)
        winner=candidates[vote.index(win)]

    #print the result
    
    print("Election Results\n-----------------------------")
    print("Total Votes: " +str(voters)+"\n-----------------------------")
    for candidate in candidates:
        percent=round((vote[candidates.index(candidate)]/voters)*100)
        print(candidate+":"+str(format(percent,'.3f'))+"% ("+str(vote[candidates.index(candidate)])+")") 
    print("-----------------------------")
    print("Winner: "+winner+"\n-----------------------------")

    outputfile= open("Election_Results_output.txt","w")
    outputfile.write("Election Results\n-----------------------------\n")
    outputfile.write("Total Votes: " +str(voters)+"\n-----------------------------\n")
    for candidate in candidates:
        percent=round((vote[candidates.index(candidate)]/voters)*100)
        outputfile.write(candidate+":"+str(format(percent,'.3f'))+"% ("+str(vote[candidates.index(candidate)])+")\n") 
    outputfile.write("-----------------------------\n")
    outputfile.write("Winner: "+winner+"\n-----------------------------")
    outputfile.close()

#calling the function and give it the file path 
path=os.path.join('election_data.csv')
election(path)
        
    
