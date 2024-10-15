import pandas as pd
# import numpy as np

def main():
    df = pd.read_csv('iris_with_errors.csv')

    missing_data = df.isnull().sum()
    print("Missing or incomplete data:\n", missing_data)
    print("\nDataframe statistics with errors:\n", df.describe(include='all'))

    numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
    for column in numeric_columns:
        mean_value = df[column].mean()
        df[column] = df[column].apply(lambda x: mean_value if x <= 0 or x > 15 else x)

    valid_species = ["Setosa", "Versicolor", "Virginica"]
    df['variety'] = df['variety'].apply(lambda x: x.capitalize() if x.lower() in [s.lower() for s in valid_species] else x)

    incorrect_species = df[~df['variety'].isin(valid_species)]
    print("\nIncorrect species names:\n", incorrect_species['variety'].unique())

    df['variety'] = df['variety'].replace("Versicolour", "Versicolor")
    print("\nCleaned dataframe:\n", df.head())

    return

if __name__ == "__main__":
    main()