import pandas as pd
import os
file_path = 'sales_data.csv'
if not os.path.isfile(file_path):
    print(f"File '{file_path}' not found.")
else:
    data = pd.read_csv(file_path)
    data['Total_Sale'] = data['Quantity'] * data['Price']
    category_sales = data.groupby('Category')['Total_Sale'].sum().reset_index()
    output_filename = 'category_sales.csv'
    category_sales.to_csv(output_filename, index=False)
    full_path = os.path.abspath(output_filename)

    print(f"Total sales per category calculated and saved to:\n {full_path}")