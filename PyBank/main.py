# Modules
import os
#Module for reading CSV files
import csv
#set path for file
csv_budget_path = os.path.join("Resources","budget_data.csv")
#setting uo the variables
#creating a list for all the months in CSV file
Months = []
#creating a list for total profits/loss in CSV file
profit = []
#setting up initial values 
# Counter for calculating total months in CSV
total_months = 0
#Counter for calculating total profit/loss in CSV
total_profit = 0
# Calculate the chnage when every row is read 
change_profit = 0
#storing the profit/loss 
profit_value = 0

#Reading the CSV file
with open(csv_budget_path, newline="") as csvfile:
    #splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #Reading Header row of CSV file
    header = next(csvreader)
    # Moving to the first row after header
    Row_1 = next(csvreader)
    # Updating the counter for the first row
    total_months = total_months +1
    total_profit = total_profit + int(Row_1[1])
    profit_value = int(Row_1[1])
    #print(total_profit)
    #print(profit_value)
    # Read through each row of data after the header
    for row in csvreader:
    #Adding to the Month list created 
     Months.append(row[0])
    # Updating the profit/loss change with each row
     change_profit = int(row[1]) - profit_value
     profit.append(change_profit)
     profit_value = int(row[1])
    #Updating total months
     total_months = total_months + 1
    # net total amount of profit/loss over the entire period
     total_profit = total_profit + int(row[1])
    #Average change
     Average_change = sum(profit) / len(profit)
     rounded_average = format(Average_change,'.2f')
#Greatest increase in profit from the profit list
    Greatest_profit = max(profit)
 #Corresponding index to the greatest increse from profit list
    greatest_profit_index = profit.index(Greatest_profit)
#Corresponding Greatest increase in profits month
    Month_greatest_increase = Months[greatest_profit_index]
#Greatest decrease in profit
    Greatest_decrease_profit = min(profit)
#Corresponding indes to the greatest decrese in profit from the profit lis
    greatest_decrease_index = profit.index(Greatest_decrease_profit)
#Corresponding decrese month
    Month_greates_decrease = Months[greatest_decrease_index]
# Printing the final result 
    print("Financial Analysis")
    print('__________________________________')
    print(f"Total Months: {str(total_months)}")
    print(f"Total : ${str(total_profit)}")
    print(f"Average Change : ${str(rounded_average)}")
    print(f"Greatest Increase in Profits: {Month_greatest_increase}  (${str(Greatest_profit)})")
    print(f"Greatest Decrease in Profits: {Month_greates_decrease}  (${str(Greatest_decrease_profit)})")
#Exporting text file
    output_path = os.path.join("analysis", "Pybankresult.txt")
    with open(output_path, 'w') as file:
        file.write("Financial Analysis\n"
                  "__________________________________\n"
                  f"Total Months: {str(total_months)}\n"
                  f"Total : ${str(total_profit)}\n"
                  f"Average Change : ${str(rounded_average)}\n"
                  f"Greatest Increase in Profits: {Month_greatest_increase}  (${str(Greatest_profit)})\n"
                  f"Greatest Decrease in Profits: {Month_greates_decrease}  (${str(Greatest_decrease_profit)})\n")
file.close()