import pandas as pd

df = pd.read_excel("C:\Users\Suraj Gupta\Downloads\python QUESTION.xlsx")

rows_per_file = 4

n_chunks = len(df) // rows_per_file

for i in range(n_chunks):
    start = i*rows_per_file
    stop = (i+1) * rows_per_file
    sub_df = df.iloc[start:stop]
    sub_df.to_excel("C:\Users\Suraj Gupta\Downloads\{i}.xlsx", sheet_name="a")#C:\Users\Suraj Gupta\Downloads\{i}.xlsx
if stop < len(df):
    sub_df = df.iloc[stop:]
    sub_df.to_excel(f"/output/path/to/test-{i}.xlsx", sheet_name="a")