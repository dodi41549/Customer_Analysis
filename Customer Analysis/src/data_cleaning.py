import pandas as pd

def drop_nulls(df, columns):
    return df.dropna(subset=columns)

def drop_duplicates(df):
    return df.drop_duplicates()
