#%%
import pandas as pd

df = pd.read_csv(r"C:\Users\User\Documents\SCRIPTS PYTHON\machine_learning\data\transacoes.csv", sep=';')

# %%
df.shape

# %%
df.info()

#%%
df.dtypes
# %%
df.head
# %%
renamed_columns = {"QtdePontos":"qtPontos",
                        "DescSistemaOrigem":"SistemaOrigem"}
df = df.rename(columns=renamed_columns)# Renomear colunas. Chave é nome da coluna a ser trocada e valor ó novo nome

# %%
df.rename(columns=renamed_columns, inplace=True) # Mesma função do comando acima

# %%
df[['IdCliente', 'qtPontos']] # Mostrar colunas selecionadas

# %%
colunas = df.columns.tolist() # Tranfosmar em uma lista
colunas.sort() # Ordenar em ordem alfabética
colunas

df = df[colunas] # Colunas reordenadas
df
