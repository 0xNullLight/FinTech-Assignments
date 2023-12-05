# import library
import os
import csv

# os.path is a function that allows us to use OS routines that is common in Posix pathnames 
# os.path.join allows for the join of two or more pathname components that makes up the path
# Reference help(os)

# Set Path
pybank_csv = os.path.join("budget_data.csv")

# Initialize variables
total_months = 0
total_profit = 0
monthly_changes = []
dates = []

# Read the CSV file
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvreader)

    # Iterate through rows in the CSV
    for row in csvreader:
        # Calculate total months
        total_months += 1

        # Extract date and profit, convert profit to integer
        date = row[0]
        profit = int(row[1])

        # Add date to the dates list
        dates.append(date)

        # Calculate total profit
        total_profit += profit

        # Store monthly changes
        if total_months == 1:
            # For the first month, set initial profit
            initial_profit = profit
        else:
            # For subsequent months, calculate change and store it
            monthly_change = profit - initial_profit
            monthly_changes.append(monthly_change)
            initial_profit = profit

# Calculate average change
average_change = round(sum(monthly_changes) / len(monthly_changes), 2)

# Find greatest increase and decrease in profits and their dates
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)
increase_date = dates[monthly_changes.index(greatest_increase) + 1]  # +1 due to index offset
decrease_date = dates[monthly_changes.index(greatest_decrease) + 1]  # +1 due to index offset

# Print the analysis to the terminal
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profits: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")
print("----------------------------------------------------------")

# Write the analysis to a text file
with open("financial_analysis.txt", "w") as text_file:
    text_file.write("----------------------------------------------------------\n")
    text_file.write("  Financial Analysis\n")
    text_file.write("----------------------------------------------------------\n")
    text_file.write(f"    Total Months: {total_months}\n")
    text_file.write(f"    Total Profits: ${total_profit}\n")
    text_file.write(f"    Average Change: ${average_change}\n")
    text_file.write(f"    Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    text_file.write(f"    Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
    text_file.write("----------------------------------------------------------\n")
