import pandas as pd
import numpy as np

def count_null(df):
    print(df.isnull().sum())

def replace_out_of_range_with_nan(df, min_value=0, max_value=15):
    for column in df.columns:
        if column != 'variety':
            df[column] = df[column].apply(lambda x: np.nan if x < min_value or x > max_value else x)

def replace_invalid_variety(df, valid_varieties):
    invalid_rows = df[~df['variety'].isin(valid_varieties)]
    
    print("Wiersze z nieprawidłowymi wartościami w kolumnie 'variety':")
    print(invalid_rows)
    
    df['variety'] = df['variety'].apply(lambda x: x if x in valid_varieties else np.nan)

def find_similar_variety(df, row_idx, tolerance=1):
    row_to_check = df.loc[row_idx]
    for idx, row in df.iterrows():
        if idx != row_idx and not pd.isna(row['variety']):
            similar = True
            for column in df.columns:
                if column != 'variety':
                    if abs(row_to_check[column] - row[column]) > tolerance:
                        similar = False
                        break
            if similar:
                return row['variety']
    return None

def fill_missing_variety(df, tolerance_step=1):
    for idx, row in df[df['variety'].isna()].iterrows():
        tolerance = tolerance_step
        similar_variety = None
        while similar_variety is None:
            similar_variety = find_similar_variety(df, idx, tolerance)
            tolerance += tolerance_step 
        
        df.loc[idx, 'variety'] = similar_variety

def main():
    missing_flags = ['n/a', '-', 'na', '--']
    valid_varieties = ["Setosa", "Versicolor", "Virginica"]
    df = pd.read_csv('iris_with_errors.csv', na_values=missing_flags)

    count_null(df)

    replace_out_of_range_with_nan(df)
    replace_invalid_variety(df, valid_varieties)
    print("Po zmianie numerów z poza zakresu:")
    count_null(df)


    fill_missing_variety(df)
    print("Po uzupełnieniu brakujących wartości variety:")
    count_null(df)
    
    for column in df.columns:
        if column != 'variety':
            median = df[column].median()
            df[column] = df[column].fillna(median)
    
    print("po wyrównaniu wartości do zakresu 0-15")
    count_null(df)

    df.to_csv('iris_cleaned.csv', index=False)

    

if __name__ == "__main__":
    main()

# # Detecting numbers 
# cnt=0
# for row in df['OWN_OCCUPIED']:
#     try:
#         int(row)
#         df.loc[cnt, 'OWN_OCCUPIED']=np.nan
#     except ValueError:
#         pass
#     cnt+=1

# # Any missing values
# print df.isnull().values.any()


# # Total number of missing values
# print df.isnull().sum().sum()

# # Replace missing values with a number
# df['ST_NUM'].fillna(125, inplace=True)

# # Location based replacement
# df.loc[2,'ST_NUM'] = 125

# # Replace using median 
# median = df['NUM_BEDROOMS'].median()
# df['NUM_BEDROOMS'].fillna(median, inplace=True)

# # DROP COLUMNS
# to_drop = ['name']
# df.drop(to_drop, inplace=True, axis=1)