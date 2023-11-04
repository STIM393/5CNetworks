import pandas as pd
import csv
#Read CSV file from directory CSV
df=pd.read_csv("./CSV/sales_data_1.csv")

#1.What is their overall gross margin for their business?
#To find out gross margin we have to remove cost of goods from netsales and remaining amount we have to find the percentage
#Gross margin is always showed as percenatge
data = []
with open('./CSV/sales_data_1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
total_revenue = 0
total_cost = 0
for transaction in data:
    selling_price = float(transaction['Selling price'])
    buying_price = float(transaction['Buying price'])
    quantity_sold = int(transaction['Quantity sold'])

    total_revenue += selling_price * quantity_sold
    total_cost += buying_price * quantity_sold
gross_margin = ((total_revenue - total_cost) / total_revenue) * 100
print(f"Overall Gross Margin: {gross_margin:.2f}%")

vendor_profits = df.groupby('Firm bought from')['Selling price'].sum() - df.groupby('Firm bought from')['Buying price'].sum()
most_profitable_vendor = vendor_profits.idxmax()
print(f"The most profitable vendor is: {most_profitable_vendor}")

customer_profits = df.groupby('Customer')['Selling price'].sum() - df.groupby('Customer')['Buying price'].sum()
least_profitable_customer = customer_profits.idxmin()
print(f"The least profitable customer is: {least_profitable_customer}")


df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
df['Day of Week'] = df['Date'].dt.day_name()

day_profits = df.groupby('Day of Week')['Selling price'].sum() - df.groupby('Day of Week')['Buying price'].sum()
most_profitable_day = day_profits.idxmax()
print(f"The most profitable day of the week is: {most_profitable_day}")

least_profitable_day = day_profits.idxmin()
print(f"The least profitable day of the week is: {least_profitable_day}")








