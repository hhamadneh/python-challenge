# import 
import csv
import os
budgetfile=os.path.join("PyBank","Resources", "budgetdata.csv")

with open(budgetfile) as financial_data:
    reader=csv.reader(financial_data)
    for row in reader:
        print(row[0])