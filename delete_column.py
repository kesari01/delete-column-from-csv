import pandas as pd

def delete_column(csv_file, column_name):
    df = pd.read_csv(csv_file)
    if column_name not in df.columns:
        print(f"Column '{column_name}' does not exist in the CSV file.")
        return

    df.drop(column_name, axis=1, inplace=True)
    df.to_csv(csv_file, index=False)
    print(f"Column '{column_name}' deleted successfully.")

# Example usage:
csv_file = 'data.csv'  # Replace with the path to your CSV file
column_name = 'gender'  # Replace with the name of the column you want to delete

delete_column(csv_file, column_name)
