#%%
import pandas as pd
df=pd.read_csv('data/dc_data.csv',skiprows=2,skipfooter=6)

# %%
shape=df.shape
r,c=shape[0],shape[1]

# %%
df.to_excel('data/out.csv',index=False)

# %%
