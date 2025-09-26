# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

series_idades = pd.Series(idades)
series_idades = series_idades.sort_values()

#%%

# Usando o 'iloc'
# O iloc irá ignorar o indice da serie e o tratará
# como uma lista
# Esta buscando/navegando por linha

series_idades.iloc[-1]
# %%

series_idades.iloc[:3]
# %%

series_idades.iloc[::-1]
# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

indexs = [
    "Teó", "Maria", "jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty","Nih", "Pedro", "Kozato", "Tito",
]
series_idades = pd.Series(idades, index=indexs)
print(series_idades)
# %%
#Buscando por indice
print(series_idades["Teó"])
# %%
