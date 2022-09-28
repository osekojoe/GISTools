''' This script fills entries in a column with leading zeroes
- eg A1 -> A001, A01 -> A010, A100 -> A1000
'''
#%%
import pandas as pd

data = {'col': ['A1', 'A10', 'A100']}
df = pd.DataFrame(data)
df
#%%
'''index df to remove undesired parts; 
A is removed from the initial df col
'''
#df['col'] = df['col'].map(lambda x: x.rstrip('A'))
df['col'] = df['col'].map(lambda x: str(x)[1:])
df
#%%
''' Pad entries with zeroes to become 3-figure'''
df['col'] = df['col'].apply(lambda x: '{0:0>3}'.format(x))
print(df)

#%%
'''add A back to the df col after padding with zeroes'''
df['col_new'] = 'A' + df['col'].astype(str)
df