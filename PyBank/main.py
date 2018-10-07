import csv
import os

#function for taking csv file and do budget calculation
def budget(filepath):
    totalmonths=0
    totalamount=0

    #read csv file
    with open(filepath,newline='') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')

        #skip the header
        next(csvreader,None)
        
        bud=[]
        month=[]
        secondmonth=0
        change=[]

        for row in csvreader:
            #change in "Profit/Losses" between months
            bud.append(int(row[1]))
            month.append(row[0])
            second=int(row[1])
            changebetween=second-bud[len(bud)-2]
            change.append(changebetween)

            #total number of months
            totalmonths=totalmonths+1

            #The total net amount of "Profit/Losses" over the entire period
            totalamount=totalamount+int(row[1])

        change=change[1:len(change)]

        #The greatest increase in profits over the entire period
        increase=max(change)

        #The greatest decrease in losses over the entire period
        decrease=min(change)

        #The average change in "Profit/Losses" between months over the entire period
        sums=sum(change)
        averagechange=round(sums/len(change),2)
        #print the result
        print("Financial Analysis\n-------------------------")
        print("Total Months: " +str(totalmonths))
        print("Total: $" + str(totalamount))
        print("Average Change: $"+str(averagechange))
        print("Greatest Increase in Profits: "+str(month[change.index(increase)+1])+"($"+str(increase)+")")
        print("Greatest Decrease in Profits: "+str(month[change.index(decrease)+1])+"($"+str(decrease)+")")


        outputfile= open("Financial_Analysis_output.txt","w")
        outputfile.write("Financial Analysis\n-------------------------\n")
        outputfile.write("Total Months: " +str(totalmonths)+"\n")
        outputfile.write("Total: $" + str(totalamount)+"\n")
        outputfile.write("Average Change: $"+str(averagechange)+"\n")
        outputfile.write("Greatest Increase in Profits: "+str(month[change.index(increase)+1])+"($"+str(increase)+")\n")
        outputfile.write("Greatest Decrease in Profits: "+str(month[change.index(decrease)+1])+"($"+str(decrease)+")\n")
        outputfile.close()
            
path=os.path.join('budget_data.csv')
budget(path)
