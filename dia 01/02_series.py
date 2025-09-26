# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]


#%%
media = sum(idades)/len(idades)
print(f"{media:.2f}")

#%%
diffs = 0
for i in idades:
    diffs += (i - media) ** 2 

variancia = diffs / (len(idades)-1)

print("Variância: ", variancia)

#%%

import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%

media_id = series_idades.mean()
var_id = series_idades.var()
sumury_id = series_idades.describe()
print(media_id)
print(var_id)
print(sumury_id)
# %%
