import pandas as pd

# Load the Excel file
df = pd.read_excel(r'C:\data\Sample3.xlsx')  # Use raw string for file path

# Print the size of the DataFrame
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

# Print column names to verify
print(df.columns.tolist())
