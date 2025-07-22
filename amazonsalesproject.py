#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 10:50:33 2025

@author: bk
"""

# =============================================================================
# Loading the data 
# =============================================================================

import pandas as pd

sales_data = pd.read_excel(r'/Users/bk/Library/Mobile Documents/com~apple~CloudDocs/Spyder Projects/Udemy - Data Analysis/Dee Naidoo/Amazon Sales Project/sales_data.xlsx')


# =============================================================================
# Exploring the data
# =============================================================================
sales_data.info()

sales_data.describe()

print(sales_data.columns)

print(sales_data.head())

print(sales_data.dtypes)

# =============================================================================
# Cleaning the data
# =============================================================================

# check missing data in our dataset
sales_data.isnull()

# check missing data in our dataset - summed per column
print(sales_data.isnull().sum())

#drop any rows with nan (null) values
sales_data_dropped = sales_data.dropna()

# above is too many dropped rows. let's only drop those in amount column
sales_data_dropped_amount = sales_data.dropna(subset = ['Amount'])

# =============================================================================
# Slicing and Filtering Data
# =============================================================================

# select a subset of our data (Top) based on the Category Column - all the Tops we have sold. 
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)

# a subset of our data where amount is over 1000
high_amount_sales = sales_data[sales_data['Amount'] < 1000]
print(high_amount_sales)

# =============================================================================
# Aggregating Data
# =============================================================================

#Total Sales by Category 
category_totals = sales_data.groupby('Category', as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

#Calculate the average Amount by category and Fulfilment 
fulfilment_averages = sales_data.groupby(['Category','Fulfilment'], as_index=False)['Amount'].mean()
fulfilment_averages = fulfilment_averages.sort_values('Amount', ascending=False)

#Calculate the average Amount By Category and Status
status_averages = sales_data.groupby(['Category','Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount', ascending=False)

#Calculate total sales by shipment and Fulfilment 
total_sales_ShipandFulfil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_ShipandFulfil = total_sales_ShipandFulfil.sort_values('Amount', ascending=False)
total_sales_ShipandFulfil.rename(columns={'Courier Status': 'Shipment'}, inplace = True)

# =============================================================================
# Exporting The Data
# =============================================================================

# save the excel document without index in the folder stipulated above right. 
status_averages.to_excel('average_sales_by_category_and_status.xlsx', index=False)

# save second dataframe excel document
total_sales_ShipandFulfil.to_excel('total_sales_by_shipment_and_fulfilment.xlsx', index=False)









