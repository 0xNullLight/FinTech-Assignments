import csv
from pathlib import Path

# Function to create a list from a CSV file
def make_list(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip header row
        # Create a list by iterating through the CSV reader
        return [row for row in csv_reader]

# Function to generate a report based on menu and sales data
def make_report(menu_list, sales_list):
    report = {}  # Initialize a dictionary to store the report
    # Iterate through each row in the sales data
    for sales_item in sales_list:
        quantity, sales_item = int(sales_item[3]), sales_item[4]
        # If the sales item is not in the report, add it to the report dictionary
        if sales_item not in report:
            report[sales_item] = {'count': 0, 'revenue': 0, 'cost': 0, 'profit': 0}

        # Iterate through each row in the menu data to find matching items
        for menu_item in menu_list:
            if sales_item == menu_item[0]:
                menu_item_price, menu_item_cost = float(menu_item[3]), float(menu_item[4])
                profit = menu_item_price - menu_item_cost
                # Update the report with the calculated metrics
                cur_item = report[sales_item]
                cur_item['count'] += quantity
                cur_item['revenue'] += menu_item_price * quantity
                cur_item['cost'] += menu_item_cost * quantity
                cur_item['profit'] += profit * quantity
    return report

# Function to write the report in table format to a Markdown file
def write_table_report(report, report_path, mode):
    with open(report_path, mode) as report_file:
        report_file.write('# PyRamen Report\n')
        report_file.write('\n|Item|Count|Revenue|Cost|Profit|\n')
        report_file.write('|---|---|---|---|---|\n')
        # Iterate through the report dictionary and write each item's metrics in table format
        for item, cur in report.items():
            report_file.write(f'|{item.title()}|{cur["count"]}|{cur["revenue"]}|{cur["cost"]}|{cur["profit"]}|\n')

# Function to write the report in list format to a Markdown file
def write_list_report(report, report_path, mode):
    with open(report_path, mode) as report_file:
        # Iterate through the report dictionary and write each item's metrics in list format
        for item, cur_item in report.items():
            report_file.write(f'\n## {item.title()}\n')
            report_file.write(f'\n- Count: {cur_item["count"]}\n')
            report_file.write(f'- Revenue: {cur_item["revenue"]}\n')
            report_file.write(f'- Cost: {cur_item["cost"]}\n')
            report_file.write(f'- Profit: {cur_item["profit"]}\n')

if __name__ == '__main__':
    menu_data = Path('data/menu_data.csv')
    sales_data = Path('data/sales_data.csv')
    report_file = Path('gen/report.md')

    # Create lists from CSV files containing menu and sales data
    menu = make_list(menu_data)
    sales = make_list(sales_data)

    # Generate the report based on the provided data
    report = make_report(menu, sales)

    # Write the report in table format and then in list format to a Markdown file
    write_table_report(report, report_file, 'w')
    write_list_report(report, report_file, 'a')

