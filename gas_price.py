import pandas as pd

# reading the Excel sheet and taking the second row as the header
df = pd.read_excel('RNGWHHDm.xls', sheet_name="Data 1", header=2)

# renaming the columns especially the second column with just 'Price'
df.columns = ['Date', 'Price']

# changing the date format to contain the year, & the day, & then the month 
# and saving it back to the same column that has the Date
df['Date'] = df['Date'].dt.strftime('%Y-%d-%m')

# saving the dataframe to the final CSV file
df.to_csv("gas_price.csv")