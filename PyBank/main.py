import os
import csv
bank_csv = os.path.join("/Users/danbishop/Desktop/Rutgers Data Science Bootcamp/RU-JER-DATA-PT-10-2019-U-C/Homework/03-Python Homework/PyBank", 'Resources', 'budget_data.csv')
#Variables
total_months = 0
net_profit = 0
changes = []
months_count = []
greatest_incr = 0
greatest_decr = 0


#Working code below
with open(bank_csv, newline= '') as data:
    csvreader = csv.reader(data, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
    prev_profit = int(row[1])
    net_profit = net_profit + int(row[1])
    total_months = total_months + 1
    greatest_incmo = str(row[0])
    greatest_decmo = str(row[0])
    
    

    for row in csvreader:
        total_months = total_months + 1
        net_profit = net_profit + int(row[1])
        mo_change = int(row[1]) - prev_profit
        changes.append(mo_change)
        prev_profit = int(row[1])
        months_count.append(prev_profit)

        if int(row[1]) > greatest_incr:
            greatest_incr = int(row[1])
            greatest_incmo = row[0]
        if int(row[1]) < greatest_decr:
            greatest_decr = int(row[1])
            greatest_decmo = row[0]

    avg_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)
    

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f'Net Profit/Loss: ${str(net_profit)}')
print(f'Average Change: ${str(avg_change)}')
print(f'Greatest Increase in Profit: {str(greatest_incmo)} {str(high)}')
print(f'Greatest Decrease in Profit: {str(greatest_decmo)} {str(low)}')

output_fin = os.path.join("/Users/danbishop/Desktop/Rutgers Data Science Bootcamp/Python/python-challenge-db/PyBank/", 'PyBank.txt')
with open(output_fin, 'w',) as PyBank:
    PyBank.write("Financial Analysis\n")
    PyBank.write("----------------------------\n")
    PyBank.write(f"Total Months: {str(total_months)}\n")
    PyBank.write(f'Net Profit/Loss: {str(net_profit)}\n')
    PyBank.write(f'Average Change: {str(avg_change)}\n')
    PyBank.write(f'Greatest Increase in Profit: {str(greatest_incmo)} {str(high)}\n')
    PyBank.write(f'Greatest Decrease in Profit: {str(greatest_decmo)} {str(low)}\n')




