#%%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

nomes = [
    "Teó", "Maria", "jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty","Nih", "Pedro", "Kozato", "Tito",
]
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)


#%%

df = pd.DataFrame()
df["Idades"] =  series_idades # Foi criado uma coluna Idade com todos os valores de series_idades
df["Nomes"] = series_nomes # Foi criado uma coluna Idade com todos os valores de series_nomes

print(df)
# %%

df["Idades"] #Acessar uma coluna

# %%

df.iloc[0]
# %%
df.iloc[0]["Nomes"]
# %%
df.iloc[-1]["Idades"]

# %%
