import pandas as pd
import os

data_folder = "data"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

if not csv_files:
    print("No CSV files found in the data folder.")
else:
    for file in csv_files:
        file_path = os.path.join(data_folder, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 50)
            print("File:", file)
            print("Shape:", df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")