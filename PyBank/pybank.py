import pathlib
import csv
import os

# Define variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

csvpath = pathlib.Path(r"C:\\Users\reeda\Anna\learnpython\pybank_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read/skip header row 
    csv_header = next(csvfile)

    for row in csv_reader:
        count_months += 1

        # Total profit/loss over entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:
            # change in profit/loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append lists
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)

            # Reset
            previous_month_profit_loss = current_month_profit_loss

    # Sum, average, min/max
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate/assign index values to min/max
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Text file 
file = os.path.join("output", r"C:\Users\reeda\Anna\learnpython\bankdata.txt")
with open(file, "w") as csv_file:
    csv_file.write("Financial Analysis\n")
    csv_file.write("----------------------------\n")
    csv_file.write(f"Total Months:  {count_months}\n")
    csv_file.write(f"Total:  ${net_profit_loss}\n")
    csv_file.write(f"Average Change:  ${average_profit_loss}\n")
    csv_file.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    csv_file.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")

