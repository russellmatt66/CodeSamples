import pandas as pd

char_df = pd.read_csv('vanilla_growths.csv')

print(char_df.head())

df_nonnum = char_df.apply(pd.to_numeric, errors='coerce')

char_df['Total'] = df_nonnum.sum(axis=1, skipna=True)

print(char_df.head())

sort_char_df = char_df.sort_values(by=['Total'], ascending=False)

print(sort_char_df.head())

sort_char_df.to_csv('sorted_vanilla_growths.csv', index=False)
