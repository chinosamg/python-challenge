#import os and CSV to read file

import os
import csv

# Open Budget CSV file
budgetCSV = os.path.join('raw_data','budget_data.csv')
    #Set empty list variables
Date = []
Revenue =[]
Month = []
Year =[]
NewDate = []
RevenueChange =[]
Source =[]
TotalRevenue =0
TotalRevChange = 0
RevBeg=0
ItemCount = 0

# Open raw data 'budget_data.csv'
with open(budgetCSV,'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
        #skip headers
    next(csvReader, None)
        
    for row in csvReader:        
            #Append data from the row
        ItemCount = ItemCount + 1
        Date.append(row[0])
        Revenue.append(int(row[1]))
        TotalRevenue = TotalRevenue + int(row[1])
        RevEnd = int(row[1])
        RevChg = RevEnd - RevBeg
        TotalRevChange = TotalRevChange + RevChg
        RevenueChange.append(RevChg)
        Source.append('budget_data.csv')
        splitdate = row[0].split('-')
        Month.append(str(splitdate[0]))
        Year.append("20"+splitdate[1])
        NewDate.append(str(splitdate[0])+'-'+"20"+splitdate[1])
        RevBeg = RevEnd

#Calculate for analysis
AveRevChg = TotalRevChange / ItemCount
GIncrease = max(RevenueChange)
GDecrease = min(RevenueChange)
IncreaseDate = NewDate[RevenueChange.index(GIncrease)]
DecreaseDate = NewDate[RevenueChange.index(GDecrease)]
  
#Get unique value of Year-Months:
CountM = len(set(NewDate))

#Create text file to export results
with open('Financial_Analysis.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------\n")
    text.write("    Total Months: " + str(CountM) + "\n")
    text.write("    Total Revenue: " + "$" + str(TotalRevenue) +"\n")
    text.write("    Average Revenue Change: " + '$' + str(int(AveRevChg)) +'\n')
    text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
    text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n")
    text.write("----------------------------------------------------------\n") 