import csv

file_path = "/Users/owner/OneDrive/python-challenge-main/PyBank/Resources/budget_data.csv"

# calculate the total months

with open(file_path, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    data = list(csvreader)
    dates = [row["Date"] for row in csvreader]
    profit_losses_values = [int(row["Profit/Losses"]) for row in csvreader]
    

profit_losses_values = [int(row["Profit/Losses"]) for row in data]
dates = [row["Date"] for row in data]

# Calculate the total number of unique months
total_months = len(set(dates))
print(f"The total number of months is: {total_months}")

# Calculate the net total amount of "Profit/Losses"
net_total = sum(profit_losses_values)
print(f"The net total of profit/losses is: {net_total}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

changes = [profit_losses_values[i + 1] - profit_losses_values[i] for i in range(len(profit_losses_values) - 1)]
if len(changes) > 0:
    average_change = sum(changes) / len(changes)
    print(f"The average change in 'Profit/Losses' is: ${average_change:.2f}")
else:
    print("There are no changes in 'Profit/Losses'.")
    

    
# The greatest increase in profits (date and amount) over the entire period
if changes:
    # Find the index of the greatest increase
    max_increase_index = changes.index(max(changes))

    # Get the date and amount of the greatest increase
    greatest_increase_date = dates[max_increase_index + 1]
    greatest_increase_amount = max(changes)

    # Print the result
    print(f"The greatest increase in profits occurred on {greatest_increase_date} with an amount of ${greatest_increase_amount}")
else:
    print("There are no changes in 'Profit/Losses'.")
    
# The greatest decrease in profits (date and amount) over the entire period

if changes:
    # Find the index of the greatest decrease
    max_decrease_index = changes.index(min(changes))

    # Get the date and amount of the greatest decrease
    greatest_decrease_date = dates[max_decrease_index + 1]
    greatest_decrease_amount = min(changes)

    # Print the result
    print(f"The greatest decrease in profits occurred on {greatest_decrease_date} with an amount of ${greatest_decrease_amount}")
else:
    print("There are no changes in 'Profit/Losses'.")
