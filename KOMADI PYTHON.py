import pandas as pd
import numpy as np
import random

print ('rand_wtd(n) generates a weigted playlist with n songs') 

df = pd.read_excel('komadi-python.xlsx', usecols={1,2,4})
df.rename(columns={'Unnamed: 1':'Song name', 'Unnamed: 2':'Rating', 'Unnamed: 4':'Subgenre'}, inplace=True)

wtd = df.copy(deep=True)
wtd.rename(columns={'Rating':'Wt index'}, inplace=True)

wtd['Wt index'] = pd.to_numeric(wtd['Wt index'])
wtd['Wt index'] -= 90
wtd['Wt index'] = wtd['Wt index']**2

weights_ind_norm = wtd['Wt index'] / wtd['Wt index'].sum()  

def rand_wtd(n):
    print (wtd.sample(n, weights=weights_ind_norm))

rand_wtd(20)

#def rand_songs(n):
#     print (df.sample(n))







     
